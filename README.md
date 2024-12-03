# License-Plate-Recognition 🪪
a Python project that detects and reads license plates from vehicle images using computer vision and OCR. It extracts the license plate, applies text recognition, and logs the results with timestamps into a CSV file.

## Credits 🤖
[![Python ANPR with OpenCV and EasyOCR in 25 Minutes | Automatic Number Plate Recognition Tutorial](https://img.youtube.com/vi/NApYP_5wlKY&t=423s.jpg)](https://www.youtube.com/watch?v=NApYP_5wlKY&t=423s) - 
**Nicholas Renotte**.
The base code for this project was adapted from Nicholas Renotte. While the original concept and code were used as a foundation, several modifications were made to suit the specific functionality and features of this License plate Detection model.

## Demo 🎬

https://github.com/user-attachments/assets/c65a7e60-4a6a-4594-909a-f8721ca48bcc

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

### 1. Image Preprocessing
ANPR starts by preparing the input image to make it suitable for analysis. The key steps include:
  - **Grayscale Conversion:** grayscale simplifies the algorithm and reduces computational requirements. Consider training neural articles on RGB images of 10x10x3 pixels. The input layer will have 300 input nodes. On the other hand, the same neural network will need only 100 input nodes for grayscale images.

  ![image](https://github.com/user-attachments/assets/6c61e7e1-53e0-4096-8884-ae411b7b887c)
    
  - **Edge Detection:** Uses the Canny Edge Detector to highlight the boundaries in the image, such as the edges of a license plate as they are rectangular and have sharp edges, making them identifiable in edge-detected images.

  ![image](https://github.com/user-attachments/assets/7df66b81-75d3-4318-b9f1-e0a68bb3dce2)

### 2. Contour Detection
  - Contours are extracted to identify the region containing the license plate. Locate and sort the largest contours by area. Approximate each contour’s shape to check if it resembles a rectangle (four sides).

    ![image](https://github.com/user-attachments/assets/ec78f313-63a3-491c-9ba1-7ac81760bf3e)

### 3. Masking and Region of Interest (ROI)
  - After identifying the license plate contour, the region is extracted using masking.
  - **Masking:** A binary mask highlights the area of interest (the license plate) while removing the background (the unnecessary detail).
  - **Bitwise AND Operation:** Combines the original image with the mask to retain only the license plate region.

  ![image](https://github.com/user-attachments/assets/48011cbe-7b4b-49dc-ba5f-9ac799bae509)

### 4. Optical Character Recognition (OCR)
  - OCR translates the cropped image of the license plate into text using **EasyOCR**.

  - this output tells us the coordinates of the number plate, the predicted text, and the confidence value of the predicted text:
  - 
    ![image](https://github.com/user-attachments/assets/ffc94a67-2a7f-4584-ad37-98341fd0f738)

  - this is the basic idea with coordinates as **[x, y]**:
  - 
    ![image](https://github.com/user-attachments/assets/d27fe28d-dc18-436b-9304-dfe656adcaeb)


  - **EasyOCR** applies a neural network to recognize and extract alphanumeric characters from images. It is trained on datasets containing various fonts and styles, enabling robust text recognition even under challenging conditions (blurry images, uneven lighting, etc.).

### 5. Data Annotation and Saving
  - **Annotation:** The recognized text (license plate number) is overlaid on the original image for visualization.
  - **Data Logging:** Recognized license plate data is saved to a CSV file with timestamps for record-keeping.

  ![image](https://github.com/user-attachments/assets/e65effd9-b296-4104-94b6-a742e2104c24)

## Limitations: ⚠️
In certain scenarios, such as when the text is unclear or EasyOCR misinterprets characters (e.g., recognizing '8' as 'B'), the accuracy may be affected, leading to potential mismatches with the actual license plates.

**unclear text:** The camera captured the text at an angle, making it appear unclear.

https://github.com/user-attachments/assets/66aafa1b-7864-4257-b329-e2927f671ac4

**misinterpreted text:** the '8' is recognised as a 'B'

https://github.com/user-attachments/assets/50f2309b-76fd-4032-85ce-9eb9cbd730b4


