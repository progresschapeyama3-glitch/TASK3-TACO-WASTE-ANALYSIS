import streamlit as st
from pathlib import Path

from src.dataset_loader import DatasetLoader
from src.data_processor import DataProcessor


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

TACO_IMAGE_DIRECTORY = Path("data")
ANNOTATION_FILE = Path("data/annotations.json")


st.set_page_config(
    page_title="TACO Waste Analysis",
    page_icon="♻️",
    layout="wide"
)


# ---------------------------------------------------------
# Helper functions
# ---------------------------------------------------------

def find_taco_images(image_directory: Path) -> list[Path]:
    """
    Find JPG images inside the TACO dataset folders.
    """

    if not image_directory.exists():
        return []

    return sorted(image_directory.rglob("*.jpg"))


def get_image_number(image_path: Path) -> str:
    """
    Return the image filename without the extension.
    """

    return image_path.stem


# ---------------------------------------------------------
# Main application
# ---------------------------------------------------------

def main():
    """Run the TACO Waste Analysis dashboard."""

    st.title("♻️ TACO Waste Analysis Application")

    st.write(
        """
        This application processes the TACO litter dataset and
        presents useful information about waste images,
        annotations and categories.
        """
    )

    # -----------------------------------------------------
    # Load dataset
    # -----------------------------------------------------

    loader = DatasetLoader(str(ANNOTATION_FILE))
    dataset = loader.load_annotations()

    # -----------------------------------------------------
    # Process dataset
    # -----------------------------------------------------

    processor = DataProcessor(dataset)

    # -----------------------------------------------------
    # Dataset Overview
    # -----------------------------------------------------

    st.header("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Images",
        processor.get_image_count()
    )

    col2.metric(
        "Total Annotations",
        processor.get_annotation_count()
    )

    col3.metric(
        "Waste Categories",
        processor.get_category_count()
    )

    st.divider()

    # -----------------------------------------------------
    # Waste Category Analysis
    # -----------------------------------------------------

    st.header("Waste Category Analysis")

    category_counts = processor.get_category_counts()
    category_names = processor.get_category_names()

    readable_counts = {
        category_names.get(category_id, "Unknown"): count
        for category_id, count in category_counts.items()
    }

    sorted_categories = sorted(
        readable_counts.items(),
        key=lambda item: item[1],
        reverse=True
    )

    # -----------------------------------------------------
    # Category Selector
    # -----------------------------------------------------

    category_options = [
        category
        for category, count in sorted_categories
    ]

    selected_category = st.selectbox(
        "Select a waste category:",
        category_options
    )

    selected_count = readable_counts[selected_category]

    st.info(
        f"{selected_category} has {selected_count} annotations "
        "in the processed dataset."
    )

    # -----------------------------------------------------
    # Top 10 Waste Categories
    # -----------------------------------------------------

    st.subheader("Top 10 Waste Categories")

    top_10 = dict(sorted_categories[:10])

    st.bar_chart(top_10)

    # -----------------------------------------------------
    # Category Details
    # -----------------------------------------------------

    st.subheader("Category Details")

    table_data = {
        "Waste Category": [
            category
            for category, count in sorted_categories
        ],
        "Number of Annotations": [
            count
            for category, count in sorted_categories
        ]
    }

    st.dataframe(
        table_data,
        use_container_width=True
    )

    # -----------------------------------------------------
    # TACO Image Viewer
    # -----------------------------------------------------

    st.divider()

    st.header("🖼️ TACO Image Viewer")

    st.write(
        """
        Select an image from the downloaded TACO dataset
        to view it inside the application.
        """
    )

    taco_images = find_taco_images(TACO_IMAGE_DIRECTORY)

    if not taco_images:
        st.warning(
            "No TACO images were found. "
            "Please make sure the batch folders are inside "
            "the data folder."
        )
        return

    st.success(
        f"{len(taco_images)} TACO images found."
    )

    selected_image = st.selectbox(
        "Select a TACO image:",
        taco_images,
        format_func=lambda path: path.name
    )

    st.image(
        selected_image,
        caption=f"TACO image: {selected_image.name}",
        width="stretch"
    )

    st.write(
        f"**Selected image:** {get_image_number(selected_image)}"
    )


# ---------------------------------------------------------
# Application Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":
    main()