import serial
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation 

X=[]
Y=[]
Z=[]
arduinoData = serial.Serial('com5', 2000000)
i=0

 

#while True: 
while (i<60):# While loop that loops forever
   # while (arduinoData.inWaiting()==0): #Wait here until there is data
       # pass #do nothing
    
    arduinoString = arduinoData.readline() #read the line of text from the serial port
    dataArray = arduinoString.split('a')   #Split it into an array called dataArray
    xs = float( dataArray[0])            #Convert first element to floating number and put in temp
    ys = float( dataArray[1]) 
    zs = float( dataArray[2])  
    X.append(xs)                    #Build our tempF array by appending temp readings
    Y.append(ys)   
    Z.append(zs)
    print xs,',',ys,',',zs
    i=i+1
    print i
    
            
fig=plt.figure()
ax = fig.add_axes([0, 0, 1, 1], projection='3d') 
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_xlim3d([0.0, 200])

ax.set_ylim3d([0.0, 200]) 

ax.set_zlim3d([0.0, 200]) 

plt.autoscale(enable=False) 
ax.set_title('3D Trilatration/3D Canvas') 
lines = ax.plot(X,Y,Z,'-',c='r') #
    


def animate(i): 
            for line, xi, yi, zi in zip(lines,X,Y,Z): 
                        line.set_data(X[0:i+1],Y[0:i+1]) 
                        line.set_3d_properties(Z[0:i+1])
                        fig.canvas.draw() 
                        return lines
            
anim=FuncAnimation(fig,animate,frames=60, interval=60, blit=True)
fig.show()   