# --------------------------------------------------
# 6x6 Grayscale Image
# Top Half = Black (0)
# Bottom Half = White (255)
# Apply 3x3 kernel for Edge Detection 
# Show Feature Map 
# --------------------------------------------------

import numpy as np

# --------------------------------------------------
# Step 1 : Create 6x6 Image
# --------------------------------------------------

image = np.array([
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [255,255,255,255,255,255],
    [255,255,255,255,255,255],
    [255,255,255,255,255,255]
])

print("Original 6x6 Image")
print(image)

# --------------------------------------------------
# Step 2 : 3X3 Kernel for Horizontal Edge Detection 
# --------------------------------------------------

kernel = np.array([
                    [-1,-1,-1],
                    [ 0, 0, 0],
                    [ 1, 1, 1]
                  ])

print("3x3 Kernel")
print(kernel)

# --------------------------------------------------
# Step 3 : Convolutional Operataion 
# Output Size = (6-3+1) x (6-3+1) = 4x4 =16 
# --------------------------------------------------
feature_map = np.zeros((4,4)) 

for i in range(4):
    for j in range(4):

        # Extract 3x3 region 
        region = image[i:i+3,j:j+3]

        # Multipy and Sum
        result = np.sum(region * kernel)

        # Store result
        feature_map[i][j] = result

# --------------------------------------------------
# Step 4 : Show Feature Map 
# --------------------------------------------------
print("Feature Map (Detected Edge)")
print(feature_map)