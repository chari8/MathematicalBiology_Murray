import os, sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns #not used

def main(step_number, lamb, a, m, T, g, init):
    print("step_number:%d, lamb:%f, a:%d, m:%d, T:%d, g:%d\n" % (step_number, lamb, a, m, T, g))
    c = np.zeros(step_number + 10) 

    for i in range(T):
        c[i] = init[i]

    for t in range(step_number):
        if(t >= T-1):
            dev = (lamb * a**m * c[t-T+1]) / (a**m + c[t-T+1]**m) - g*c[t]
            c[t+1] = dev + c[t]
    return c[:step_number]


def plot_series(dataset):

    set_num = len(dataset)
    
    for i in range(set_num):
        data = dataset[i][0]
        T = dataset[i][1]

        plt.subplot(set_num,2, i*2 + 1)
        plt.plot(range(data.size), data)
        plt.title("c(t)-t")
        plt.xlabel("day")
        plt.ylabel("c(t)/a")

        plt.subplot(set_num, 2, i*2 + 2)
        plt.plot(data[T:], data[:(data.size - T)])
        plt.title("c(t-T)-c(t)")
        plt.xlabel("c(t)/a")
        plt.ylabel("c(t-T)/a")

    plt.tight_layout()
    plt.show()

def plot_multi(dataset):

    set_num = len(dataset)
    hight = int(np.ceil(np.sqrt(set_num)))
    width = int(np.ceil(np.sqrt(set_num)))
    
    cnt = 0
    for i in range(set_num):
        data = dataset[i][0]
        T = dataset[i][1]
        plt.subplot(hight, width,i+1)
        plt.plot(data[T:], data[:(data.size - T)])

    plt.tight_layout()
    plt.show()


def plot_by_c(data, T):
    x = data[T:]
    y = data[:(data.size - T)] 

    plt.xlabel("c(t)/a")
    plt.ylabel("c(t-T)/a")
    plt.plot(x, y)
    plt.show()


def plot_by_time(data):
    x = range(data.size)
    y = data

    plt.xlabel("day")
    plt.ylabel("c(t)/a")
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    ##### params #####
    step_number = 1500
    lamb = 0.2
    a = 1.0
    m = 10
    T = 2
    g = 0.1

    init = [a*np.random.rand() for i in range(1000)]
#init = np.linspace(0.15, 1.15, 100)
#init = [0.5, 0.8]

#dataset = [ [main(step_number, lamb, a, float(m), 6, g, init[:6]), 6, m], [main(step_number, lamb, a, float(m), 20, g, init[:20]), 20, m]] 
    dataset = [ [main(step_number, lamb, a, float(m), T, g, init[:T]), T, m]  for T in range(1, 50, 5)] 
#dataset = [ [main(step_number, lamb, a, float(m), T, g, init[:T]), T]] 

    for data in dataset:
        print(np.array_equal(dataset[0][0], data[0]))

#plot_series(dataset)
    plot_multi(dataset)
