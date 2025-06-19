import os
from torchvision import transforms
from torchvision.utils import save_image
from PIL import Image

# Original image folder
input_dir = 'C:/Users/fires/Downloads/BalancedData/train'

augment_transform = transforms.Compose([
    transforms.CenterCrop(360),
    transforms.Resize(128),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.ColorJitter(brightness=0.2, contrast=0.2), # still add some random noise
    transforms.ToTensor()
])

# Number of augmented versions per image
N = 2

# Go through each class folder
for class_name in os.listdir(input_dir):
    class_path = os.path.join(input_dir, class_name)
    if not os.path.isdir(class_path):
        continue

    output_class_path = os.path.join(input_dir, class_name)

    # For each image
    for img_name in os.listdir(class_path):
        img_path = os.path.join(class_path, img_name)
        if img_path.count('_') == 3: # only augment original images
            try:
                img = Image.open(img_path).convert("RGB")
            except:
                print(img_path, "is corrupted")
                continue  # skip

            # Create and save augmentations
            for i in range(N):
                augmented = augment_transform(img)
                aug_name = f"{os.path.splitext(img_name)[0]}_cropped{i}.jpg"
                save_image(augmented, os.path.join(output_class_path, aug_name))                        

print("Done")