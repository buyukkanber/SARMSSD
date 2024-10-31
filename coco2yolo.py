import json
import os
from PIL import Image

def coco_to_yolo(coco_bbox, img_width, img_height):
    x_top_left, y_top_left, bbox_width, bbox_height = coco_bbox
    x_center = x_top_left + bbox_width / 2
    y_center = y_top_left + bbox_height / 2
    x_center_relative = x_center / img_width
    y_center_relative = y_center / img_height
    width_relative = bbox_width / img_width
    height_relative = bbox_height / img_height
    return [x_center_relative, y_center_relative, width_relative, height_relative]

def convert_dataset(coco_annotation_file, images_dir, output_dir):
    # Load COCO annotations
    with open(coco_annotation_file, 'r') as file:
        coco = json.load(file)
    
    # Prepare output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Process each annotation
    for image_info in coco['images']:
        image_id = image_info['id']
        image_path = os.path.join(images_dir, image_info['file_name'])
        image = Image.open(image_path)
        img_width, img_height = image.size
        
        annotations = [ann for ann in coco['annotations'] if ann['image_id'] == image_id]
        
        yolo_annotations = []
        for ann in annotations:
            category_id = ann['category_id'] - 1  # YOLO class ids are zero-indexed
            coco_bbox = ann['bbox']
            yolo_bbox = coco_to_yolo(coco_bbox, img_width, img_height)
            yolo_annotations.append([category_id] + yolo_bbox)
        
        # Save YOLO annotations to a text file
        yolo_annotation_filename = os.path.splitext(image_info['file_name'])[0] + '.txt'
        yolo_annotation_filepath = os.path.join(output_dir, yolo_annotation_filename)
        
        with open(yolo_annotation_filepath, 'w') as file:
            for yolo_annotation in yolo_annotations:
                file.write(' '.join(map(str, yolo_annotation)) + '\n')

# Example usage
convert_dataset('path/to/your/annotations.json', 'path/to/your/images', 'path/to/output/annotations')