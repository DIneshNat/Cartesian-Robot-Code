import cv2
import matplotlib.pyplot as plt

#Opens/reads image
img = cv2.imread('Tiger.jpg')

#Converts image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Thresholds the image
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

#Generates contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Puts contours and points in array
pointCords = []
for contour in contours:
    for point in contour:
        x, y = point[0]
        pointCords.append((x, y))

#Plots points/contours
fig, ax = plt.subplots()
for contour in contours:
    ax.plot(contour[:, 0, 0], contour[:, 0, 1], linewidth=2)
plt.show()