import json
from pathlib import Path

class DatasetLoader:
    """
    Loads the TACO dataset annotations.
    Single Responsibility Principle:
    This class is responsible only for loading
    annotation data from the JSON file.
    """

    def __init__(self, annotation_file: str):
        self.annotation_file = Path(annotation_file)

    def load_annotations(self) -> dict:
        """Load the TACO annotations from JSON."""

        if not self.annotation_file.exists():
            raise FileNotFoundError(
                f"Annotation file not found: {self.annotation_file}"
            )
        with self.annotation_file.open("r", encoding="utf-8") as file:
            return json.load(file)