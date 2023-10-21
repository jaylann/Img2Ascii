# ASCII Art Generator

ASCII Art Generator is a Python-based project that converts images to ASCII art. It uses the Python Imaging Library (PIL), numpy, and pyperclip to achieve this.

## Prerequisites

Make sure you have installed the following Python libraries:

1. Python Imaging Library (PIL)
2. numpy
3. pyperclip

You can install them with the following commands:

```bash
pip install pillow
pip install numpy
pip install pyperclip
```

Or you can install them using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

### As a Library

First, import the necessary classes from the script:

```python
from ascii_art import ImageProcessor, AsciiArt
```

Then, follow the example code to create instances of `ImageProcessor` and `AsciiArt`, and generate your ASCII art.

### As a Command-Line Tool

You can also use the script directly from the command line. Here's how you can do it:

```bash
python ascii_art.py -i path_to_your_image.jpg -d 2
```

Options:

- `-i, --image`: Path to the image that will be used for the ASCII art (required).
- `-d, --detail`: Factor to scale the detail of the output ASCII art. Default is 1.
- `-c, --copy`: Copy the ASCII art to the clipboard after generation.

## Example

Here is an example of how to use the code as a library:

```python
from ascii_art import ImageProcessor, AsciiArt

image_processor = ImageProcessor('sample.jpg', detail_size=2)
ascii_art_instance = AsciiArt(image_processor)
print(ascii_art_instance.generate_ascii_art())
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
