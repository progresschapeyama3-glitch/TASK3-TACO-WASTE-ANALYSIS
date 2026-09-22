from collections import Counter
class DataProcessor:
    """Processes TACO dataset information.Single Responsibility Principle:
    This class processes dataset information
    and calculates useful statistics."""
    def __init__(self, dataset: dict):
        self.dataset = dataset
    def get_image_count(self) -> int:
        """Return the number of images in the dataset."""
        return len(self.dataset.get("images", []))
    def get_annotation_count(self) -> int:
        """Return the number of annotations."""
        return len(self.dataset.get("annotations", []))
    def get_category_count(self) -> int:
        """Return the number of waste categories."""
        return len(self.dataset.get("categories", []))
    def get_category_counts(self) -> Counter:
        """Count annotations for each category."""
        return Counter(
            annotation["category_id"]
            for annotation in self.dataset.get("annotations", [])
        )
    def get_category_names(self) -> dict:
        """Create a category ID to category name mapping."""
        return {
            category["id"]: category["name"]
            for category in self.dataset.get("categories", [])
        }

