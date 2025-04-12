# Collect & Avoid Game (RL - DQN)

## Overview

The **Collect & Avoid** game is a grid-based reinforcement learning environment where the agent must collect rewards while avoiding enemies. The agent can move in a n x n grid (15 x 15 as default) and must avoid enemies that chase it. The game ends if the agent collides with an enemy. The goal of the agent is to collect as many rewards as possible while staying alive.

## Environment

This environment is a subclass of `gym.Env` and follows the OpenAI Gym API. The grid consists of:
- **Agent:** It can move one step in any of four directions.
- **Rewards:** The agent collects these rewards by moving to their location. They are placed randomly on the grid and they have fixed positions until the episode ends. 
- **Enemies:** They chase the agent to bust it (50% chance of random movement at each step). The game ends when an enemy collides with the agent.

The agent interacts with the environment by taking actions, which are determined by a reinforcement learning algorithm.

## State Space

The state space is represented by a **flattened 2D grid** (15x15 by default), where each cell corresponds to a position on the grid.

- **Shape:** The state is a 1D vector of size `grid_size * grid_size` (e.g., 225 for a 15x15 grid).
- **Values:**
  - `1`: Represents the agent's position.
  - `2`: Represents reward positions.
  - `3`: Represents enemy positions.
  - `0`: Represents empty cells.

### Example of State (Flattened):
[0, 0, 0, ..., 0, 1, 0, ..., 0, 2, 0, ..., 3, 3, 0, ...]


## Action Space

The action space is **discrete** with 5 possible actions:

- `0`: Stay (do nothing)
- `1`: Move Up
- `2`: Move Down
- `3`: Move Left
- `4`: Move Right

## UI (User Interface)

The environment includes a **real-time graphical user interface** (GUI) to visualize the agent's actions and the game's state:

- **Grid:** The agent, rewards, and enemies are visualized on a 15x15 grid.
- **Text Information:** The top of the grid shows the current episode, step, and the current reward collected by the agent.
- **Agent: Blue Circle**
- **Rewards: Green Circles**
- **Enemies: Red Circles**


## Usage

1. Have torch installed then; Install other dependencies:
   ```bash
   pip install gym matplotlib numpy
   ```








