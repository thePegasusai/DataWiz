import os

# Define the root directory and dataset name
root_dir = 'HOME/'
dataset_name = 'dataset-name'

# Define the subdirectories
subdirectories = ['test', 'train', 'valid']
subdirectories_images = ['images']
subdirectories_labels = ['labels']

# Create the directory structure
dataset_dir = os.path.join(root_dir, dataset_name)
os.makedirs(dataset_dir, exist_ok=True)

for subdir in subdirectories:
    subdir_path = os.path.join(dataset_dir, subdir)
    os.makedirs(subdir_path, exist_ok=True)
    
    images_dir = os.path.join(subdir_path, 'images')
    os.makedirs(images_dir, exist_ok=True)
    
    labels_dir = os.path.join(subdir_path, 'labels')
    os.makedirs(labels_dir, exist_ok=True)
    
# Generate sample file paths
image_paths = [os.path.join(dataset_dir, 'test', 'images', f'image-{i}.jpg') for i in range(5)]
label_paths = [os.path.join(dataset_dir, 'test', 'labels', f'image-{i}.txt') for i in range(5)]

# Print the generated file paths
print("Generated file paths:")
print("Image paths:")
for image_path in image_paths:
    print(image_path)
    
print("\nLabel paths:")
for label_path in label_paths:
    print(label_path)

HOME/
└── dataset-name/
    ├── test/
    │   ├── images/
    │   │   ├── image-0.jpg
    │   │   ├── image-1.jpg
    │   │   ├── image-2.jpg
    │   │   ├── image-3.jpg
    │   │   └── image-4.jpg
    │   └── labels/
    │       ├── image-0.txt
    │       ├── image-1.txt
    │       ├── image-2.txt
    │       ├── image-3.txt
    │       └── image-4.txt
    ├── train/
    │   ├── images/
    │   └── labels/
    ├── valid/
    │   ├── images/
    │   └── labels/
    └── data.yaml

