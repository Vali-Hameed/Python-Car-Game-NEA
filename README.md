# Python Car Racing Game - A-Level Computer Science NEA

This project is a 2D car racing game developed using Pygame. It was created as my first major Python project for my A-Level Computer Science NEA (Non-Exam Assessment).

## Project Overview

The game features multiple tracks, different cars to choose from, and two game modes: Arcade and Competitive. In competitive mode, your car's performance degrades over time (tyre health), adding an extra layer of challenge. The game also includes a local leaderboard for each track, which saves and sorts the best lap times.

As this was a learning project, the code is not perfectly optimized and represents my initial approach to game development in Python. There is significant room for improvement and refactoring.

## Getting Started

### Prerequisites

To run this game, you will need to have Python and the Pygame library installed.

You can install Pygame using pip:
```bash
pip install pygame
```

### **IMPORTANT: Updating Image File Paths**

The image assets (cars, tracks, buttons, etc.) are loaded into the game using **absolute file paths**. This means the game will **not** run on your computer unless you update these paths to match the location of the files on your system.

1. Open the `new car.py` file in a text editor.
2. Near the top of the file (starting around line 23), you will find a block of code where all the images are loaded using `pygame.image.load()`. Here is an example:

   ```python
   # Storing all the images as variables 
   img = pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\speed_8252022_layout_14.jpg').convert()
   title = pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\title.png').convert()
   # ... and so on for all other images
   ```

3. For each `pygame.image.load()` line, you must change the file path (the string inside the parentheses) to the correct location of the image files on your computer.

   **Recommendation:** A good practice is to create a folder named `assets` or `images` in the same directory as the `new car.py` file, place all the images inside it, and then use relative paths. For example:

   ```python
   # Using relative paths (recommended)
   img = pygame.image.load('assets/speed_8252022_layout_14.jpg').convert()
   title = pygame.image.load('assets/title.png').convert()
   ```

### Running the Game

Once you have updated the file paths, you can run the game by executing the Python script from your terminal:

```bash
python "new car.py"
```

## How to Play

* **Navigation:** Use the mouse to click through the menus.
* **Controls:**
  * `W` - Accelerate Forward
  * `S` - Brake/Reverse
  * `A` - Turn Left
  * `D` - Turn Right
* **Objective:** Complete 3 laps as fast as possible. Your time will be recorded and displayed on the leaderboard for that track.

## Future Development & Potential Improvements

This project was a fantastic learning experience, but there are many areas that could be improved in future versions.

* **Code Optimization:** The main game loop is a large series of `if` statements. This could be refactored into a more efficient state machine pattern to handle different game states (e.g., `MainMenu`, `Playing`, `Paused`, `GameOver`).
* **Relative Paths:** As mentioned, hardcoding absolute file paths is not ideal. The code should be updated to use relative paths so it can run on any machine without modification.
* **Modularity:** The code could be broken down into multiple files. For instance, the `Car` and `Button` classes could each have their own Python file and be imported into the main script. This would make the project much easier to manage.
* **Game Logic Refactoring:** The `game()` function contains a lot of repeated code for each track and game mode. This could be consolidated into a more generic function that takes the track and mode as parameters.
* **Physics and Movement:** The car's movement and rotation logic could be made smoother and more realistic, perhaps by using vector-based physics instead of fixed angle rotations.
* **Gameplay Mechanics:** Introduce power-ups (like speed boosts or shields) and obstacles on the tracks in the arcade mode to make the gameplay more dynamic, similar to arcade racers like Mario Kart.
* **Multiplayer Functionality:** Implement multiplayer modes, including local split-screen and potentially an online mode for racing against other players.
* **Advanced Leaderboards:** Expand the leaderboard system to support online rankings in addition to the current local leaderboards.
