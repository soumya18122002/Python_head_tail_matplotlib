from turtle import color
import matplotlib.pyplot as plt
import random

head_tail = [0,0]
for x in range(100000):
    if x % 50 ==0:
        head_tail[random.randint(0,1)] +=1
        plt.bar([0,1],head_tail,color=("blue","red"))
        plt.pause(0.0001)

plt.show()