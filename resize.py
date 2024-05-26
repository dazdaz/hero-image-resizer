from PIL import Image

# Open the image
image_path = 'Blind_monks_examining_an_elephant.jpg'
image = Image.open(image_path)

# Resize the image maintaining aspect ratio
aspect_ratio = image.width / image.height
new_height = 1200
new_width = int(aspect_ratio * new_height)

# Ensure the new width is less than or equal to 2436
if new_width > 2436:
    new_width = 2436
    new_height = int(new_width / aspect_ratio)

resized_image = image.resize((new_width, new_height))

# Create a new image with the desired dimensions (2436 x 1200)
final_image = Image.new('RGB', (2436, 1200), (255, 255, 255))

# Calculate the position to paste the resized image (centered horizontally)
x_offset = (2436 - new_width) // 2
y_offset = (1200 - new_height) // 2

# Paste the resized image onto the new image
final_image.paste(resized_image, (x_offset, y_offset))

# Save the final image
final_image.save('resized_image_with_space.jpg')
