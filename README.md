# DPT_Project


# Depth Estimation Web App

## Overview

This project demonstrates an interactive web application for depth estimation from images using advanced AI techniques. Users can upload their own images and obtain instant depth maps, showcasing the power of computer vision. The app leverages pre-trained models provided by Intel and utilizes various powerful tools and libraries.

## Features

- **Image Upload**: Users can upload images in various formats (JPG, JPEG, PNG).
- **Depth Estimation**: Generates a depth map for the uploaded image using Intel's pre-trained DPT model.
- **Interactive Web Interface**: Built with Streamlit, providing an easy-to-use interface.
- **Real-time Processing**: Instantaneous processing and display of depth estimation results.

## Tools and Technologies

- **[Streamlit](https://streamlit.io/)**: For creating the interactive web interface.
- **[Hugging Face Transformers](https://huggingface.co/transformers/)**: Using Intel's DPT model for depth estimation.
- **[Intel](https://www.intel.com)**: Providing pre-trained models optimized for performance.
- **[PyTorch](https://pytorch.org/)**: For handling deep learning model operations.
- **[Pillow](https://python-pillow.org/)**: For image processing tasks.

## Applications

- **Autonomous Driving**: Enhances navigation systems with accurate depth data.
- **Augmented Reality (AR)**: Improves the overlay of virtual objects in real-world scenes.
- **Robotics**: Assists in the navigation and interaction of robots with their environments.
- **Photography**: Enables advanced photo editing techniques such as background blurring and depth-based enhancements.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Josoriop9/DPT_Project
    cd depth-estimation-web-app
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install xyz
    ```

## Running the Application

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:xyz01`).

## Usage

1. Upload an image using the file uploader in the web interface.
2. Wait for the app to process the image and display the depth estimation result.
3. The original image and its corresponding depth map will be displayed side by side.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


## Acknowledgments

- Thanks to Intel for providing the pre-trained models.
- Inspired by the work of Robert Chesebrough on depth estimation.

---

Feel free to modify and expand upon this template to better fit your project's specifics and personal preferences.

