# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import tkinter as tk
from tkinter import ttk
import matplotlib.image as mpimg
import bleifer_tkinter_classes


"""
root = tk.Tk()
label1 = ttk.Label(root, text='ttk window')
label1.pack()

scale1 = tk.Scale(root, label = 'param 1', from_=0, to_=10, orient='horizontal')
scale1.pack()

scale2 = tk.Scale(root, label = 'param 1', from_=0, to_=20, orient='horizontal')
scale2.pack()

param1Scale = tk.Scale(root, label= 'param 1', from_=0, to_=100, orient='horizontal')
param1Scale.pack()

param2Scale = tk.Scale(root, label= 'param 2', from_=0, to_=100, orient='horizontal')
param2Scale.pack()

minRadiusScale = tk.Scale(root, label= 'Min Radius (nm)', from_=0, to_=1000, orient='horizontal')
minRadiusScale.pack()

maxRadiusScale = tk.Scale(root, label= 'Max Radius (nm)', from_=0, to_=10000, orient='horizontal')
maxRadiusScale.pack()

root.mainloop()
"""

img = cv.imread('11056-83_5.jpg', 0)
img = cv.medianBlur(img, 5)
cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, .8, 30,
                          param1=50, param2=30, minRadius=0, maxRadius=100)
#circles = cv.HoughCircles
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
#img = mpimg.imread(cimg)
# print(img)
fig, ax = plt.subplots()
imgplot = plt.imshow(cimg)

"""
img = ax.imshow(cimg)
axcolor = 'yellow'
ax_slider = plt.axes()
slider = Slider(ax_slider, 'Slide->', valmin=0, valmax=30, valinit=2)
"""

def update(val):
    ax.imshow(cimg)


#fig.canvas.draw_idle()
#slider.on_changed(update)
plt.show()
# cv.waitKey(0)
# cv.destroyAllWindows()

plt.hist(radii, density=True, bins=30)  # density=False would make counts
plt.ylabel('count')
plt.xlabel('Radius(nm)')
plt.show()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
