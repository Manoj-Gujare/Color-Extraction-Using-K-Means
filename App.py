import streamlit as st
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from PIL import Image, ImageDraw

def create_color_palette(image, n_clusters=5, palette_size=(300, 50)):
    # Resize image to reduce processing time
    resized_image = image.resize((150, 150))  # Resize to 150x150 pixels

    # Convert resized image to numpy array
    np_image = np.array(resized_image)

    # Reshape the image into a 2D array
    X = np_image.reshape(-1, 3)

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(X)

    # Function to create a color palette
    def generate_palette(dominant_colors, palette_size):
        # Create an image to display the colors
        palette = Image.new("RGB", palette_size)
        draw = ImageDraw.Draw(palette)

        # Calculate the width of each color swatch
        swatch_width = palette_size[0] // len(dominant_colors)

        # Draw each color as a rectangle on the palette
        for i, color in enumerate(dominant_colors):
            draw.rectangle([i * swatch_width, 0, (i + 1) * swatch_width, palette_size[1]], fill=tuple(color))

        return palette

    # Create and return the color palette image
    return generate_palette(kmeans.cluster_centers_.astype(int), palette_size)

def main():
    st.title("Color Palette Generator")

    # File uploader for image selection
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Generate palette button
        if st.button("Generate Palette"):
            # Generate and display the color palette
            palette_image = create_color_palette(image, n_clusters=5, palette_size=(300, 50))
            st.image(palette_image, caption="Color Palette", use_column_width=True)

if __name__ == "__main__":
    main()