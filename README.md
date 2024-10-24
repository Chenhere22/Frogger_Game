![image](https://github.com/user-attachments/assets/ae1c905e-57f3-4a47-8b70-bf8bce004f90)


# Frogger Game

## Overview
The Frogger Game project is a Python-based recreation of the classic arcade game "Frogger." It leverages Python's `turtle` graphics library to create an interactive and engaging game where players control a frog character that must cross busy roads and treacherous rivers to reach safe zones, known as homes. Players must avoid cars, manage obstacles on the river, and safely navigate their frog to one of the homes at the top of the screen. The game aims to replicate the nostalgic experience of the original Frogger while providing a simple yet challenging gameplay.

## Features
The Frogger Game comes with a range of features that enhance gameplay and challenge players to think strategically:

- **Player Control**: Players can move the frog character up, down, left, or right using the arrow keys on the keyboard. This allows precise control of the frog’s movements as it navigates the game environment.

- **Obstacle Management**: Players must navigate a variety of moving obstacles. These include:
  - **Cars**: Cars move horizontally across the screen, posing a danger to the frog when crossing roads.
  - **Logs**: Logs float across the river, allowing the frog to hitch a ride to avoid falling into the water.
  - **Turtles**: Turtles also help the frog cross the river, but they occasionally submerge, adding to the challenge.

- **Collision Detection**: The game has built-in collision detection that identifies when the frog comes into contact with cars or other obstacles. A collision results in the player losing one of their lives.

- **Game Mechanics**: The player’s objective is to guide the frog to one of the homes without losing all lives. The game is designed to be challenging with limited lives, meaning careful timing and strategy are needed to succeed.

## Installation
To play the Frogger Game, follow these instructions to set up and run the game on your local machine.

### Prerequisites
To successfully run the Frogger Game, you need the following:
- **Python 3.x**: Make sure you have Python 3 installed. You can download it from [Python's official website](https://www.python.org/downloads/).
- **Turtle Graphics Library**: The turtle library is part of Python’s standard library, so it comes pre-installed with Python.

### Setup Instructions
1. **Clone the Repository**:
   Begin by cloning the repository to your local machine using the following command:
   ```sh
   git clone <repository_url>
   ```
2. **Configure Image Paths**:
   Ensure that all the image paths used in the code are accurate. You may need to adjust the paths to point to the correct directory where the images are stored. The images required include:
   - `frogger.gif` (frog sprite)
   - `car_left.gif` (car facing left)
   - `car_right.gif` (car facing right)
   - `log.gif` (log used to cross the river)
   - `turtles_right.gif` (turtles used to cross the river, moving right), etc.

   These image files must be placed in the correct folder so that the game can load them properly.

## Running the Game
Once the setup is complete, you can run the game by executing the following command in your terminal or command prompt:
```sh
python Frogger.py
```
Make sure that all the required image files are accessible in the specified paths, as they are necessary for rendering the graphics during gameplay.

## Controls
- **Arrow Keys**: Use the arrow keys on your keyboard to move the frog:
  - **Up Arrow**: Move the frog up.
  - **Down Arrow**: Move the frog down.
  - **Left Arrow**: Move the frog left.
  - **Right Arrow**: Move the frog right.

## File Structure
The game project consists of the following files:
- **`Frogger.py`**: This is the main script that contains the entire game logic, including player movement, obstacle management, collision detection, and rendering of game elements.
- **Image Files**: A set of image files (e.g., `frogger.gif`, `car_left.gif`, etc.) that are essential for the visual representation of game characters and obstacles.

## Gameplay Mechanics
The gameplay mechanics of the Frogger Game are inspired by the original arcade version, with several distinct elements:

- **Starting Point**: The frog starts at the bottom of the screen and must reach one of the homes located at the top of the screen.
- **Road and River Crossing**: The player needs to cross a road filled with moving cars and a river filled with floating logs and turtles.
  - **Cars**: Cars move at varying speeds across the road. Players must avoid colliding with these vehicles to stay alive.
  - **Logs and Turtles**: Logs and turtles move across the river, providing a way for the player to cross. Players need to jump onto these objects, but beware—turtles occasionally submerge, which can cause the player to fall into the river.
- **Lives**: The player starts with a limited number of lives. Each collision with an obstacle or fall into the water reduces the player's lives. If all lives are lost, the game ends.

## Additional Notes
- **Timer**: The game includes a timer that counts down. The player must successfully reach one of the homes before time runs out. Failing to do so will result in losing a life.
- **Dynamic Obstacles**: Logs and turtles move at different speeds and in different directions, making it challenging for players to plan their moves accurately.

## License
This project is open-source and distributed under the [MIT License](LICENSE). You are free to use, modify, and distribute the game as per the terms of the MIT License.

## Credits
This game was developed by Li, inspired by the classic "Frogger" arcade game concept.

Acknowledgements: This project was developed with hints and inspiration from the work of TokyoEdtech, whose tutorials were instrumental in understanding some of the mechanics used in the game.
