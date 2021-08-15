import numpy as np
import matplotlib.pyplot as plt



class numphyExamples():
    def __init__(self) -> None:
        super().__init__()


    def four(self):
        arr = np.arange(10)
        print(arr)
        sol = arr[1::2]
        sol2 = arr[arr%2==1]
        print(sol)
        print(sol2)

    def five(self):
        arr = np.arange(10)
        print(arr)
        arr[arr%2==1]= -1
        print(arr)
        out = np.where(arr%2==1,-1,arr)
        print(out)

    def six(self):
        arr = np.arange(10)
        print(arr)
        out = arr.reshape(5,-1)
        print(out)

    def eight(self):
        a = np.arange(3)
        b = np.repeat(1, 10).reshape(2, -1)
        print(a)
        print(b)
        print("-----")
        print(np.repeat(a,3))
        print(np.tile(a,3))
        out = np.r_[np.repeat(a,3),np.tile(a,3)]
        print(out)

    def thirteen(self):
        a = np.array([5, 7, 9, 8, 6, 4, 5])
        b = np.array([6, 3, 4, 8, 9, 7, 1])

        out =np.where(a>b,a,b)
        print(out)

    def function(self):
        a= np.arange(60).reshape(6,5,2)
        print(a)
        b= a.transpose()
        print(b)
        c = a.transpose((1,0,2))
        print(c)
        d= np.where(a>8,0,a)
        print(d)

    def plot(self):
        x = np.arange(-5,5,0.1)
        y = np.arange(-5, 5, 0.1)
        xx , yy = np.meshgrid(x,y,sparse=True)
        z= np.sin(xx**2+yy*2)/ (xx*2 +yy*2)
        plt.contourf(x,y,z)
       # plt.show()
