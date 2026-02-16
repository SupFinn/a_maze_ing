*This project has been created as part of the 42 curriculum by mlakhlil and rhssayn.*

# 🎮 **A-Maze-ing**

## 📌 **Description**

**A-Maze-ing** is a Python-based maze generation and solution visualizer. The goal of this project is to algorithmically generate mazes, visualize their creation process in real-time within the terminal, and solve them using pathfinding algorithms.

The project features a modular design allowing for different generation algorithms, customizable colors, and a specific "42" pattern embedded within the maze walls. It uses ANSI escape codes to render animations directly in the console.

---

## 📖 **Instructions**

### 📋 **Prerequisites**

* Python 3.10 or higher.  
* pip package manager.

### 💾 **Installation**

To install the necessary dependencies (flake8, mypy for linting), run:
```bash
make install
```

### ▶️ **Execution**

To generate and solve a maze using the default configuration:
```bash
make run
```

Or manually:
```bash
python3 a_maze_ing.py config.txt
```

### 🎮 **Interactive Controls**

Once the maze is generated and solved, an interactive menu allows you to:

1. **Re-generate maze:** 🔄 Create a new maze with the current settings (or new seed).  
2. **Show/Hide solution:** 👁️ Toggle the visibility of the pathfinding solution.  
3. **Change colors:** 🎨 Customize wall and pattern colors.  
4. **Change Algorithm:** ⚙️ Switch between Backtracking and Prim's algorithm on the fly.

### 🔧 **Other Commands**

* `make lint` 🔍: Run code quality checks (flake8 and mypy).  
* `make clean` 🧹: Remove cache files and temporary artifacts.

---

## ⚙️ **Configuration File Structure**

The behavior of the generator is controlled by a config.txt file. The format is KEY=VALUE (no spaces around the equals sign).

**Example config.txt:**
```
# Maze config
WIDTH=15
HEIGHT=13
ENTRY=0,0
EXIT=14,12
OUTPUT_FILE=maze.txt
PERFECT=false
SEED=42
```

| Key | Description |
| :---- | :---- |
| WIDTH | 📏 Integer. The width of the maze grid. |
| HEIGHT | 📏 Integer. The height of the maze grid. |
| ENTRY | 🟢 Tuple x,y. Coordinates for the starting point. |
| EXIT | 🔴 Tuple x,y. Coordinates for the ending point. |
| OUTPUT_FILE | 💾 String. Filename to save the hexagonal representation of the maze. |
| PERFECT | ✨ Boolean (true/false). If true, the maze has no loops. If false, walls are removed to create loops. |
| SEED | 🌱 Integer (Optional). Seed for random generation to reproduce specific mazes. |

---

## 🔀 **Maze Generation Algorithms**

We selected two distinct algorithms to provide variety in the visual generation process and the resulting maze structure:

### 1️⃣ **Recursive Backtracking (DFS):**  
* **Description:** A "drunken walk" approach that carves passages until it hits a dead end, then backtracks to the last valid cell.  
* **Why we chose it:** It produces long, winding corridors with fewer dead ends, making the maze look like a river or a snake. It is visually satisfying to watch the "stack" operation in the animation.

### 2️⃣ **Prim's Algorithm:**  
* **Description:** Starts from a grid full of walls and grows the maze from a starting cell by adding random frontier neighbors.  
* **Why we chose it:** In contrast to DFS, Prim's generates a branching structure with many short dead ends. It creates a more "organic" spread during the visualization, offering a different challenge to the solver.

### 🎯 **Solving Algorithm:**

* **BFS (Breadth-First Search):** 🔍 Used to find the shortest path from Entry to Exit. It guarantees the optimal solution in an unweighted grid.

---

## 🔧 **Reusable Code**

The project is structured as a package (mazegen), separating logic from the execution script.

* **mazegen/maze_generator.py** 🏗️: The MazeGenerator class is entirely reusable. It can be imported into other projects (e.g., a GUI-based maze game or a web backend) to generate grid data structures without relying on the terminal display.  
* **mazegen/maze_display.py** 🎨: The ANSI color logic is encapsulated here. While specific to terminal output, the class structure allows it to be swapped for a GUI-based display class (like PyGame) while keeping the Generator logic used in a_maze_ing.py intact.

---

## 👥 **Team and Project Management**

### 👨‍💼 **Roles**

* **mlakhlil** 🧠: Focused heavily on the core algorithmic logic. Implemented the **Backtracking** and **Prim's** generation algorithms and handled the primary visualization logic for the grid.  
* **rhssayn** 🎨: Focused on the **User Experience** and specific constraints. Implemented the hardcoded **"42" pattern**, the **BFS Pathfinding** algorithm, the animation delays, and the interactive menu system (changing colors, toggling paths).

### 📅 **Planning & Evolution**

We initially planned to work on the entire project simultaneously. However, as we progressed, we naturally discovered different approaches to managing the maze data and visualization.

* **Evolution:** Instead of forcing a single workflow, we pivoted to leverage our individual strengths. We split the workload: one focused on the "math/logic" (algorithms) and the other on the "features/polish" (patterns, solving, UX).  
* **Convergence:** In the final phase, we sat down together to integrate the features and ensure the code adhered to the requirements. This pair-programming session helped us understand each other's perspectives and debug edge cases.

### 🎯 **Retrospective**

* **What worked well:** ✅ Dividing tasks based on interest (Algorithms vs. UX) resulted in a polished product with robust logic. The final integration phase was crucial for knowledge transfer.  
* **Improvements:** 🔄 Initial synchronization could have been better to avoid minor merge conflicts in the core Cell structure early on.

### 🛠️ **Tools Used**

* **Custom Simulator:** 🔬 We built a simple web-based simulation tool to visualize how the algorithms propagate. This saved significant time compared to debugging purely through terminal text output.  
* **Git:** 📦 For version control.

---

## 📚 **Resources**

* **Algorithms:** 🔗 [Wikipedia - Maze generation algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm)  
* **Python Typing:** 🔗 [Python Docs - typing](https://docs.python.org/3/library/typing.html)

### 🤖 **AI Usage**

AI was utilized as a supportive tool throughout the development process:

1. **Algorithm Understanding:** 🧠 Used to break down the steps of Prim's algorithm to ensure correct implementation of the "frontier" logic.  
2. **Code Organization:** 📁 Assisted in structuring the project into a proper Python package (handling __init__.py and imports).  
3. **Optimization & Verification:** ✅ Used to check for potential infinite loops in the while structures and to verify that no requirements from the subject were missed during the final review.

---

## 👤 Author

*Created as part of the 42 curriculum — Functional Programming Mastery*

If this project helped you master functional programming, feel free to ⭐ the repository!

**Functional programming makes code more elegant, reusable, and powerful. You've learned to think in terms of functions, composition, and data transformation.** 🧙✨