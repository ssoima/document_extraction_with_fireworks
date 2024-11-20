import streamlit as st
from PIL import Image

from process_image import process_image
from models import DriverLicense, Passport, DocumentType, DocumentTypeEnum, ModelOptionsEnum
from prompts import DRIVER_LICENSE_DATA_EXTRACTION_PROMPT, PASSPORT_DATA_EXTRACTION_PROMPT
from utils import binary_stream_to_base64


# Helper function to map Enum to shorter names for display
def get_display_value(option: ModelOptionsEnum) -> str:
    return option.name

def classify_document_type(image_base64: str, model: ModelOptionsEnum) -> DocumentTypeEnum:
    return process_image(
        response_model=DocumentType,
        prompt="Identify the type of document in the image",
        image_base64=image_base64,
        model=model.technical_value
    ).document_type


def extract_license_data(image_base64: str, model: ModelOptionsEnum):
    return process_image(
        response_model=DriverLicense,
        prompt=DRIVER_LICENSE_DATA_EXTRACTION_PROMPT,
        image_base64=image_base64,
        model=model.technical_value
    )


def extract_passport_data(image_base64: str, model: ModelOptionsEnum):
    return process_image(
        response_model=Passport,
        prompt=PASSPORT_DATA_EXTRACTION_PROMPT,
        image_base64=image_base64,
        model=model.technical_value
    )


# Streamlit App
st.set_page_config(layout="wide")  # Set wide page layout

# CSS for custom padding and smaller image
st.markdown(
    """
    <style>
    .main {
        padding-top: 20px;
        padding-right: 50px;
        padding-left: 50px;
    }
    .block-container {
        padding: 1rem 2rem;
    }
    img {
        max-width: 400px;
        height: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("License and Passport Data Extractor")

# Layout: Two Wider Columns
left_column, right_column = st.columns([1.5, 4])  # Proportions for left (1.5) and right (4)

# Left-hand column for model selection
with left_column:
    st.header("Model Selection")
    doc_type_classification_model = st.selectbox(
        "Model for Document Type Identification",
        options=list(ModelOptionsEnum),
        format_func=get_display_value
    )
    data_extraction_model = st.selectbox(
        "Model for Data Extraction",
        options=list(ModelOptionsEnum),
        format_func=get_display_value
    )

# Right-hand column for functionality
with (right_column):
    # File uploader
    st.header("Document Analyzer")
    uploaded_file = st.file_uploader("Upload an image of a driver's license or passport", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Display uploaded image (smaller size)
        image = Image.open(uploaded_file)
        image_base64 = binary_stream_to_base64(image)
        st.image(image, caption="Uploaded Image (Smaller)", use_container_width=False)

        # Classify document type
        with st.spinner("Processing image..."):
            document_type = classify_document_type(image_base64, doc_type_classification_model)
            print("Document Type:", document_type)

        st.subheader("Document Type")
        st.text(document_type.value)

        # Extract data based on document type
        with st.spinner("Extracting data..."):
            if document_type == DocumentTypeEnum.driver_license:
                extracted_data = extract_license_data(image_base64, data_extraction_model)
            elif document_type == DocumentTypeEnum.passport:
                extracted_data = extract_passport_data(image_base64, data_extraction_model)
            else:
                st.error("Document type not recognized.")
                st.stop()

        st.subheader("Extracted Data")
        st.json(extracted_data.dict())