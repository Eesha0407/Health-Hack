# 🧬 HealthHack 2.0: The Graph Edition

> **Train Smarter. Not Harder. Powered by Medical-Grade Graph Intelligence.**

HealthHack 2.0 is a next-generation fitness and health-tech application designed for a hackathon demo. Unlike generic fitness trackers, HealthHack 2.0 acts as a **"Graph-powered decision engine for safe training."** It uses Knowledge Graph concepts to dynamically analyze a user's biometric data, fitness goals, and active injuries to prune contraindicated exercises and route them to safe alternatives.

---

## ✨ Core Features

### 1. Interactive UI Flow
A clean, accessible user journey from the landing page to a comprehensive health dashboard, capturing essential biometrics, dietary preferences, and injury data.

### 2. Clinical Nutrition Configurator
Maps active injuries to specific dietary interventions (e.g., Turmeric for Patellar Tendonitis). 

### 3. Safe Workout Routing (Concept)
A conceptual visualizer designed to map:
`User Profile ➔ Fitness Goal ➔ Standard Exercises ➔ Biomechanics (Joints/Muscles) ➔ Safe Replacements`
* 🟢 **Green Paths:** Safe routing.
* 🔴 **Red Paths:** Blocked nodes due to contraindications.

### 4. Comprehensive Health Dashboards
* **Exercise & Injury Protocol:** Side-by-side comparisons of standard workout routines vs. optimized safe routines.
* **AI Insights:** Dual-mode explanations ("Explain Like I'm 5" vs. Technical Traversal Logic) that explain *why* certain exercises were pruned from your routine.

---

## 🛠 Tech Stack

Built for maximum speed and simplicity for the hackathon demo, requiring zero build tools or backend dependencies.

* **Frontend:** HTML5, CSS3
* **Styling:** Custom CSS (Responsive, medical-grade UI with glassmorphic elements)
* **Interactivity:** Vanilla JavaScript (for form handling and dashboard logic)
* **Assets:** Custom background imagery and native HTML elements

---

## 🚀 How to Run Locally

Because this project is built with pure web technologies, setup is instantaneous. 

1. **Clone or Download the Repository:**
   Save the project files to your local machine.

2. **Run the App:**
   Simply double-click on `index.html` to open it in any modern web browser (Chrome, Firefox, Safari, Edge). 
   *No servers, no `npm install`, no waiting.*

3. **Navigation:**
   Use the UI buttons to navigate from `index.html` ➔ `secondpage.html` ➔ `dashboard.html`.

---

## 🔮 Future Roadmap (Post-Hackathon)
* **Graph Database Integration:** Move the conceptual data to a proper graph database (like TigerGraph) for infinite scalability.
* **Wearable Integration:** Pull live biomechanical stress data from Apple Health / Garmin.
* **Generative AI Expansion:** Plug in the Gemini API to generate custom daily routines based on the graph's pruning output.

## 👩‍💻 Meet the Team

**HealthHack 2.0** was conceptualized and developed by:

| Member | Role | Key Responsibilities |
| :--- | :--- | :--- |
| **Ananya** | Lead Developer (AI & Graph) | TigerGraph Cloud setup, GSQL schema design, pyTigerGraph backend integration, and Gemini API implementation for natural language advice. |
| **Eesha** | Frontend Engineer | Dashboard development, UI forms for injury logging, and repository management. |
| **Ishvi** | Product Lead & Pitch | Market research on injury prevention, PPT design (focusing on the "Why Graph"), and project documentation. |
| **Aashi** | UI/UX & Integration | "Health Map" visualization design, UI layout, and end-to-end testing for the demo. |

---
*Built with ❤️ for HealthHack 2.0*
