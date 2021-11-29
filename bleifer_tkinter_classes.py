import tkinter as tk
from tkinter import ttk
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg


class CustomScale(tk.Frame):
    def __init__(self, parent, label, from_=0, to_=10):
        tk.Frame.__init__(self, parent)

        self.tkvar = tk.DoubleVar()
        self.tkvar.trace_add('write', self.updateEntry)
        self.tkvar.set(from_)
        self.label = label
        self.scale = tk.Scale(self, label=self.label, from_=from_, to_=to_, orient='horizontal', command=self.updateScale)
        #self.label = tk.Label(self, text=label, anchor="w")
        self.entry = tk.Entry(self, textvariable=self.tkvar)
        #self.entry.insert(from_)
        self.scale.pack(side='left')
        self.entry.pack(side='right')

    def get(self):
        return self.scale.get()

    def update1(self, val):
        #self.tkvar = val
        self.entry.set(val)

    def updateScale(self, val):
        self.tkvar.set(val)
        print('Updating Scale '+self.label+' : New value: '+str(val))

    def updateEntry(self,a,b,c):
        #print(a)
        #print(b)
        #print(c)
        if self.scale.get()!=self.tkvar:
            self.scale.set(float(self.entry.get()))
            print('Updating Scale '+self.label+' : New value: ' + self.entry.get())


class CustomHoughTransformInterface(tk.Frame):
    def __init__(self, parent, label, dp=.8, minDist=30,
                          edgeParam=50, perfCircleParam=30, minRadius=0, maxRadius=100):
        tk.Frame.__init__(self, parent)

        self.paramObjlist=[]

        self.dpScale = CustomScale(root, label='dp', from_=0, to_=1000)
        self.dpScale.updateScale(dp)
        self.dpScale.pack()
        self.paramObjlist.append(self.dpScale)
        self.minDistScale = CustomScale(root, label='Minimum Distance', from_=0, to_=1000)
        self.minDistScale.updateScale(minDist)
        self.minDistScale.pack()
        self.paramObjlist.append(self.minDistScale)
        self.edgeParamScale = CustomScale(root, label='Edge Parameter', from_=0, to_=1000)
        self.edgeParamScale.updateScale(edgeParam)
        self.edgeParamScale.pack()
        self.paramObjlist.append(self.edgeParamScale)
        self.perfCircleScale = CustomScale(root, label='Perfect Circle Parameter', from_=0, to_=1)
        self.perfCircleScale.updateScale(perfCircleParam)
        self.perfCircleScale.pack()
        self.paramObjlist.append(self.perfCircleScale)
        self.minRadiusScale = CustomScale(root, label='Min Radius (nm)', from_=0, to_=1000)
        self.minRadiusScale.updateScale(minRadius)
        self.minRadiusScale.pack()
        self.paramObjlist.append(self.minRadiusScale)
        self.maxRadiusScale = CustomScale(root, label='Max Radius (nm)', from_=0, to_=1000)
        self.maxRadiusScale.updateScale(maxRadius)
        self.maxRadiusScale.pack()
        self.paramObjlist.append(self.maxRadiusScale)

        self.newPlotButton = tk.Button(root, text='Run Image Analysis', command=self.newPlt)
        self.newPlotButton.pack()

    def getParams(self):
       print('todo')

    def newPlt(self):
        img = cv.imread('11056-83_5.jpg', 0)
        img = cv.medianBlur(img, 5)
        cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
        circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, self.dpScale.get(), self.minDistScale.get(),
                                  param1=self.edgeParamScale.get(), param2=self.perfCircleScale.get(),
                                  minRadius=self.minRadiusScale.get(), maxRadius=self.maxRadiusScale.get())
        # circles = cv.HoughCircles
        # print(circles)
        radii = []
        for circle in circles:
            for val in circle:
                radii.append(val[2] * 20)
                # print(val[2])
        circles = np.uint16(np.around(circles))
        # print(circles)
        # radii=circles
        # print(circles[0,0,0])
        for i in circles[0, :]:
            # draw the outer circle
            cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
        # cv.imshow('detected circles',cimg)
        # img = mpimg.imread(cimg)
        # print(img)
        #fig, ax = plt.subplots()
        imgplot = plt.imshow(cimg)
        plt.show()
        # cv.waitKey(0)
        # cv.destroyAllWindows()

        plt.hist(radii, density=True, bins=30)  # density=False would make counts
        plt.ylabel('count')
        plt.xlabel('Radius(nm)')
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()


    """
    minRadiusScale = CustomScale(root, label='Min Radius (nm)', from_=0, to_=1000)
    minRadiusScale.pack()
    maxRadiusScale = CustomScale(root, label='Max Radius (nm)', from_=0, to_=1000)
    maxRadiusScale.pack()
    #maxRadiusScale = tk.Scale(root, label='Max Radius (nm)', from_=0, to_=10000, orient='horizontal')
    """
    Gui = CustomHoughTransformInterface(root, label='String')
    Gui.pack()
    root.mainloop()
