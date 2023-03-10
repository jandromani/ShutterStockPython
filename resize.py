from skimage import io, transform
import os

input_dir = "C:/Users/Antonio/Downloads/midjourney_selection_2023-2-15_172755_[499]"
output_dir = "C:/Users/Antonio/Downloads/midjourney_selection_2023-2-15_172755_[499]/resize"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

image_size = (4096, 4096)

for filename in os.listdir(input_dir):
    if filename.endswith(".png"):
        image = io.imread(os.path.join(input_dir, filename))
        resized_image = transform.resize(image, image_size, anti_aliasing=True)
        io.imsave(os.path.join(output_dir, filename), resized_image, check_contrast=False)