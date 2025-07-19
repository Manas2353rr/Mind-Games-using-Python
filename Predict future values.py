import numpy
import matplotlib.pyplot as plt

x=[5,10,15,20,30,40,50,60,70,80,90,100]
y=[2,8,12,30,45,40,30,25,20,10,5,5]

model=numpy.poly1d(numpy.polyfit(x,y,3))
line=numpy.linspace(5,100,100)

plt.scatter(x,y,color='g')
plt.plot(line,model(line),color='r')
plt.show()
