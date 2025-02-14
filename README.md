# Connect4 AI Game

A Connect Four game implemented in Python featuring several AI strategies. This project demonstrates different approaches to game playing, including:

- **Default Agent:** A heuristic-based strategy that searches for winning moves and blocks the opponent.
- **Minimax Agent:** Implements the minimax algorithm to select optimal moves.
- **Q-Learning Agent:** Uses reinforcement learning to improve gameplay decisions over time.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)

## Overview

This project is a modular implementation of a Connect Four game in Python. With separate modules for board management, game logic, and AI strategies, it serves as a practical example of:
  
- **Reinforcement Learning:** Demonstrated by the Q-learning agent.
- **Search Algorithms:** The minimax implementation showcases perfect-play scenarios.
- **Heuristic-based Play:** The default agent offers a balanced strategy by attempting winning moves and blocking opponents.

Whether you're interested in artificial intelligence or simply enjoy classic board games, this project is a great way to see AI strategies in action.

## Features

- **Interactive Game:** Run the game in the terminal to see AI agents compete.
- **Multiple AI Strategies:** Compare the performance and behavior of Q-learning, minimax, and default heuristic agents.
- **Customizable Options:** Modify game settings or extend agent functionalities to experiment further.
- **Educational:** Perfect for anyone looking to understand how various AI strategies can be implemented in games.

## Installation

Ensure you have [Python 3.x](https://www.python.org/downloads/) installed on your system. Then, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/Connect4.git
cd Connect4
```

## Usage

```bash
python main.py
```

## Project Structure

Connect4/
├── board.py       # Handles the board logic, move validation, and win checks.
├── default.py     # Implements the default player strategy.
├── game.py        # Contains the game loop and overall match management.
├── main.py        # Entry point of the application; starts the game.
├── minimax.py     # Implements the minimax algorithm for decision making.
├── players.py     # Common player utilities and abstract classes.
├── qlearning.py   # Contains the Q-learning agent logic.
└── .gitignore     # Lists files and directories to be ignored by Git.

