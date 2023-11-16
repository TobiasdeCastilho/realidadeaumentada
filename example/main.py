import cv2 as cv
import imageio as img
import ar as ar

ar.arShow(cv.aruco.DICT_4X4_1000, cv.VideoCapture('/dev/video2'), [640, 480],[
            {"id": 218, "image": [cv.imread('./assets/218.jpeg')]},
            {"id": 11, "image": [cv.cvtColor(i, cv.COLOR_RGB2BGR) for i in img.mimread('./assets/11.gif')]},
            {"id": 22, "image": [cv.cvtColor(i, cv.COLOR_RGB2BGR) for i in img.mimread('./assets/22.gif')]},
            {"id": 33, "image": [cv.cvtColor(i, cv.COLOR_RGB2BGR) for i in img.mimread('./assets/ij.gif')]},
            {"id": 44, "image": [cv.cvtColor(i, cv.COLOR_RGB2BGR) for i in img.mimread('./assets/44.gif')]},
            {"id": 55, "image": [cv.cvtColor(i, cv.COLOR_RGB2BGR) for i in img.mimread('./assets/55.gif')]},
            {"id": 66, "image": [cv.cvtColor(i, cv.COLOR_RGB2BGR) for i in img.mimread('./assets/66.gif')]},])