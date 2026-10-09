# Show the image pixel values

import cv2
import matplotlib.pyplot as plt

# 1.Read the image 
img = cv2.imread("sample.png")
# OpenCV reads the image and stores it as a NumPy array
# print(img)s

print("Shape of image (RGB):",img.shape)

# 2. Convert to GrayScale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
# This converts the 3-channel BGR image into a single-channel grayscale image.
print(gray)    #print pixel values
print("Shape of image After Converting to GrayScale :",gray.shape)


# 3. Display image + pixel grid
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(gray,cmap="gray") #displays the grayscale matrix as an image.


plt.title("Grayscale Image :")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(gray,cmap="gray") #cmap="gray" tells Matplotlib: small value → dark,large value → light

plt.colorbar(label="pixel value")
plt.title("Pixel Values")

plt.show()