import cv2
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
im = args["image"]
img = cv2.imread(im)
img_og = img.copy()
fill_color = [169, 169, 169]
mask_value = 255

if im == "front.jpg":
    point_one = (401, 2665)
    point_two = (3809, 2681)
    point_three = (2025, 1545)

if im == "left.jpg":
    point_one = (2601, 2873)
    point_two = (3809, 1913)
    point_three = (1873, 1681)

if im == "right.jpg":
    point_one = (337, 2225)
    point_two = (2801, 2761)
    point_three = (2265, 1560)

triangle = [np.array([point_one, point_two, point_three])]
stencil = np.zeros(img.shape[:-1]).astype(np.uint8)
cv2.fillPoly(stencil, triangle, mask_value)
sel = stencil != mask_value
img[sel] = fill_color

x = (point_one[0]+point_two[0]+point_three[0])//3
y = (point_one[1]+point_two[1]+point_three[1])//3

product = img.copy()
gray = cv2.cvtColor(product, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
detected_lines = cv2.HoughLinesP(edges, 1, np.pi/380, 30, maxLineGap=400)

for detected_line in detected_lines:
    x1, y1, x2, y2 = detected_line[0]
    cv2.line(product, (x1, y1), (x2, y2), (0, 0, 225), 5)

x2 = point_three[0]
down_point = point_three[1]

image = cv2.arrowedLine(img_og, (x-10, y), (x2, down_point), (0, 0, 0), 20)
cv2.imshow("Final Product", np.hstack([product, image]))
cv2.waitKey(0)
