# Color Palette Generator using K-means

## Description
This project implements a Color Palette Generator using K-means clustering algorithm. The application allows users to upload an image, and then it extracts the dominant colors from the image using K-means clustering. It then generates and displays a color palette based on these dominant colors.

## Tools & Libraries
- Python (Version 3.x)
- Streamlit
- Matplotlib
- NumPy
- scikit-learn (sklearn)
- Pillow (PIL)

## Functionality
- Users can upload an image in JPG, PNG, or JPEG format.
- The uploaded image is displayed to the user.
- Upon clicking the "Generate Palette" button, the application extracts the dominant colors from the image using K-means clustering.
- It then generates a color palette based on these dominant colors and displays it to the user.

## Implementation Details
- The uploaded image is resized to reduce processing time.
- The K-means clustering algorithm is applied to the resized image to identify the dominant colors.
- The color palette is generated based on the dominant colors identified by K-means clustering.
- The color palette is displayed to the user alongside the uploaded image.

## Usage
To use the Color Palette Generator:
1. Ensure that the required libraries are installed (Streamlit, Matplotlib, NumPy, scikit-learn, Pillow).
2. Run the Python script containing the code.
3. Upload an image by clicking the "Choose an image..." button.
4. Once the image is displayed, click the "Generate Palette" button to generate the color palette.
5. The color palette will be displayed below the uploaded image.
