from TemplateMatch import *
import cv2
import os
from waldo import color

dir = "images"
files = os.listdir(dir)
dir1 = "template"
files1 = os.listdir(dir1)

def main(f,f1):

    i=1

    print(files,files1)

    image = cv2.imread(dir + "/" + f[i])
    template = cv2.imread(dir1 + "/" + f1[i])

    templateMatching(image, template)
    color(dir + "/" + f[i])

if __name__ == '__main__':
    main(files,files1)
        