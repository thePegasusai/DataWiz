import os

# Define the root directory and dataset name
root_dir = 'HOME/'
dataset_name = 'dataset-name'

# Define the variations
variations = ['variation1', 'variation2', 'variation3']

# Create the directory structure
dataset_dir = os.path.join(root_dir, dataset_name)
os.makedirs(dataset_dir, exist_ok=True)

for variation in variations:
    variation_dir = os.path.join(dataset_dir, variation)
    os.makedirs(variation_dir, exist_ok=True)
    
    images_dir = os.path.join(variation_dir, 'images')
    os.makedirs(images_dir, exist_ok=True)
    
    labels_dir = os.path.join(variation_dir, 'labels')
    os.makedirs(labels_dir, exist_ok=True)

    # Generate sample file paths for the variation
    image_paths = [os.path.join(variation_dir, 'images', f'{variation}_image-{i}.jpg') for i in range(5)]
    label_paths = [os.path.join(variation_dir, 'labels', f'{variation}_image-{i}.txt') for i in range(5)]

    # Print the generated file paths for the variation
    print(f"Generated file paths for {variation}:")
    print("Image paths:")
    for image_path in image_paths:
        print(image_path)

    print("\nLabel paths:")
    for label_path in label_paths:
        print(label_path)
    print()

# Example: Accessing file paths for variation 2
variation2_images_dir = os.path.join(dataset_dir, 'variation2', 'images')
variation2_labels_dir = os.path.join(dataset_dir, 'variation2', 'labels')

variation2_image_paths = [os.path.join(variation2_images_dir, f'variation2_image-{i}.jpg') for i in range(5)]
variation2_label_paths = [os.path.join(variation2_labels_dir, f'variation2_image-{i}.txt') for i in range(5)]

print("Example: File paths for variation 2")
print("Image paths:")
for image_path in variation2_image_paths:
    print(image_path)

print("\nLabel paths:")
for label_path in variation2_label_paths:
    print(label_path)
HOME/
└── dataset-name/
    ├── variation1/
    │   ├── images/
    │   │   ├── variation1_image-0.jpg
    │   │   ├── variation1_image-1.jpg
    │   │   ├── variation1_image-2.jpg
    │   │   ├── variation1_image-3.jpg
    │   │   └── variation1_image-4.jpg
    │   └── labels/
    │       ├── variation1_image-0.txt
    │       ├── variation1_image-1.txt
    │       ├── variation1_image-2.txt
    │       ├── variation1_image-3.txt
    │       └── variation1_image-4.txt
    ├── variation2/
    │   ├── images/
    │   │   ├── variation2_image-0.jpg
    │   │   ├── variation2_image-1.jpg
    │   │   ├── variation2_image-2.jpg
    │   │   ├── variation2_image-3.jpg
    │   │   └── variation2_image-4.jpg
    │   └── labels/
    │       ├── variation2_image-0.txt
    │       ├── variation2_image-1.txt
    │       ├── variation2_image-2.txt
    │       ├── variation2_image-3.txt
    │       └── variation2_image-4.txt
    ├── variation3/
    │   ├── images/
    │   │   ├── variation3_image-0.jpg
    │   │   ├── variation3_image-1.jpg
    │   │   ├── variation3_image-2.jpg
    │   │   ├── variation3_image-3.jpg
    │   │   └── variation3_image-4.jpg
    │   └── labels/
    │       ├── variation3_image-0.txt
    │       ├── variation3_image-1.txt
    │       ├── variation3_image-2.txt
    │       ├── variation3_image-3.txt
    │       └── variation3_image-4.txt
    └── data.yaml
