# cv_assignment_1.py

# Write a function that divides an image into non-overlapping blocks (e.g., 8x8 or 16x16) 
# and applies a simple pixel manipulation technique such as averaging or quantization to each block. 
# You should reduce the color precision within each block while preserving 
# structural information (for example, reducing the number of unique colors per block).

# Please follow the following guidelines:
# - Use python code.
# - Do not attach any files, submit only the code that takes the input image indicated below and produces an output image saved as "img.jpg".
# - If possible, use only opencv-python, scikit-image and numpy.
# - Make sure your code is properly indented and commented, and executable with Python >= 3.8.
# - Use the following code to load the image as a numpy array:

from skimage import io
import matplotlib.pyplot as plt   # just for representation purposes

img = io.imread('https://t4.ftcdn.net/jpg/07/18/12/87/360_F_718128776_nJReWqPkf5qF4Y5na8ZqGWAbdCJTpczZ.jpg')




plt.imshow(img)
plt.axis('off')  # Hide axes
plt.show()