import os
import xml.etree.ElementTree as ET
from PIL import Image

def voc_to_yolo(voc_bbox, img_width, img_height):
    xmin, ymin, xmax, ymax = voc_bbox
    x_center = (xmin + xmax) / 2
    y_center = (ymin + ymax) / 2
    width = xmax - xmin
    height = ymax - ymin

    # Normalize the coordinates by the dimensions of the image
    x_center_relative = x_center / img_width
    y_center_relative = y_center / img_height
    width_relative = width / img_width
    height_relative = height / img_height

    return [x_center_relative, y_center_relative, width_relative, height_relative]

def convert_annotations(voc_annotations_dir, images_dir, output_dir):
    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Process each XML annotation file in the VOC annotations directory
    for annotation_file in os.listdir(voc_annotations_dir):
        if not annotation_file.endswith('.xml'):
            continue
        
        tree = ET.parse(os.path.join(voc_annotations_dir, annotation_file))
        root = tree.getroot()
        
        image_file = root.find('filename').text
        image_path = os.path.join(images_dir, image_file)
        image = Image.open(image_path)
        img_width, img_height = image.size
        
        # Prepare the output file
        yolo_annotation_filename = os.path.splitext(image_file)[0] + '.txt'
        yolo_annotation_filepath = os.path.join(output_dir, yolo_annotation_filename)
        
        with open(yolo_annotation_filepath, 'w') as fil.
            for obj in root.iter('object'):
                class_id = obj.find('name').text
                # Map your class names to indices as needed
                class_id = class_name_to_id[class_id]  # Define your class_name_to_id mapping
                
                voc_bbox = [
                    int(obj.find('bndbox/xmin').text),
                    int(obj.find('bndbox/ymin').text),
                    int(obj.find('bndbox/xmax').text),
                    int(obj.find('bndbox/ymax').text)
                ]
                
                yolo_bbox = voc_to_yolo(voc_bbox, img_width, img_height)
                file.write(f"{class_id} " + " ".join(map(str, yolo_bbox)) + '\n')

# Example class name to ID mapping
class_name_to_id = {
    'ship': 0,
}

# Example usage
convert_annotations('path/to/VOCdevkit/Annotations', 'path/to/VOCdevkit/JPEGImages', 'path/to/yolo/annotations')
