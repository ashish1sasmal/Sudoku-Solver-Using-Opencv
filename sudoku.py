import cv2
import imutils
from imutils import contours
import numpy as np
from digit_recognition import digits

from sudoku_solver import solve_sudoku

cv2.namedWindow("Sudoku",cv2.WINDOW_NORMAL)

img = cv2.imread("sudoku2.jpg")

img = cv2.resize(img, (260,260),interpolation = cv2.INTER_CUBIC)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
canny = cv2.Canny(blur,100,220)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)

out = img.copy()

cnts = cv2.findContours(canny.copy(), cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

cnts,_ = contours.sort_contours(cnts,"left-to-right")
cnts,_ = contours.sort_contours(cnts,"top-to-bottom")

print(img.shape)

sorted_grid = []
for i in range(9):
    sorted_grid.append([])


boxarea = cv2.contourArea(cnts[0])//81




ind=0

for (i,c) in enumerate(cnts):
    area = cv2.contourArea(c)
    hull = cv2.convexHull(c)
    hull_area = cv2.contourArea(hull)
    solidity = float(area)/hull_area
    x,y,w,h = cv2.boundingRect(c)
    equi_diameter = np.sqrt(4*area/np.pi)
    # print(equi_diameter)
    aspect_ratio = float(w)/h
    # print(solidity,area,equi_diameter)
    # print(aspect_ratio)
    if solidity>0.995 and equi_diameter>6 and abs(boxarea-area)<200:
        # print(solidity)
        x,y,w,h = cv2.boundingRect(c)
        # out = cv2.rectangle(out,(x,y),(x+w,y+h),(0,255,0),2)
        # print(digits(img[y:y+h, x:x+w]))
        # print(ind,ind//9)
        m1 = int(x+w/2)
        m2 = int(y+h/2)
        sorted_grid[ind//9].append([[x,y],[w,h],[(m1+m2)//2],c])
        ind +=1
        #
        # cv2.imshow("Sort",out)
        # k = cv2.waitKey(0)
        # if k == 27:
        #     break

# sorted_grid.sort(key=lambda x:x[0][1])


for i in sorted_grid:
    i.sort(key = lambda x:x[2])


grid =[]
for i in range(9):
    grid.append([None]*9)

for i in range(9):
    for j in range(9):
        cell = sorted_grid[i][j]
        x,y,w,h = cell[0][0],cell[0][1],cell[1][0],cell[1][1]
        grid[i][j] = digits(img[y:y+h, x:x+w])
        sorted_grid[i][j].append(grid[i][j])

solved_grid = solve_sudoku(grid)

print("[Sudoku Solved !].....")

for i in range(9):
    for j in range(9):
        cell = sorted_grid[i][j]
        x,y = tuple(cell[0])
        w,h = tuple(cell[1])
        if cell[-1] == 0:
            cv2.putText(out, str(solved_grid[i][j]),(int(x+w/2)-5, int(y+h/2)+5),cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

cv2.imwrite("Results/sudoku_sol1.jpg",out)
cv2.imshow("Sudoku",out)
cv2.waitKey(0)
