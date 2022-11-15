from PIL import Image

def decode_image(path_to_png):
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    # Set pixels on decoded_image to decoded values:
    for y in range(y_size):
        for x in range(x_size):
            red_pixel = (red_channel.getpixel((x, y)))
            pixel_binary = bin(red_pixel)
            if (pixel_binary[-1] == '0'):
                pixels[x, y] = (0, 0, 0)
            else:
                pixels[x, y] = (255, 255, 255)

    # Save the decoded image to disk:
    decoded_image.save("decoded_image.png")

def encode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    pass

def write_text(text_to_write):
    """
    TODO: Add docstring and complete implementation.
    """
    pass

decode_image('images/encoded_sample.png')
