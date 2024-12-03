import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr
import pandas as pd
import os

def read_image(file_path):
    img = cv2.imread(file_path)
    if img is None: # Check if the image was loaded correctly
        raise ValueError(f"Failed to load image from {file_path}")
    return img

def preprocess_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        # Convert the image to grayscale
    plt.title("Grayscale Image")
    plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
    plt.show()
    return gray

def detect_edges(gray):
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17)     # Apply bilateral filter to reduce noise
    edged = cv2.Canny(bfilter, 30, 200)                 # Perform Canny edge detection
    plt.title("Edge Detection")
    plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
    plt.show()
    return edged

def find_license_plate_contour(edged):
    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)                             # Grab the contours using imutils
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]     # Sort contours by area and keep the largest 10

    location = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)    # Approximate the contour to a polygon
        if len(approx) == 4:                            # Check if the polygon has 4 sides (license plate is rectangular)
            location = approx                           # If it's a rectangle, store the location of the license plate
            break
    return location

def extract_license_plate(img, gray, location):
    mask = np.zeros(gray.shape, np.uint8)                       # Create a blank mask with the same dimensions as the grayscale image
    new_image = cv2.drawContours(mask, [location], 0,255, -1)   # Draw the license plate contour on the mask  
    new_image =  cv2.bitwise_and(img, img, mask=mask)           # Use bitwise AND to extract the license plate region from the image
    plt.title("Extracted License Plate")
    plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
    plt.show()
    return mask, new_image

def crop_license_plate(gray, mask):
    (x,y) = np.where(mask==255)                     # Get the coordinates of the pixels where the mask is white
    (x1, y1) = (np.min(x), np.min(y))               # Get the minimum x and y coordinates
    (x2, y2) = (np.max(x), np.max(y))               # Get the maximum x and y coordinates
    cropped_image = gray[x1:x2+1, y1:y2+1]          # Crop the image based on these coordinates
    plt.title("Cropped License Plate")
    plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
    plt.show()
    return cropped_image

def perform_ocr(cropped_image):
    reader = easyocr.Reader(['en'])                 # Initialize the EasyOCR reader for English
    result = reader.readtext(cropped_image)         # Perform OCR on the cropped image
    print(result)
    return result

def annotate_image(img, location, text):
    font = cv2.FONT_HERSHEY_SIMPLEX 
    annotated_img = cv2.putText(img, text=text, org=(location[0][0][0], location[1][0][1]+60),  # Put the OCR text on the image
                                fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
    annotated_img = cv2.rectangle(img, tuple(location[0][0]), tuple(location[2][0]), (0,255,0),3) # Draw a rectangle around the license plate
    plt.title("Annotated Image")
    plt.imshow(cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB))
    plt.show()

def save_to_csv(log_file, data, refresh=False):
    if refresh or not os.path.exists(log_file): # Check if we need to refresh the CSV or if it doesn't exist
        df = pd.DataFrame(columns=["Timestamp", "License Plate"])
        df.to_csv(log_file, index=False)

    if data is None: # If no OCR result, don't add anything
        return
    
    df = pd.read_csv(log_file)
    timestamp = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S") # Get the current timestamp excluding microseconds
    new_row = {"Timestamp": timestamp, "License Plate": data}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(log_file, index=False)

def main():
    file_path = 'image3.jpg'
    log_file = 'license_plate_log.csv'

    save_to_csv(log_file, None, refresh=True) # Refresh or initialize the CSV file
    img = read_image(file_path)
    gray = preprocess_image(img)
    edged = detect_edges(gray)
    location = find_license_plate_contour(edged)
    # print(location)
    if location is not None: # If a license plate contour is found
        mask, _ = extract_license_plate(img, gray, location)
        cropped_image = crop_license_plate(gray, mask)
        result = perform_ocr(cropped_image)
        if result: # If OCR result is found
            text = result[0][-2]
            annotate_image(img, location, text)
            save_to_csv(log_file, text)

if __name__ == "__main__":
    main()