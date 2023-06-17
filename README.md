# ASCII Art Generator

ASCII Art Generator is a Python-based project which converts images to ASCII art. It uses the Python Imaging Library (PIL) and numpy to achieve this. 

## Prerequisites

Make sure you have installed the following Python libraries:

1. Python Imaging Library (PIL)
2. numpy

You can install them with the following commands:

```bash
pip install pillow
pip install numpy
```

## Usage

First, import the necessary classes from the script:

```python
from ascii_art import ImageProcessor, AsciiArt
```

Then, create an instance of the `ImageProcessor` class with the path to your image file and your desired detail size as arguments. The detail size affects the level of detail of the resulting ASCII art. A higher value will result in more detail:

```python
image_processor = ImageProcessor('path_to_your_image.jpg', detail_size=2)
```

Next, create an instance of the `AsciiArt` class with your `ImageProcessor` instance as an argument:

```python
ascii_art = AsciiArt(image_processor)
```

Finally, call the `generate_ascii_art` method on your `AsciiArt` instance to generate your ASCII art:

```python
print(ascii_art.generate_ascii_art())
```

This will print the ASCII art representation of your image to the console.


## Example

Here is an example of how to use the code:

```python
from ascii_art import ImageProcessor, AsciiArt

image_processor = ImageProcessor('sample.jpg', detail_size=2)
ascii_art = AsciiArt(image_processor)
print(ascii_art.generate_ascii_art())
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
