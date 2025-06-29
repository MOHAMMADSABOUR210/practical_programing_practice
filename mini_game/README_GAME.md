# Terminal Mini Game

This is a terminal-based mini game written in Python using the `curses` library. The player navigates through a world filled with obstacles, food, and enemies.

## How to Play

- The player is represented by `x`.
- Move using **WASD** keys:
  - `W`: up
  - `A`: left
  - `S`: down
  - `D`: right
- Collect food marked as `*` to gain points.
- Avoid enemies marked as `E` — if they catch you, the game ends.
- Press `Q` at any time to quit.

## Features

- Randomly generated world and food/enemy placement
- Countdown timer for each food item (they respawn when expired)
- Enemies randomly move toward the player
- Auto-wrapping screen edges (player reappears on opposite side)
- Displays score on screen

## Requirements

- Python 3.x
- `curses` library (built-in on Linux/macOS; use `windows-curses` on Windows)

## Run the Game

On Linux/macOS:

```bash
python3 mini_game.py
```

On Windows (after installing curses support):

```bash
pip install windows-curses
python mini_game.py
```

## Notes

- This game is designed for terminal environments.
- Make sure your terminal is large enough for a comfortable experience.
- The game uses non-blocking key input for smooth control.

## License

This project is for educational and personal use.