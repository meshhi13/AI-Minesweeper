
# Minesweeper AI

This is a Python implementation of the classic Minesweeper game with an AI assistant to help you play. The game is built using the `pygame` library.

## Requirements

Before running the game, ensure you have the following installed:

- Python 3.8 or higher
- `pygame` library

To install `pygame`, run:
```bash
pip install pygame
```

## How to Run

1. Clone or download this repository to your local machine.
2. Navigate to the project directory.
3. Run the game using the following command:
```bash
python main.py
```

## How to Play

1. **Objective**: The goal is to reveal all tiles that do not contain mines. Flag all the mines to win the game.
2. **Controls**:
   - **Left Click**: Reveal a tile.
   - **Right Click**: Flag or unflag a tile.
   - **AI Move Button**: Click the "AI MOVE" button to let the AI assist you in making a move.
   - **Restart**: If the game ends, click the "RESTART" button to start a new game.
3. **Game Over**:
   - If you reveal a mine, you lose.
   - If all non-mine tiles are revealed and all mines are flagged, you win.

## Features

- **AI Assistance**: The AI can analyze the board and make moves or flag tiles based on clues.
- **Dynamic Board**: The board size and number of mines can be customized.
- **Visual Feedback**: The game provides visual cues for flagged tiles, revealed tiles, and game status.

Enjoy playing Minesweeper with AI assistance!
