#This script is the environment part of this example.
#Pink grid:hell
#Jiege:Agent
#Awei:Object location

import numpy as np
import time
import sys
from PIL import Image, ImageTk
from tkinter import messagebox
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk


UNIT = 40   # grid's width and height
MAZE_H = 8  # the numbers of grids height
MAZE_W = 8  # the numbers of grids width


class Maze(tk.Tk, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.title('maze')
        self.path = []
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_H * UNIT))
        self._build_maze()

    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='white',
                           height=MAZE_H * UNIT,
                           width=MAZE_W * UNIT)

        # create grids
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 =c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT , r
            self.canvas.create_line(x0, y0, x1, y1)

        # create origin
        origin = np.array([20, 20])

        # hell
        hell1_center = origin + np.array([UNIT *2, UNIT])
        self.hell1 = self.canvas.create_rectangle(
            hell1_center[0] - 20, hell1_center[1] - 20,
            hell1_center[0] + 20, hell1_center[1] + 20,
            fill='pink')
        # hell
        hell2_center = origin + np.array([UNIT, UNIT * 2])
        self.hell2 = self.canvas.create_rectangle(
            hell2_center[0] - 20, hell2_center[1] - 20,
            hell2_center[0] + 20, hell2_center[1] + 20,
            fill='pink')
        # hell
        hell3_center = origin + np.array([UNIT, UNIT * 3 ])
        self.hell3 = self.canvas.create_rectangle(
            hell3_center[0] - 20, hell3_center[1] - 20,
            hell3_center[0] + 20, hell3_center[1] + 20,
            fill='pink')
        # hell
        hell4_center = origin + np.array([UNIT * 3, UNIT * 2])
        self.hell4 = self.canvas.create_rectangle(
            hell4_center[0] - 20, hell4_center[1] - 20,
            hell4_center[0] + 20, hell4_center[1] + 20,
            fill='pink')
        # hell
        hell5_center = origin + np.array([UNIT * 4, UNIT * 2])
        self.hell5 = self.canvas.create_rectangle(
            hell5_center[0] - 20, hell5_center[1] - 20,
            hell5_center[0] + 20, hell5_center[1] + 20,
            fill='pink')
        # hell
        hell6_center = origin + np.array([UNIT * 1, UNIT * 4])
        self.hell6 = self.canvas.create_rectangle(
            hell6_center[0] - 20, hell6_center[1] - 20,
            hell6_center[0] + 20, hell6_center[1] + 20,
            fill='pink')
        # hell
        hell7_center = origin + np.array([UNIT * 4, 0])
        self.hell7 = self.canvas.create_rectangle(
            hell7_center[0] - 20, hell7_center[1] - 20,
            hell7_center[0] + 20, hell7_center[1] + 20,
            fill='pink')
        # hell
        hell8_center = origin + np.array([UNIT * 6, UNIT])
        self.hell8 = self.canvas.create_rectangle(
            hell8_center[0] - 20, hell8_center[1] - 20,
            hell8_center[0] + 20, hell8_center[1] + 20,
            fill='pink')
        # hell
        hell9_center = origin + np.array([UNIT * 4, UNIT * 6])
        self.hell9 = self.canvas.create_rectangle(
            hell9_center[0] - 20, hell9_center[1] - 20,
            hell9_center[0] + 20, hell9_center[1] + 20,
            fill='pink')
        # hell
        hell10_center = origin + np.array([UNIT * 0, UNIT * 7])
        self.hell10 = self.canvas.create_rectangle(
            hell10_center[0] - 20, hell10_center[1] - 20,
            hell10_center[0] + 20, hell10_center[1] + 20,
            fill='pink')
        # hell
        hell12_center = origin + np.array([UNIT * 2, UNIT * 5])
        self.hell12 = self.canvas.create_rectangle(
            hell12_center[0] - 20, hell12_center[1] - 20,
            hell12_center[0] + 20, hell12_center[1] + 20,
            fill='pink')
        # hell
        hell13_center = origin + np.array([UNIT * 6, UNIT * 3])
        self.hell13 = self.canvas.create_rectangle(
            hell13_center[0] - 20, hell13_center[1] - 20,
            hell13_center[0] + 20, hell13_center[1] + 20,
            fill='pink')
        # hell
        hell15_center = origin + np.array([UNIT * 6, UNIT * 4])
        self.hell15 = self.canvas.create_rectangle(
            hell15_center[0] - 20, hell15_center[1] - 20,
            hell15_center[0] + 20, hell15_center[1] + 20,
            fill='pink')
        # hell
        hell16_center = origin + np.array([UNIT * 5, UNIT * 1])
        self.hell16 = self.canvas.create_rectangle(
            hell16_center[0] - 20, hell16_center[1] - 20,
            hell16_center[0] + 20, hell16_center[1] + 20,
            fill='pink')
        # hell
        hell17_center = origin + np.array([UNIT * 3, UNIT * 6])
        self.hell17 = self.canvas.create_rectangle(
            hell17_center[0] - 20, hell17_center[1] - 20,
            hell17_center[0] + 20, hell17_center[1] + 20,
            fill='pink')
        # hell
        hell18_center = origin + np.array([UNIT * 5, UNIT * 5])
        self.hell18 = self.canvas.create_rectangle(
            hell18_center[0] - 20, hell18_center[1] - 20,
            hell18_center[0] + 20, hell18_center[1] + 20,
            fill='pink')

        # create oval
        oval_center = origin + UNIT * 2

        # load Awei's image
        image_path2 = "D:\pythonProject\Qlearning project Hong\wei.jpg"
        image2 = Image.open(image_path2)
        image2 = image2.resize((40, 40), Image.LANCZOS)  # resize image
        self.photo2 = ImageTk.PhotoImage(image2)
        #use image
        self.oval=self.canvas.create_image(oval_center[0], oval_center[1], image=self.photo2, anchor=tk.CENTER)


        # load Jiege's image
        image_path = "D:\pythonProject\Qlearning project Hong\jiege.png"
        image = Image.open(image_path)
        image = image.resize((40, 40), Image.LANCZOS)  # resize image
        self.photo = ImageTk.PhotoImage(image)
        #use image
        self.image = self.canvas.create_image(origin[0], origin[1], image=self.photo, anchor=tk.CENTER)

        # pack all
        self.canvas.pack()

    def reset(self):
        self.update()
      #  time.sleep(0.5)
        self.canvas.delete(self.image)
        origin = np.array([20, 20])

        # load Jiege's image
        image_path = "D:\pythonProject\Qlearning project Hong\jiege.png"
        image = Image.open(image_path)
        image = image.resize((40, 40), Image.LANCZOS)  # resize image
        self.photo = ImageTk.PhotoImage(image)
        #use image
        self.image =self.canvas.create_image(origin[0], origin[1], image=self.photo, anchor=tk.CENTER)

        self.path = [self.canvas.coords(self.image)]  # reset path

        # return observation
        return self.canvas.coords(self.image)

    def step(self, action):
        s = self.canvas.coords(self.image)
        base_action = np.array([0, 0])
        if action == 0:   # up
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:   # right
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:   # left
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.image, base_action[0], base_action[1])  # move agent

        s_ = self.canvas.coords(self.image)  # next state
        #print("s_",s_)
        #print("self.oval", self.canvas.coords(self.oval))
        #print("self.canvas.coords(self.hell1)",self.canvas.coords(self.hell1))

        self.path.append(s_)

        # reward function
        if s_ == self.canvas.coords(self.oval):
            reward = 100
            #messagebox.showinfo("catch", "jiege catch")
            done = True
            s_ = 'terminal'
        # into pink grid
        elif s_ in [[100.0,60.0],  #self.canvas.coords(self.hell1)
                    [180.0, 20.0],
                    [220.0, 60.0],
                    [260.0, 60.0],
                    [60.0, 100.0],
                    [60.0, 140.0],
                    [60.0, 180.0],
                    [140.0, 100.0],
                    [180.0, 100.0],
                    [100.0, 220.0],
                    [20.0, 300.0],
                    [140.0, 260.0],
                    [180.0, 260.0],
                    [220.0, 220.0],
                    [260.0, 180.0],
                    [260.0, 140.0],
                    ]:
            reward = -100   # reward
            done = True
            s_ = 'terminal'
        else:
            reward = -1
            done = False

        return s_, reward, done

    def render(self):
        self.canvas.delete("path_line")
        for i in range(len(self.path) - 1):
            self.canvas.create_line(self.path[i][0], self.path[i][1], self.path[i + 1][0], self.path[i + 1][1],fill='red',tags="path_line")
        # time.sleep(0.1)
        self.update()


def update():
    for t in range(10):
        s = env.reset()
        while True:
            env.render()
            a = 1
            s, r, done = env.step(a)
            if done:
                break

if __name__ == '__main__':
    env = Maze()
    env.after(100, update)
    env.mainloop()
    