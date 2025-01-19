import os
import cv2
import bm3d
import numpy as np
import shutil

# Paths to the input and output directories
input_directory = './sarmssd' # path/to/your/input/directory
output_directory = './sarmssd_bm3d' # path/to/your/output/directory

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def process_images_and_labels(input_dir, output_dir):
    # Walk through the input directory
    for root, _, files in os.walk(input_dir):
        for filename in files:
            input_path = os.path.join(root, filename)
            relative_path = os.path.relpath(root, input_dir)
            output_subdir = os.path.join(output_dir, relative_path)

            # Create subdirectory if it doesn't exist
            if not os.path.exists(output_subdir):
                os.makedirs(output_subdir)

            # Process images
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tif', '.tiff')):
                output_path = os.path.join(output_subdir, filename)

                # Load the image
                image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

                if image is None:
                    print(f"Failed to load image {filename}")
                    continue

                # Normalize the image to [0, 1]
                normalized_image = image / 255.0

                # Apply BM3D denoising
                denoised_image = bm3d.bm3d(normalized_image, sigma_psd=0.1)  # Adjust sigma_psd as needed

                # Convert back to [0, 255] and uint8
                denoised_image_uint8 = np.clip(denoised_image * 255, 0, 255).astype(np.uint8)

                # Save the processed image
                cv2.imwrite(output_path, denoised_image_uint8)
                print(f"Processed and saved {filename}")

            # Copy YOLO label files
            elif filename.lower().endswith('.txt'):
                output_label_path = os.path.join(output_subdir, filename)
                shutil.copy2(input_path, output_label_path)
                print(f"Copied label file {filename}")

print("Starting processing of images and labels...")
process_images_and_labels(input_directory, output_directory)
print("All images and labels processed.")
