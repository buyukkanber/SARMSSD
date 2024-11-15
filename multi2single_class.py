import os

# Path to the directory containing annotation files
annotation_dir = "/path/to/your/annotations"

# Function to process each annotation file
def convert_to_single_class(annotation_dir):
    for root, _, files in os.walk(annotation_dir):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    lines = f.readlines()
                
                # Convert all annotations to class '0'
                new_lines = []
                for line in lines:
                    parts = line.strip().split()
                    parts[0] = "0"  # Set class ID to 0
                    new_lines.append(" ".join(parts) + "\n")
                
                # Write back the modified annotations
                with open(file_path, "w") as f:
                    f.writelines(new_lines)

# Run the conversion
convert_to_single_class(annotation_dir)
print("Conversion to single class annotations completed.")