# 🧬 HealthHack 2.0: The Graph Edition

> **Train Smarter. Not Harder. Powered by Medical-Grade Graph Intelligence.**

HealthHack 2.0 is a next-generation fitness and health-tech application designed for a hackathon demo. Unlike generic fitness trackers, HealthHack 2.0 acts as a **"Graph-powered decision engine for safe training."** It uses an in-memory Knowledge Graph to dynamically analyze a user's biometric data, fitness goals, and active injuries to prune contraindicated exercises and route them to safe alternatives in real-time.

---

## ✨ Core Features

### 1. Real-Time "What-If" Simulation Engine
Toggle active injuries (e.g., Wrist Strain, Knee Pain) and watch the Knowledge Graph instantly recalculate your safe workout path without requiring a page reload.

### 2. Interactive SVG Graph Visualization
A bespoke, dynamic SVG network graph that visually maps:
`User Profile ➔ Fitness Goal ➔ Standard Exercises ➔ Biomechanics (Joints/Muscles) ➔ Safe Replacements`
* 🟢 **Green Paths:** Safe routing.
* 🔴 **Red Paths:** Blocked nodes due to contraindications.

### 3. Adjustable Graph Traversal Depth
A slider controls the depth of the algorithm:
* **2-Hop (Shallow):** Basic Goal ➔ Exercise matching.
* **3-Hop (Deep):** Analyzes biomechanics for conflicts.
* **4-Hop (Max Depth):** Prunes dangerous paths and maps to optimal safe alternatives.

### 4. Comprehensive Health Dashboards
* **Exercise & Injury Protocol:** Side-by-side comparisons of standard workout routines vs. graph-optimized safe routines.
* **Clinical Nutrition Configurator:** Maps active injuries to specific dietary interventions (e.g., Turmeric for Patellar Tendonitis). Includes a daily macro tracker.
* **BMI Calculator:** A responsive visual gauge tracking Body Mass Index in real-time.
* **AI Insights:** Dual-mode explanations ("Explain Like I'm 5" vs. Technical Traversal Logic) that explain *why* certain exercises were pruned from your routine.

---

## 🛠 Tech Stack

Designed for maximum performance and visual impact with zero backend dependencies for the hackathon demo.

* **Frontend Framework:** React 18 (Functional Components, Hooks, `useMemo` for optimization)
* **Styling:** Tailwind CSS (Modern, glassmorphic, medical-grade UI)
* **Icons:** Lucide-React
* **Visualizations:** Custom DOM/SVG rendering (No heavy charting libraries required)
* **Routing:** Custom lightweight in-memory router (Zero external dependencies)
* **Database:** Mock JSON Knowledge Graph (In-memory)

---

## 🚀 How to Run Locally

Because this project is consolidated into a single highly-modular `App.jsx` file, setup is incredibly fast.

### Prerequisites
Make sure you have [Node.js](https://nodejs.org/) installed.

### Setup Instructions

1. **Create a new React app (Vite recommended for speed):**
   ```bash
   npm create vite@latest healthhack -- --template react
   cd healthhack
   ```

2. **Install Dependencies:**
   ```bash
   npm install
   npm install lucide-react
   ```

3. **Install Tailwind CSS:**
   ```bash
   npm install -D tailwindcss postcss autoprefixer
   npx tailwindcss init -p
   ```

   *Configure your `tailwind.config.js` to scan your React files:*
   ```javascript
   export default {
     content: [
       "./index.html",
       "./src/**/*.{js,ts,jsx,tsx}",
     ],
     theme: { extend: {} },
     plugins: [],
   }
   ```

   *Add Tailwind directives to your `src/index.css` (or `App.css`):*
   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```

4. **Add the Code:**
   Replace the contents of `src/App.jsx` with the `App.jsx` code provided in this repository.

5. **Run the Development Server:**
   ```bash
   npm run dev
   ```
   Open `http://localhost:5173` in your browser.

---

## 🧠 How the Graph Traversal Works (Under the Hood)

The engine relies on a `useMemo` hook that acts as our graph traversal algorithm. 
1. It looks at the user's **Goal** and pulls the `defaultExercises` array.
2. It loops through active **Injuries** and generates a `Set` of blocked **Biomechanics** (e.g., *j_wrists*, *j_knees*).
3. It maps the standard exercises to their target biomechanics. If a target intersects with the blocked `Set`, the node is flagged as a `conflict`.
4. If `Graph Depth >= 4`, the engine checks the graph for a predefined `alt` (alternative) exercise. It runs the alternative through the same safety check before adding it to the `safeExercises` array.

---

## 🔮 Future Roadmap (Post-Hackathon)
* **Neo4j / GraphQL Integration:** Move the in-memory mock data to a proper graph database for infinite scalability.
* **Wearable Integration:** Pull live biomechanical stress data from Apple Health / Garmin.
* **Generative AI Expansion:** Plug in the Gemini/OpenAI API to generate custom daily routines based on the graph's pruning output.

## 👩‍💻 Meet the Team

**HealthHack 2.0** was conceptualized and developed by:

| Member | Role | Key Responsibilities |
| :--- | :--- | :--- |
| **Ananya** | Lead Developer (AI & Graph) | TigerGraph Cloud setup, GSQL schema design, pyTigerGraph backend integration, and Gemini API implementation for natural language advice. |
| **Eesha** | Frontend Engineer | React dashboard development, UI forms for injury logging, and GitHub repository management (Vercel deployment). |
| **Ishvi** | Product Lead & Pitch | Market research on injury prevention, PPT design (focusing on the "Why Graph"), and project documentation for Unstop/IIT Delhi. |
| **Aashi** | UI/UX & Integration | "Health Map" visualization design, JavaScript logic assistance, and end-to-end testing for the demo. |

---
*Built with ❤️ for HealthHack 2.0*
