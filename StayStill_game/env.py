import numpy as np
import gym
from gym import spaces

class StayStillEnv(gym.Env):
    def __init__(self):
        super(StayStillEnv, self).__init__()
        self.grid_size = 11
        self.action_space = spaces.Discrete(5)  # [stay, up, down, left, right]
        self.observation_space = spaces.Box(low=0, high=10, shape=(2,), dtype=np.int32)
        self.reset()

    def reset(self):
        self.agent_pos = np.array([5, 5])  # start at center
        return self.agent_pos

    def step(self, action):
        x, y = self.agent_pos

        # Move based on action
        if action == 1 and y > 0:      # up
            y -= 1
        elif action == 2 and y < 10:   # down
            y += 1
        elif action == 3 and x > 0:    # left
            x -= 1
        elif action == 4 and x < 10:   # right
            x += 1
        # action == 0 means stay still

        self.agent_pos = np.array([x, y])
        reward = self.calculate_reward(action)

        done = False  # can define a done condition if needed
        return self.agent_pos, reward, done, {}

    def calculate_reward(self, action):
        x, y = self.agent_pos
        # Preferred zone: center 3x3
        if 4 <= x <= 6 and 4 <= y <= 6:
            if action == 0:
                return 1.0  # reward for staying still
            else:
                return -0.1  # small penalty for moving

        # Medium penalty zone: between outer and inner square
        elif 2 <= x <= 9 and 2 <= y <= 9:
            return -1.0

        # Outside penalty zone
        else:
            return -10.0

    def render(self, mode="human"):
        grid = np.full((11, 11), '.', dtype=str)
        x, y = self.agent_pos
        grid[y][x] = 'A'
        print("\n".join([" ".join(row) for row in grid]))
        print()
