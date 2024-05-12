#performing the first step that is, making a sample dataset of 500 images from the given dataset
import zipfile
import os
import random
zip_file_path = "train.zip"
output_zip_path = "selected_images.zip"
def select_random_images(zip_file_path, num_images=500):
    selected_images = []
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        image_filenames = [name for name in zip_ref.namelist() if name.endswith('.jpg')]
        selected_images = random.sample(image_filenames, num_images)
    return selected_images
def create_zip_with_selected_images(zip_file_path, selected_images, output_zip_path):
    with zipfile.ZipFile(output_zip_path, 'w') as output_zip:
        with zipfile.ZipFile(zip_file_path, 'r') as input_zip:
            for image_name in selected_images:
                with input_zip.open(image_name) as image_file:
                   output_zip.writestr(image_name, image_file.read())
selected_images = select_random_images(zip_file_path)
create_zip_with_selected_images(zip_file_path, selected_images, output_zip_path)
print("Selected images saved to:", output_zip_path)



#performing the next step that is dividing the dataset into train,val,test
#in the ratio 7:2:1
import shutil
def split_dataset(source_folder, train_folder, val_folder, test_folder, split_ratio=(0.7, 0.2, 0.1)):
    for folder in [train_folder, val_folder, test_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)
    image_files = [file for file in os.listdir(source_folder) if file.endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(image_files)
    num_images = len(image_files)
    num_train = int(num_images * split_ratio[0])
    num_val = int(num_images * split_ratio[1])
    num_test = num_images - num_train - num_val
    for i, file in enumerate(image_files):
        if i < num_train:
            shutil.copy(os.path.join(source_folder, file), os.path.join(train_folder, file))
        elif i < num_train + num_val:
            shutil.copy(os.path.join(source_folder, file), os.path.join(val_folder, file))
        else:
            shutil.copy(os.path.join(source_folder, file), os.path.join(test_folder, file))
source_folder = "selected_images"
train_folder = "train"
val_folder = "val"
test_folder = "test"
split_ratio = (0.7, 0.2, 0.1)
split_dataset(source_folder, train_folder, val_folder, test_folder, split_ratio)




