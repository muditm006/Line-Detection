# Line Detection with Direction Indicator

This repository contains a Python program designed to detect lines in an image, identify key triangular regions, and overlay directional arrows to indicate the direction of travel. The program uses OpenCV and NumPy for advanced image processing and visualization.

## Features

- **Line Detection**  
  Uses Hough Line Transform to detect lines in the input image.

- **Triangular Region Selection**  
  Dynamically selects triangular regions in the image based on predefined points for different views (`front.jpg`, `left.jpg`, `right.jpg`).

- **Directional Arrow Overlay**  
  Calculates the center of the triangle and overlays an arrow pointing toward a specified direction.

- **Side-by-Side Visualization**  
  Displays the processed image with detected lines alongside the original image with directional arrows.

## File Descriptions

- **Lines.py**  
  The main script that:
  - Processes an input image to detect lines.
  - Selects a triangular region based on the input image type.
  - Calculates the center of the triangle and overlays a directional arrow.
  - Displays a side-by-side comparison of the processed image and the original image with annotations.

- **README.md**  
  Provides an overview of the project, its features, file descriptions, and usage instructions.

## How to Use

1. Clone this repository to your local machine:
git clone https://github.com/muditm006/Line-Detection.git
cd Line-Detection
2. Install the required Python libraries:
pip install numpy opencv-python

3. Run the program with an input image:
python Lines.py --image path/to/your/image.jpg
4. View the output:
- The left side will display the processed image with detected lines.
- The right side will display the original image with a directional arrow overlay.

5. Modify or extend functionality by editing `Lines.py` as needed.

## Libraries Used

- **OpenCV**: For line detection, region masking, and visualization.
- **NumPy**: For numerical operations and array manipulations.
- **argparse**: For command-line argument parsing.

## Notes

- Ensure that your input images match one of the predefined types (`front.jpg`, `left.jpg`, `right.jpg`) for accurate region selection.
- The program dynamically calculates triangle centers and overlays arrows based on these points.

This project demonstrates advanced line detection and visualization techniques using Python's OpenCV library.
