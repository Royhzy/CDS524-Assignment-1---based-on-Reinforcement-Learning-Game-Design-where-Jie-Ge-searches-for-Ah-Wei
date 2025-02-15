from tkinter import messagebox

from maze_env import Maze
from RL_brain import QLearningTable
import time


def update():
    for episode in range(2250):
        # initial observation
        observation = env.reset()  #observation is Awei's coordinate
        R = 0  # Record the rewards for each round
        while True:
            # update environment
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_
            # Slow down after 2240(stable catch success reward=75) episodes
            if episode >2240:
                time.sleep(0.3)
            R = R + reward  # Accumulate the rewards of each action
            print("episode", episode)
            print("rewards", R)  # show each round rewards
            #if R == 75:
            #    print("final episode",episode)
            #    messagebox.showinfo("success", "jiege catch")
            # break while loop when end of this episode
            if done:
                break


    # end of game
    print('game over')
    messagebox.showinfo("game over", "Jie, please don't!!!")
    env.destroy()

if __name__ == "__main__":
    env = Maze()

    RL = QLearningTable(actions=list(range(env.n_actions)))  #env.n_actions is the number of operations that can be performed, 4 operations including the top, bottom, left, and right directions

    env.after(100, update)
    env.mainloop()