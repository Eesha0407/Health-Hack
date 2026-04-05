from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import csv
import os

app = Flask(__name__)
CORS(app)

# --- CONFIGURATION ---
HOST = "https://tg-b1268d3a-0bc5-4c61-b288-b86fe810bd12.tg-2635877100.i.tgcloud.io"
SECRET = "guenj4tm0a7p4l9tvlqcso31k3d75db1"
GRAPH_NAME = "HealthGraph"

# --- DYNAMIC DATA LOADING ---
injury_dict = {}
exercise_dict = {}

def load_data():
    global injury_dict, exercise_dict
    
    # Load Injuries (Mapping Name -> ID for TigerGraph)
    try:
        if os.path.exists('injuries.csv'):
            with open('injuries.csv', mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    injury_dict[row['name']] = row['id']
            print(f"Successfully loaded {len(injury_dict)} injuries.")
        else:
            print("Warning: injuries.csv not found.")
    except Exception as e:
        print(f"Error loading injuries.csv: {e}")

    # Load Exercises (Mapping ID -> Name for the UI)
    try:
        if os.path.exists('exercise.csv'):
            with open('exercise.csv', mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    exercise_dict[row['id']] = row['exercise_name']
            print(f"Successfully loaded {len(exercise_dict)} exercises.")
        else:
            print("Warning: exercise.csv not found.")
    except Exception as e:
        print(f"Error loading exercise.csv: {e}")

# Run data loading on startup
load_data()

@app.route('/api/get_safe_workouts', methods=['GET'])
def get_safe_workouts():
    user_injury = request.args.get('injury')
    
    # If "No Injury" is selected, return all known exercises from the CSV
    if not user_injury or user_injury == "No Injury" or user_injury not in injury_dict:
        return jsonify({"safe_exercises": list(exercise_dict.values())})

    try:
        injury_id = injury_dict[user_injury]
        
        # --- TIGERGRAPH QUERY CALL ---
        # Using GSQL-Secret header for direct authentication
        query_url = f"{HOST}/restpp/query/{GRAPH_NAME}/find_safe_workouts?active_injury={injury_id}"
        headers = {"Authorization": f"GSQL-Secret {SECRET}"}
        
        print(f"DEBUG: Querying Graph for injury ID: {injury_id}")
        response = requests.get(query_url, headers=headers)
        
        if response.status_code != 200:
            print(f"Graph Error: {response.text}")
            return jsonify({"error": "Database communication error"}), 500

        data = response.json()
        results = data.get("results", [])

        # Parse results: TigerGraph returns a list of vertices
        safe_exercise_names = []
        if results:
            # Adjust 'SafeExercises' to match exactly what your GSQL PRINTs
            safe_vertices = results[0].get("SafeExercises", [])
            for vertex in safe_vertices:
                v_id = vertex.get("v_id")
                if v_id in exercise_dict:
                    safe_exercise_names.append(exercise_dict[v_id])

        return jsonify({"safe_exercises": safe_exercise_names})

    except Exception as e:
        print(f"Backend Crash: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/get_nutrition_tips', methods=['GET'])
def get_nutrition_tips():
    goal = request.args.get('goal', 'General Fitness')
    preference = request.args.get('preference', 'Vegetarian')

    # Logical mapping for nutrition tips
    nutrition_data = {
        "Muscle Gain": {
            "title": "High Protein Growth Plan",
            "macros": {"protein": "45%", "carbs": "35%", "fats": "20%"},
            "description": f"Focusing on {preference} protein sources to repair muscle tissue after your graph-optimized workouts.",
            "meals": {
                "Non-Vegetarian": ["Grilled Chicken Breast", "Greek Yogurt", "Lean Beef Stir-fry"],
                "Vegan": ["Tofu Scramble", "Lentil Soup", "Tempeh Power Bowl"],
                "Vegetarian": ["Paneer Tikka", "Sprouted Moong Salad", "Whey Protein Shake"]
            }
        },
        "Weight Loss": {
            "title": "Calorie Deficit Focus",
            "macros": {"protein": "40%", "carbs": "20%", "fats": "40%"},
            "description": "A balanced low-carb approach to maximize fat oxidation while maintaining satiety.",
            "meals": {
                "Non-Vegetarian": ["Baked Salmon with Asparagus", "Turkey Wrap", "Boiled Eggs"],
                "Vegan": ["Chickpea Salad", "Zucchini Noodles", "Roasted Chickpeas"],
                "Vegetarian": ["Moong Dal Chilla", "Low-fat Curd with Berries", "Vegetable Soup"]
            }
        },
        "General Fitness": {
            "title": "Balanced Maintenance Plan",
            "macros": {"protein": "30%", "carbs": "40%", "fats": "30%"},
            "description": "A sustainable mix of macronutrients to support energy levels for your daily activities.",
            "meals": {
                "Non-Vegetarian": ["Chicken Salad", "Tuna Sandwich", "Stir-fried Veggies"],
                "Vegan": ["Quinoa Bowl", "Fruit Smoothie with Pea Protein", "Hummus & Veggies"],
                "Vegetarian": ["Brown Rice & Lentils", "Cottage Cheese Wrap", "Mixed Nut Mix"]
            }
        },
        "Rehabilitation": {
            "title": "Recovery & Inflammation Control",
            "macros": {"protein": "35%", "carbs": "35%", "fats": "30%"},
            "description": "Emphasizing anti-inflammatory foods to support joint and tissue repair during your recovery phase.",
            "meals": {
                "Non-Vegetarian": ["Fatty Fish (Omega-3s)", "Bone Broth", "Chicken and Ginger Soup"],
                "Vegan": ["Chia Seed Pudding", "Turmeric Cauliflower", "Walnut & Spinach Salad"],
                "Vegetarian": ["Turmeric Milk (Golden Milk)", "Fruit & Nut Parfait", "Soya Chunks Stir-fry"]
            }
        }
    }

    # Fallback logic
    selected_plan = nutrition_data.get(goal, nutrition_data["General Fitness"])
    meals = selected_plan["meals"].get(preference, selected_plan["meals"]["Vegetarian"])

    return jsonify({
        "title": selected_plan["title"],
        "description": selected_plan["description"],
        "macros": selected_plan["macros"],
        "meals": meals
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)
