import cv2
import os
import shutil

# Paths to the input and output directories
input_directory = './sarmssd' # path/to/your/input/directory
output_directory = './sarmssd_median' # path/to/your/output/directory

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

                # Apply a median filter to reduce speckles
                speckle_free_image = cv2.medianBlur(image, 5)

                # Save the processed image
                cv2.imwrite(output_path, speckle_free_image)
                print(f"Processed and saved {filename}")

            # Copy YOLO label files
            elif filename.lower().endswith('.txt'):
                output_label_path = os.path.join(output_subdir, filename)
                shutil.copy2(input_path, output_label_path)
                print(f"Copied label file {filename}")

print("Starting processing of images and labels...")
process_images_and_labels(input_directory, output_directory)
print("All images and labels processed.")
