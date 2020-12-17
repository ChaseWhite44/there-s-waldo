import os
import matplotlib.pyplot as plt
import numpy as np
import math

from skimage import feature, filters, io, color

import cv2

dir = "images"
files = os.listdir(dir)

def color(file):
    print("new")
    img = io.imread(file)
    new=img.copy()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    plt.figure(file, figsize=[9, 9])

    plt.subplot(1,1,1,title="Color")
    plt.axis('off')
    plt.imshow(hsv)
    hsv_red = cv2.cvtColor(np.uint8([[[255,0,0]]]),cv2.COLOR_BGR2HSV)
    r = hsv_red[0][0][0]
    print(r)
    lower_red = np.array([r-10,100,100])
    upper_red = np.array([r+10,255,255])
    lower_white = np.array([0,0,168])
    upper_white = np.array([255,50,255])


    redMask = cv2.inRange(hsv, lower_red, upper_red)
    whiteMask = cv2.inRange(hsv, lower_white, upper_white)

    mask = cv2.bitwise_or(redMask, whiteMask)

    res = cv2.bitwise_and(img,img, mask= mask)

    ret, thresh = cv2.threshold(mask,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # You need to choose 4 or 8 for connectivity type
    connectivity = 8
    # Perform the operation
    output = cv2.connectedComponentsWithStats(thresh, connectivity, cv2.CV_32S)
    # Get the results
    # The first cell is the number of labels
    num_labels = output[0]
    # The second cell is the label matrix
    labels = output[1]
    # The third cell is the stat matrix
    stats = output[2]
    print(num_labels)
    # The fourth cell is the centroid matrix
    centroids = output[3]

    for i in range(1, num_labels):
        if i%100 == 0:
            print(i)
        pts = np.where(labels == i)
        if stats[i][4] < 1000 or stats[i][4] > 10000:
            labels[pts] = 0

    res[labels == 0] = (0,0,0)
    

   # plt.subplot(2,2,2)
   # plt.axis('off')
  #  plt.imshow(mask,cmap="gray")

    plt.subplot(1,1,1)
    plt.axis('off')
    plt.imshow(res)

    plt.show()

if __name__ == '__main__':
    for file in files:
        color(dir + "/" + file)
        plt.savefig("processed/" + file)



