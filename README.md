# Python Project: License and Passport Data Extractor

## Overview

This project is a Streamlit application that allows users to upload images of driver's licenses or passports and extract relevant data from them using machine learning models.

## Features

- **Document Type Classification**: Identifies whether the uploaded document is a driver's license or a passport.
- **Data Extraction**: Extracts detailed information from the identified document type.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/pythonproject.git
    cd pythonproject
    ```

2. **Install dependencies**:
    ```sh
    poetry install
    ```

3. **Set up environment variables**:
    Create a `.env` file in the project root and add your Fireworks API key:
    ```env
    FIREWORKS_API_KEY=your_fireworks_api_key
    ```

## Usage

1. **Run the Streamlit app**:
    ```sh
    streamlit run streamlit_app.py
    ```

2. **Upload an image**:
    - Upload an image of a driver's license or passport.
    - The app will classify the document type and extract relevant data.

## Project Structure

- `streamlit_app.py`: Main Streamlit application file.
- `models.py`: Contains Pydantic models for driver's license, passport, and document type enums.
- `prompts.py`: Contains prompts for data extraction.
- `process_image.py`: Handles the interaction with the Fireworks API for image processing.
- `utils.py`: Utility functions for image preprocessing and encoding.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.