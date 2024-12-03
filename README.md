# License-Plate-Recognition 🪪
a Python project that detects and reads license plates from vehicle images using computer vision and OCR. It extracts the license plate, applies text recognition, and logs the results with timestamps into a CSV file.

## Credits 🤖
[![Python ANPR with OpenCV and EasyOCR in 25 Minutes | Automatic Number Plate Recognition Tutorial](https://img.youtube.com/vi/NApYP_5wlKY&t=423s.jpg)](https://www.youtube.com/watch?v=NApYP_5wlKY&t=423s) - 
**Nicholas Renotte**.
The base code for this project was adapted from Nicholas Renotte. While the original concept and code were used as a foundation, several modifications were made to suit the specific functionality and features of this License plate Detection model.

## Demo 🎬

## The Code files: 📄
**anpr.py:** processes vehicle images to detect and read license plates using computer vision and OCR. It identifies the license plate region, extracts the text, annotates the image with the recognized plate number, and logs the results with timestamps into a CSV file.

## Functionality ⚙️

**Image Loading:** Loads the input image for processing using OpenCV.

**Grayscale Conversion:** Converts the image to grayscale for easier contour detection and processing.

**Edge Detection:** Applies bilateral filtering and Canny edge detection to identify edges in the image.

**Contour Detection:** Detects and filters contours to locate the rectangular region of the license plate.

**License Plate Extraction:** Masks and isolates the license plate region from the original image.

**Cropping:** Crops the license plate region for focused optical character recognition (OCR).

**OCR Processing:** Utilizes EasyOCR to read and extract text from the cropped license plate.

**Annotation:** Annotates the original image with the detected license plate text and highlights the plate.

**CSV Logging:** Records the detected license plate text with a timestamp in a CSV file.

**Error Handling:** Ensures graceful handling of missing files, unreadable images, or OCR failures.

**Visualization:** Displays intermediate processing stages, including grayscale, edges, and final annotations.

## Installation 💻
To run the anpr.py Number Plate Detection project, you'll need to install the following dependencies:

*pip install opencv-python==4.10.0.84*

*pip install matplotlib==3.7.2*

*pip install numpy==1.23.5*  

*pip install imutils==0.5.4*  

*pip install easyocr==1.7.2*  

*pip install pandas==2.0.3*  

## The Theory: 💡
Automatic Number Plate Recognition (ANPR) is a **computer vision and OCR-based approach** used to identify and extract text (license plate numbers) from images of vehicles. Here’s the theory behind the implementation in anpr.py:

**1. Image Preprocessing**
ANPR starts by preparing the input image to make it suitable for analysis. The key steps include:

  - **Grayscale Conversion:** grayscale simplifies the algorithm and reduces computational requirements. Consider training neural articles on RGB images of 10x10x3 pixels. The input layer will have 300 input nodes. On the other hand, the same neural network will need only 100 input nodes for grayscale images.

  - **Edge Detection:** Uses the Canny Edge Detector to highlight the boundaries in the image, such as the edges of a license plate as they are rectangular and have sharp edges, making them identifiable in edge-detected images.
