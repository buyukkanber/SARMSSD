import os
import numpy as np

# Define the class mapping
class_mapping = {
    "ore-oil": 0,
    "Cell-Container": 1,
    "Fishing": 2,
    "LawEnforce": 3,
    "Dredger": 4,
    "Container": 5
}

# Define the conversion function
def obb_to_hbb_yolo_format(annotations, img_width=1024, img_height=1024):
    yolo_annotations = []
    for annotation in annotations:
        x1, y1, x2, y2, x3, y3, x4, y4, category, _ = annotation
        
        # Get class ID from mapping
        class_id = class_mapping.get(category, -1)
        if class_id == -1:
            continue  # Skip if category not in mapping
        
        # Convert to numpy arrays for easy manipulation
        x_coords = np.array([x1, x2, x3, x4])
        y_coords = np.array([y1, y2, y3, y4])
        
        # Find the bounding box in HBB format
        x_min, x_max = np.min(x_coords), np.max(x_coords)
        y_min, y_max = np.min(y_coords), np.max(y_coords)
        
        # Calculate the center, width, and height of the bounding box
        x_center = (x_min + x_max) / 2
        y_center = (y_min + y_max) / 2
        width = x_max - x_min
        height = y_max - y_min
        
        # Normalize the values for YOLO format
        x_center_norm = x_center / img_width
        y_center_norm = y_center / img_height
        width_norm = width / img_width
        height_norm = height / img_height
        
        # Append the YOLO formatted annotation
        yolo_annotations.append(f"{class_id} {x_center_norm} {y_center_norm} {width_norm} {height_norm}")
    
    return yolo_annotations

# Define paths
dataset_path = "/path/to/dataset"  # The 'SRSSD' dataset's root path 
subsets = ["train", "test"]

for subset in subsets:
    labels_path = os.path.join(dataset_path, subset, "labels")
    output_labels_path = os.path.join(dataset_path, subset, "labels_yolo")
    os.makedirs(output_labels_path, exist_ok=True)  # Ensuring output folder exists

    for label_file in os.listdir(labels_path):
        input_path = os.path.join(labels_path, label_file)
        output_path = os.path.join(output_labels_path, label_file)

        # Read the original annotations
        with open(input_path, 'r') as f:
            annotations = []
            for line in f:
                parts = line.strip().split()
                # Convert parts to the expected types
                annotation = tuple(map(int, parts[:8])) + (parts[8], int(parts[9]))
                annotations.append(annotation)

        # Convert annotations
        yolo_annotations = obb_to_hbb_yolo_format(annotations)

        # Write the YOLO annotations to the output file
        with open(output_path, 'w') as f:
            for yolo_annotation in yolo_annotations:
                f.write(yolo_annotation + "\n")

print("Conversion completed.")
