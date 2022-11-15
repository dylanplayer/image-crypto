from PIL import Image, ImageDraw

FILE_NAME = "dog.png"
TEXT = "Zombie ipsum reversus ab viral inferno"

def decode_image(path_to_png):
    encoded_image = Image.open(path_to_png)

    red_channel = encoded_image.split()[0]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    for y in range(y_size):
        for x in range(x_size):
            red_pixel = (red_channel.getpixel((x, y)))
            pixel_binary = bin(red_pixel)
            if (pixel_binary[-1] == '0'):
                pixels[x, y] = (0, 0, 0)
            else:
                pixels[x, y] = (255, 255, 255)

    decoded_image.save(f"output/decoded_{FILE_NAME}")

def encode_image(path_to_png, text_to_encode):
    original_image = Image.open(path_to_png)
    original_pixels = original_image.load()

    decoded_image = generate_image_with_text(text_to_encode, original_image.size)
    decoded_pixels = decoded_image.load()

    encoded_image = Image.new("RGB", original_image.size)
    encoded_image_pixels = encoded_image.load()

    x_size, y_size = encoded_image.size

    for y in range(y_size):
        for x in range(x_size):
            original_pixel_r, original_pixel_g, original_pixel_b = original_pixels[x, y]
            encoded_red_pixel = original_pixel_r
            encoded_red_pixel_binary = bin(encoded_red_pixel)
            decoded_pixel = decoded_pixels[x, y]

            if decoded_pixel == (255, 255, 255):
                encoded_red_pixel_binary = encoded_red_pixel_binary[:-1] + "1"
            else:
                encoded_red_pixel_binary = encoded_red_pixel_binary[:-1] + "0"

            encoded_red_pixel = int(encoded_red_pixel_binary, 2)
            encoded_image_pixels[x, y] = (encoded_red_pixel, original_pixel_g, original_pixel_b)
    
    encoded_image.save(f"output/encoded_{FILE_NAME}")

def generate_image_with_text(text_to_write, size):
    img = Image.new("RGB", size)
    new_img = ImageDraw.Draw(img)
    new_img.text((20, 20), text_to_write, fill=(255, 255, 255))
    return img

encode_image(FILE_NAME, TEXT)
decode_image(f"output/encoded_{FILE_NAME}")
