import cv2

# Load the image
image = cv2.imread('path_to_image.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Canny edge detection
edges = cv2.Canny(blurred_image, 100, 200)

# Display the original image, grayscale image, and edges
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Edges', edges)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()