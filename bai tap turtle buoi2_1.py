from turtle import *
for n in range(6,2,-1):
    for i in range(n):
        if n == 4 or n == 6:
            pencolor("red")

        else:
            pencolor("navy")

        forward(100)
        left(360/n)



mainloop()