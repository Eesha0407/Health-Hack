const BASE_URL = "http://127.0.0.1:5000/api";

export const getSafeWorkouts = async (injury) => {
  try {
    // encodeURIComponent handles the spaces in names like "Knee Pain"
    const response = await fetch(`${BASE_URL}/get_safe_workouts?injury=${encodeURIComponent(injury)}`);
    
    if (!response.ok) throw new Error("Network response was not ok");

    const data = await response.json();
    return data.safe_exercises || []; 
  } catch (error) {
    console.error("Error fetching data from Flask:", error);
    return [];
  }
};
