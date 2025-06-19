import cv2
import os
import csv

# Define label category mapping
label_dict = {
    '1': 'front',
    '2': 'side',
    '3': 'rear',
    '4': 'inside',
    '5': 'distant',
    '6': 'no car'
}

frames_folder = "frames"           # Folder containing original frames
labeled_folder = "labeled_frames"  # Output folder for labeled images
csv_filename = "labels.csv"

os.makedirs(labeled_folder, exist_ok=True)

# set up list of files
starting_file = "frame_0000.jpg"
starting_index = int(starting_file.split('_')[1].split('.')[0])
image_files = sorted([f for f in os.listdir(frames_folder) if f.endswith(('.jpg', '.png'))])
image_files_filtered = [f for f in image_files if int(f.split('_')[1].split('.')[0]) >= starting_index]

print(f"{len(image_files_filtered)} images to label starting from '{starting_file}'")

# iterate through files
quit_program = False
for image_file in image_files_filtered:
    if quit_program:
        break

    img_path = os.path.join(frames_folder, image_file)
    img = cv2.imread(img_path)
    
    if img is None:
        print(f"Failed to load {image_file}")
        continue

    cv2.imshow('Labeling - Press 1-6 to label, ESC to skip, q to quit', img)

    # wait for user to label or quit
    while True:
        key = cv2.waitKey(0) & 0xFF  # Wait for keypress

        if key == ord('q'):  # Quit key
            print("Quitting program.")
            quit_program = True
            cv2.destroyWindow('Press 1:front, 2:side, 3:rear, 4:inside, 5:distant, 6:no car, q to quit')
            break

        elif chr(key) in label_dict:
            label = label_dict[chr(key)]
            filename_base, ext = os.path.splitext(image_file)
            labeled_filename = f"{filename_base}_{label}{ext}"
            labeled_path = os.path.join(labeled_folder, labeled_filename)
            cv2.imwrite(labeled_path, img)
            print(f"Labeled {image_file} as '{label}' → saved as {labeled_filename}")

            with open(csv_filename, mode='a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([image_file, labeled_filename, label])

            cv2.destroyWindow('Labeling - Press 1-6 to label, ESC to skip, q to quit')
            break

        else:
            print("Invalid key! Please press 1-6 to label, ESC to skip, or q to quit.")

# Ensure all windows close
cv2.waitKey(1) 
cv2.destroyAllWindows()
print("Labeling completed. All windows closed.")
