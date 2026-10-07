# Detect edges in an image

import cv2

# Read image
img = cv2.imread("profile.jpeg",0)

# Canny Edge Detection 
edges = cv2.Canny(img,100,100)
 
# # Create resizable windows
# cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
# cv2.namedWindow("Edges", cv2.WINDOW_NORMAL)

# # Set window size
# cv2.resizeWindow("Original", 900, 900)
# cv2.resizeWindow("Edges", 900, 900)

cv2.imshow("Original",img)
cv2.imshow("Edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows() 
