from enum import Enum
import numpy as np

class CoinState(Enum):
    Head = 1
    Tail = 0

class Game():
    def __init__(self,id, head_prob):
        self._id = id
        self._head_prob = head_prob
        self._rnd = np.random
        self._rnd.seed(id)

        self._coinstate = CoinState.Tail
        self._wintimes = 0
        self._reward = 0


    def simulate(self, n_time_steps):
        n = 0
        while n+1 < n_time_steps:
            if self._rnd.sample() < self._head_prob:
               self._coinstate = CoinState.Head
               self._wintimes +=1
               n += 3
            n += 1

    def get_reward(self):
        self._reward =  - 250 + self._wintimes *100
        return self._reward

class Cohort():
    def __init__(self, id, size, head_prob):
        self._id = id
        self._size = size
        self._head_prob =head_prob
        self._players = []
        self._rewards = []

        for i in range(size):
            player = Game(id * size + i, head_prob)
            self._players.append(player)

    def simulate(self, n_times_steps):
        for player in self._players:
            player.simulate(n_times_steps)
            value = player.get_reward()
            self._rewards.append(value)

    def get_ave_reward(self):
        return sum(self._rewards)/len(self._rewards)


Trail1 = Cohort(id=1, size =1000, head_prob=0.4)
Trail1.simulate(n_times_steps=19)
print(Trail1.get_ave_reward())
