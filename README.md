# Memory Card Game

A classic memory matching game implemented in Python using Tkinter. Players need to find matching pairs of letters by flipping cards and remembering their positions.

## Features

- 4x4 grid of cards (8 pairs of letters)
- Move counter to track player performance
- Pairs found counter
- Clean and intuitive user interface
- Automatic card hiding for non-matching pairs
- Win detection with move count display

## How to Play

1. Launch the game using the installation instructions above
2. The game presents a 4x4 grid of face-down cards
3. Click on any card to reveal its letter
4. Click on a second card to find its match
5. If the cards match:
   - They remain face up
   - Your "Pairs Found" counter increases
6. If the cards don't match:
   - They automatically flip face down after 1 second
   - Try to remember their positions for future moves
7. Game continues until all pairs are found
8. Upon completion, the game displays your total moves

## Game Logic

The game implements the following key features:

- **Card Representation**: Letters A-H are used, with each letter appearing exactly twice
- **Random Distribution**: Cards are shuffled at the start of each game
- **Move Validation**: Prevents clicking already revealed cards
- **Match Detection**: Automatically checks if two revealed cards match
- **Game State Tracking**: Monitors moves made and pairs found
- **Win Condition**: Game ends when all 8 pairs are found

## GUI Layout

- Main game grid (4x4)
- Information panel showing:
  - Number of moves made
  - Number of pairs found
- Pop-up message for game completion
