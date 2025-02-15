# CDS524-Assignment-1---based-on-Reinforcement-Learning-Game-Design-where-Jie-Ge-searches-for-Ah-Wei

# README

Author：Zhiyi Hong

YouTube Link: 

Background Video link: https://www.youtube.com/watch?v=q2l-E91v7Rk

# The game rules: 

In this game, the goal of the intelligent agent (Jie Ge) is to discover the shortest path from the starting point (Jie Ge's initial position) to the ending point (Ah Wei's position) while avoiding collision with obstacles. 

![image](https://github.com/user-attachments/assets/d90979f5-4519-4ce7-8a77-42fa8d211408)

After reinforcement learning training, Jie Ge found the shortest path.The final shortest path:

![image](https://github.com/user-attachments/assets/6d5b669a-edaa-4828-ba46-6e98b88ab954)

At the end, the system will pop up a prompt::

![image](https://github.com/user-attachments/assets/f3b602a1-78e1-4fec-aee9-6f9a7b300086)

When the agent touches the pink grid or reaches the finish line(Ah Wei’s position), it will reset the game to the next round. In the game, the agent will conduct 2250 rounds.

# Game environment: 

The maze is composed of a two-dimensional grid, which includes passable positions (white grid), obstacles (pink grid), starting point (Jie Ge's initial position), and ending point (Ah Wei's position).

The agent can choose four directions to move: Up, Down, Left, and Right.

The current position of the intelligent agent is represented by row and column coordinates.

## Run main.exe to start the game

# Reward function :

The reward mechanism is as follows:

Reaching the finish line (Ah Wei's position): Reward+100.

Encountering obstacles: Punishment -100.

Each move: Punish -1 (encourages quick path finding).

The goal of agent is to learn how to make optimal actions through interaction with the environment, in order to maximize future cumulative rewards.


# Q-Learning and the ε-growth strategy

When selecting actions, algorithms have a certain probability (ε) to choose a random action (exploration) in order to discover new combinations of states and actions.

On the other hand, using probability (1- ε) to select the currently known optimal action (utilization), that is, selecting the action corresponding to the maximum Q value of the current state from the Q table.


# Tools Overview

1. **Python**

2. **QLearning**

3. **Tkinter**

4. **Maze**


# Evaluation results

When the episodes reach 117 times, the agent found the path to the destination for the first time.

In the following rounds, the agent will find the path faster and faster.

When the episodes reach 2232 times, the agent can stably find the target endpoint position through the shortest path.

