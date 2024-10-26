import cv2
import numpy as np
import os

# Set the folders for input images and where to save masks
input_folder = 'input_images'
output_folder = 'output_masks'
os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn’t already exist

# RGB threshold for each channel
threshold_value = 200

# Function to make a mask and count white pixels
def create_mask(image_file):
    img = cv2.imread(image_file)  # Read the image
    if img is None:
        print(f"Error loading {image_file}")
        return 0
    
    # Mask pixels where all channels exceed the threshold
    mask = cv2.inRange(img, (threshold_value, threshold_value, threshold_value), (255, 255, 255))
    
    # Count white pixels
    white_pixel_count = np.sum(mask == 255)
    
    # Save the mask image
    output_name = os.path.join(output_folder, os.path.basename(image_file).split('.')[0] + '_mask.png')
    cv2.imwrite(output_name, mask)
    
    return white_pixel_count

# Main function to run the workflow
def main():
    total_white_pixels = 0  # Initialize counter for white pixels

    # Loop through each image file in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith(('.png', '.jpg')):
            image_path = os.path.join(input_folder, file_name)
            total_white_pixels += create_mask(image_path)

    print("Total white pixels across all images:", total_white_pixels)

# Run main function
if __name__ == '__main__':
    main()
