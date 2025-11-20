import numpy as np

from PIL import Image

import matplotlib.pyplot as plt

import sys

 

def simple_binary_edge_detection_numpy(binary_array):

 

    height, width = binary_array.shape

 

    edge_matrix = np.zeros_like(binary_array)

       

    for r in range(1, height - 1):

        for c in range(1, width - 1):

           

            if binary_array[r, c] == 1:

               

                if (binary_array[r-1, c] == 0 or  # Check neighbor above

                    binary_array[r+1, c] == 0 or  # Check neighbor below

                    binary_array[r, c-1] == 0 or  # Check neighbor to the left

                    binary_array[r, c+1] == 0):   # Check neighbor to the right

                   

                    edge_matrix[r, c] = 1

                   

    return edge_matrix

 

BINARY_THRESHOLD = 128

 

image_path = 'Copy pastu\WhatsApp Image 2025-11-07 at 11.48.48_9a78055a.jpg'

 

try:

    print(f"Loading image from: {image_path}")

    img_pil = Image.open(image_path)

   

 

    img_gray_pil = img_pil.convert('L')

   

   

    img_gray_np = np.array(img_gray_pil)

   

 

    print(f"Binarizing image with threshold={BINARY_THRESHOLD}...")

    img_binary_np = (img_gray_np > BINARY_THRESHOLD).astype(np.uint8)

   

   

    print("Running edge detection...")

    edge_matrix = simple_binary_edge_detection_numpy(img_binary_np)

    print("Done.")

 

    print("Displaying results...")

    plt.figure(figsize=(21, 7))

 

    plt.subplot(1, 3, 1)

    plt.title('1. Original Grayscale Image')

    plt.imshow(img_gray_np, cmap='gray')

    plt.axis('off')

 

    plt.subplot(1, 3, 2)

    plt.title(f'2. Binarized Image (Threshold > {BINARY_THRESHOLD})')

    plt.imshow(img_binary_np, cmap='gray')

    plt.axis('off')

 

    plt.subplot(1, 3, 3)

    plt.title('3. Detected Edges')

    plt.imshow(edge_matrix, cmap='gray')

    plt.axis('off')

 

    plt.tight_layout()

    plt.show()

 

except FileNotFoundError:

    print(f"Error: The file '{image_path}' was not found.")

    print("Please make sure the image is in the same directory as your notebook,")

    print("or update the 'image_path' variable to the correct file path.")

except Exception as e:

    print(f"An error occurred: {e}")

    print("Please ensure you have PIL, NumPy, and Matplotlib installed:")

    print("!pip install pillow numpy matplotlib")