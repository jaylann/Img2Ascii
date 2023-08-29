from PIL import Image
import numpy as np
import argparse
import pyperclip

# ASCII characters to use for different intensity values
ASCII_CHARS = '@%#*+=-:. '


class ImageProcessor:
    def __init__(self, image_path: str, detail_size: int = 1):
        """
        Constructor for the ImageProcessor class.

        image_path: str, path to the image file.
        detail_size: int, factor to scale the detail of the output ascii art.
        """
        self.image_path = image_path
        self.detail_size = detail_size

    def load_image(self):
        """
        Opens the image file and returns the image.

        returns: PIL.Image, the opened image.
        """
        return Image.open(self.image_path)

    def resize_image(self, image, new_width=100):
        """
        Resizes the image while maintaining the aspect ratio.

        image: PIL.Image, the image to resize.
        new_width: int, the new width for the image. Height is calculated based on aspect ratio.

        returns: PIL.Image, the resized image.
        """
        new_width *= self.detail_size
        (old_width, old_height) = image.size

        # ASCII Chars are usually twice as tall as they are wide
        aspect_ratio = old_height / (old_width * 2)  # Adjusting aspect ratio for ASCII

        new_height = int(aspect_ratio * new_width)
        return image.resize((new_width, new_height))

    def grayscale(self, image):
        """
        Converts the image to grayscale.

        image: PIL.Image, the image to convert to grayscale.

        returns: PIL.Image, the grayscale image.
        """
        return image.convert("L")

    def map_pixels_to_ascii(self, image):
        """
        Maps the grayscale image pixels to ASCII characters.

        image: PIL.Image, the grayscale image.

        returns: str, the ascii string representation of the image.
        """
        pixels = np.array(image)
        bucket_size = 256 // len(ASCII_CHARS)

        # map each pixel to an ascii character and join them into a single string
        ascii_str_list = [
            ASCII_CHARS[min(pixel_value // bucket_size, len(ASCII_CHARS) - 1)] for pixel_row in pixels for pixel_value
            in pixel_row
        ]

        return ''.join(ascii_str_list)


class AsciiArt:
    def __init__(self, image_processor: ImageProcessor):
        """
        Constructor for the AsciiArt class.

        image_processor: ImageProcessor, an instance of the ImageProcessor class.
        """
        self.image_processor = image_processor

    def generate_ascii_art(self):
        """
        Generates ascii art from the image.

        returns: str, the ascii art representation of the image.
        """
        image = self.image_processor.load_image()
        image = self.image_processor.resize_image(image)
        image = self.image_processor.grayscale(image)
        ascii_str = self.image_processor.map_pixels_to_ascii(image)

        # split the ascii_str into lines based on the width of the image
        return '\n'.join([ascii_str[i:i + image.width] for i in range(0, len(ascii_str), image.width)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert an image to ASCII art.")
    parser.add_argument("-i", "--image", type=str, required=True, help="Path to the image that will be used for the ASCII art.")
    parser.add_argument("-d", "--detail", type=int, default=1, help="Factor to scale the detail of the output ASCII art. Default is 1.")
    parser.add_argument("-c", "--copy", action="store_true", help="Copy the ASCII art to the clipboard after generation.")

    args = parser.parse_args()

    image_processor = ImageProcessor(args.image, detail_size=args.detail)
    ascii_art_instance = AsciiArt(image_processor)
    ascii_art = ascii_art_instance.generate_ascii_art()

    print(ascii_art)

    if args.copy:
        pyperclip.copy(ascii_art)
        print("ASCII art copied to clipboard.")
