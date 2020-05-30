# 图像分割部分代码
import cv2
import numpy as np

count = 1

for i in range (1,11):
    image = cv2.imread("./RISC-VDigilent/id/"+str(count)+".jpg")
    #print(image.shape)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    thresh = np.array(thresh)


    def countPoint(img):
        re = []
        for th in img:
            re.append(sum(th) / 255)
        return re


    def findPoint(img, axis):
        if (axis == 'y'):
            img = img.T
        start = -1
        end = -1
        result = []
        countx = countPoint(img)
        for x in range(len(countx)):
            if (countx[x] != 0 and start < 0):
                start = x
            elif (countx[x] != 0):
                end = x
            elif (countx[x] == 0 and start > 0):
                result.append([start, end])
                start, end = -1, -1
        return result


    def Cut(img, axis):
        point = findPoint(img, axis)
        re = []
        for x in point:
            if (axis == 'x'):
                re.append(img[x[0]: x[1]])
            elif (axis == 'y'):
                re.append(img[:, x[0]: x[1]])
        return re


    def cutImage(img):
        for r_x in Cut(img, 'x'):
            for r_y in Cut(r_x, 'y'):
                r_y = cv2.resize(r_y, (16, 16))
                if r_y[2][1] == 21:  # 0
                    print('0', end='')
                if r_y[3][8] == 69:  # 1
                    print('1', end='')
                if r_y[10][4] == 63:  # 2
                    print('2', end='')
                if r_y[2][2] == 67:  # 3
                    print('3', end='')
                if r_y[5][5] == 39:  # 4
                    print('4', end='')
                if r_y[2][5] == 87:  # 5
                    print('5', end='')
                if r_y[7][4] == 45:  # 6
                    print('6', end='')
                if r_y[11][5] == 55:  # 7
                    print('7', end='')
                if r_y[7][3] == 21:  # 8
                    print('8', end='')
                if r_y[7][3] == 234:  # 9
                    print('9', end='')
                if r_y[12][10] == 100:  # X
                    print('X', end='')


    cutImage(thresh)
    print()
    count += 1
