from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# --- CONFIGURATION (Sanitized for GitHub) ---
# Replace these with your own credentials from the TigerGraph portal
HOST = "YOUR_TIGERGRAPH_HOST_URL_HERE"
SECRET = "YOUR_TIGERGRAPH_SECRET_HERE"
GRAPH_NAME = "HealthGraph"

# --- TRANSLATION DICTIONARIES ---
injury_dict = {"Lower Back Pain": "i1", "Knee Pain": "i2", "Wrist Pain": "i3", "Shoulder Injury": "i4"}
exercise_dict = {
    "e1": "Barbell Squat", "e2": "Deadlift", "e3": "Bench Press", "e4": "Pull-ups", 
    "e5": "Plank", "e6": "Push-ups", "e7": "Walking Lunges", "e8": "Overhead Press",
    "e9": "Bicep Curls", "e10": "Tricep Dips", "e11": "Leg Press", "e12": "Glute Bridges", 
    "e13": "Lat Pulldowns", "e14": "Calf Raises", "e15": "Russian Twists"
}

@app.route('/api/get_safe_workouts', methods=['GET'])
def get_safe_workouts():
    user_injury = request.args.get('injury')
    
    # If no injury or unknown injury, return all exercises
    if user_injury not in injury_dict:
        return jsonify({"safe_exercises": list(exercise_dict.values())})

    try:
        injury_id = injury_dict[user_injury]
        
        # --- THE BYPASS MAGIC ---
        # We call the query directly and use "GSQL-Secret" instead of a Token
        query_url = f"{HOST}/restpp/query/{GRAPH_NAME}/find_safe_workouts?active_injury={injury_id}"
        
        # Use GSQL-Secret header to skip token generation
        headers = {"Authorization": f"GSQL-Secret {SECRET}"}
        
        print(f"DEBUG: Calling query at: {query_url}")
        query_response = requests.get(query_url, headers=headers)
        results = query_response.json().get("results", [])

        # Parse results
        safe_exercise_names = []
        if results:
            safe_list = results[0].get("SafeExercises", [])
            for ex in safe_list:
                v_id = ex.get("v_id")
                if v_id in exercise_dict:
                    safe_exercise_names.append(exercise_dict[v_id])

        return jsonify({"safe_exercises": safe_exercise_names})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Graph communication failed"}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
