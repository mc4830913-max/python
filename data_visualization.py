import numpy as np
import time
import matplotlib.pyplot as plt

##  1 basic line graph
x=np.linspace(1,20,100)
y=np.cos(x)
plt.plot(x,y)
plt.show()
plt.xlabel("s_axis")
plt.ylabel("y_axis")
plt.title("basic line plot")

##custom line graph
x=np.linspace(1,20,100)
y=np.sin(x)
plt.plot(x,y,"o",linestyle=":",color="red",markersize=5,alpha=0.5)
plt.xlabel("s_axis")
plt.ylabel("y_axis")
plt.title("custom line plot ")
plt.show()

##line plot with multiple lines
x=np.linspace(1,10,50)
y1=np.sin(x)
y2=np.cos(x)
plt.plot(x,y1,"o",linestyle=":",color="red",markersize=5,alpha=0.5,label="sin(x)")
plt.plot(x,y2,"o",linestyle=":",color="green",markersize=5,alpha=0.5,label="cos(x)")
plt.xlabel("s_axis")
plt.ylabel("y_axis")
plt.title("line plot with multiple line ")
plt.legend()
plt.show()

### 2 scatter plot basic 
x=np.random.rand(100)
y=np.random.rand(100)
plt.scatter(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("basic scatter plot")
plt.show()

#customizes scatter plot 
x=np.random.rand(300)
y=np.random.rand(300)
z=np.random.rand(300)
plt.scatter(x,y,marker="o",alpha=0.7,c=z,cmap='viridis')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("basic scatter plot")
plt.colorbar()
plt.show()

##scatter plot with multiple class
x1=np.random.rand(250)-0.5
y1=np.random.rand(250)-1
x2=np.random.rand(250)+0.5
y2=np.random.rand(250)
x3=np.random.rand(250)-0.5
y3=np.random.rand(250)
x4=np.random.rand(250)+0.5
y4=np.random.rand(250)-1
plt.scatter(x1,y1,marker="o",alpha=0.7)
plt.scatter(x2,y2,marker="o",alpha=0.7)
plt.scatter(x3,y3,marker="o",alpha=0.7)
plt.scatter(x4,y4,marker="o",alpha=0.7)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("basic scatter plot")
# plt.colorbar()
plt.show()


## hexbining scatter plot
x=np.random.rand(1000)
y=np.random.rand(1000)
plt.hexbin(x,y,gridsize=20)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("hexbin scatter plot")
plt.colorbar()
plt.show()

## 3 basic bar graph 
x=np.array(["A","B","C","D","E"])
y=np.array([10,20,30,40,50])
plt.bar(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("bar graph")
plt.show()

##stacked bar graph
x=np.random.rand(10,5)
plt.bar(np.arange(10),x[:,0]+x[:,1]+x[:,2]+x[:,3]+x[:,4],label="d-5")
plt.bar(np.arange(10),x[:,0]+x[:,1]+x[:,2]+x[:,3],label="d-4")
plt.bar(np.arange(10),x[:,0]+x[:,1]+x[:,2],label="d-3")
plt.bar(np.arange(10),x[:,0]+x[:,1],label="d-2")
plt.bar(np.arange(10),x[:,0],label="d-1")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("stacked bar graph")
plt.legend()
plt.show()


##grouped bar graph
data=np.array([[10,20,30],[40,50,60],[70,80,90]])
x=np.arange(3)
width=0.25
plt.bar(x-width, data[:,0], width, label="D-1")
plt.bar(x, data[:,1], width, label="D-2")
plt.bar(x+width, data[:,2], width, label="D-3")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("grouped bar graph")
plt.legend()
plt.show()

## 4 basic histogram
data=np.random.randn(1000000)
plt.hist(data,bins=1000)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("basic histogram")
plt.show()

##cumultative histogram
data=np.random.randn(1000)
plt.hist(data,bins=10,cumulative=True)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("cumulative histohram")
plt.show()

#histogram with multiple valuse 
data1=np.random.randn(10000)
data2=np.random.randn(10000)+3
data3=np.random.randn(10000)+6
plt.hist(data1,bins=30,alpha=.9,label="D-1")
plt.hist(data2,bins=30,alpha=.7,label="D-2")
plt.hist(data3,bins=30,alpha=.7,label="D-3")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("histogram with multiple datdset")
plt.legend()
plt.show()


### 5 box plot 
data1=np.random.randn(100,5)
plt.boxplot(data1,label=["d1","d2","d3","d4","d5"],vert=False)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("box plot")
plt.legend()
plt.show()


## 6 heatmap
data=np.random.randn(10,10)
plt.imshow(data)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("heat map")
plt.colorbar()
plt.show()


#### 7 pie chat
label=['python','java','c++',"c language","javascript"]
sizes=[21.3,14.7,7.7,8.9,13.5]
explode=(0,0,0,0,0.1)
color=["lightpink", "lightcoral", "yellowgreen", "olive", "lightskyblue",]

plt.title("programming languges")
plt.pie(sizes,colors=color,labels=label,autopct='%1.1f%%',shadow=True,explode=explode,startangle=90)

plt.axis("equal")
plt.legend(title="languages",loc="upper right")

plt.show()