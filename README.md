# 🧬 HealthHack 2.0: The Graph Edition

> **Train Smarter. Not Harder. Powered by Medical-Grade Graph Intelligence.**

HealthHack 2.0 is a next-generation fitness and health-tech application by team **ByteNova**. Unlike generic fitness trackers, HealthHack 2.0 acts as a **"Graph-powered decision engine for safe training."** It uses an active Knowledge Graph (TigerGraph) to dynamically analyze a user's biometric data, fitness goals, and active injuries to prune contraindicated exercises and route them to safe alternatives.

---

## ✨ Core Features

### 1. TigerGraph-Powered Safe Workout Routing
We have moved beyond conceptual routing. HealthHack 2.0 now actively queries a live TigerGraph database via a Python/Flask REST API. 
* 🟢 **Safe Exercises:** The graph dynamically returns exercises verified as safe based on the user's specific injury nodes.
* 🔴 **Pruned Contraindications:** Aggravating exercises are automatically filtered out of the user's dashboard based on graph traversal logic.

### 2. Interactive Web Dashboard
A clean, accessible user journey that captures essential biometrics, dietary preferences, and injury data. The application maintains state dynamically, updating workout recommendations and health scores in real-time as the user's physical constraints change.

### 3. Dynamic Clinical Nutrition Configurator
Personalized macronutrient breakdowns and meal plans generated dynamically based on the user's primary fitness goal (e.g., Muscle Gain, Weight Loss, Rehabilitation) and dietary preferences (Vegan, Vegetarian, Non-Vegetarian).

### 4. Injury Context Management
Users can update their active injuries (e.g., "Knee Pain", "Lower Back Pain"), instantly recalibrating the Knowledge Graph to route around the affected muscle groups and update the daily training plan.

---

## 🛠 Tech Stack

HealthHack 2.0 has evolved into a robust full-stack application:

* **Frontend:** HTML5, CSS3 (Glassmorphic, medical-grade UI)
* **Backend:** Python, Flask, Flask-CORS
* **Database / Engine:** TigerGraph Cloud (GSQL)
* **Data Management:** Dynamic CSV data loading for exercises and injury mapping via backend processing.

---

## 🚀 How to Run Locally

### 1. Start the Backend Server (Python/Flask)
Ensure you have Python installed, then install the required dependencies and start the API:
```bash
pip install flask flask_cors requests
python app.py
```

*The server will start on `http://127.0.0.1:5000` and automatically connect to the TigerGraph instance.*

### 2. Start the Frontend 
Simply double-click on `index.html` to open it in your browser (Chrome, Firefox, Safari, Edge). *No build tools or npm required.*

---

## 🔮 Future Roadmap 
* **Wearable Integration:** Pull live biomechanical stress data and heart rate metrics from Apple Health / Garmin via their respective APIs.
* **Generative AI Expansion:** Deepen the Gemini API implementation to generate highly customized, day-by-day conversational fitness routines based on the graph's pruning output.
* **Expanded Graph Topology:** Add more granular nodes to the TigerGraph schema (e.g., specific ligament tracking, recovery timeframes, and micro-nutrient impacts).

---

## 👩‍💻 Meet the Team

**HealthHack 2.0** was conceptualized and developed by team **ByteNova**:

| Member | Role | Key Responsibilities |
| :--- | :--- | :--- |
| **Ananya** | Lead Developer (AI & Graph) | Python/Flask backend integration, TigerGraph Cloud API routing, and AI implementation. |
| **Eesha** | Frontend Engineer | Dashboard development, UI forms for injury logging, and repository management. |
| **Ishvi** | Product Lead & Pitch | Market research on injury prevention, PPT design (focusing on the "Why Graph"), and project documentation. |
| **Aashi** | UI/UX & Integration | "Health Map" visualization design, CSS styling, UI layout, and end-to-end testing for the demo. |

---
*Built with ❤️ by ByteFours*
