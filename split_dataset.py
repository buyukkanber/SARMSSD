import os
import shutil
import random
from pathlib import Path

# Define the path to your dataset folder
dataset_path = 'path/to/yolo/annotations'  # dataset path

# Define ratios for splitting
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

# Gather image files
img_files = [f for f in os.listdir(dataset_path) if f.endswith('.jpg')]

# Shuffle files to ensure randomness in splits
random.shuffle(img_files)

# Calculate split indices
train_count = int(len(img_files) * train_ratio)
val_count = int(len(img_files) * val_ratio)

# Split the files into train, val, and test sets
train_files = img_files[:train_count]
val_files = img_files[train_count:train_count + val_count]
test_files = img_files[train_count + val_count:]

# Define subdirectories for splits
split_paths = {
    'train': {'images': Path(dataset_path) / 'train/images', 'labels': Path(dataset_path) / 'train/labels'},
    'val': {'images': Path(dataset_path) / 'val/images', 'labels': Path(dataset_path) / 'val/labels'},
    'test': {'images': Path(dataset_path) / 'test/images', 'labels': Path(dataset_path) / 'test/labels'}
}

# Create directories
for split, paths in split_paths.items():
    paths['images'].mkdir(parents=True, exist_ok=True)
    paths['labels'].mkdir(parents=True, exist_ok=True)

# Function to move files to respective directories
def move_files(file_list, split):
    for img_file in file_list:
        # Determine corresponding label file
        label_file = img_file.replace('.jpg', '.txt')
        
        # Move image file
        shutil.move(os.path.join(dataset_path, img_file), split_paths[split]['images'] / img_file)
        
        # Move label file if it exists
        if os.path.exists(os.path.join(dataset_path, label_file)):
            shutil.move(os.path.join(dataset_path, label_file), split_paths[split]['labels'] / label_file)

# Move files to train, val, and test folders
move_files(train_files, 'train')
move_files(val_files, 'val')
move_files(test_files, 'test')
