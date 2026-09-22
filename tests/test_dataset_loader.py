import json
import pytest

from src.dataset_loader import DatasetLoader


def test_load_annotations(tmp_path):
    data = {
        "images": [{"id": 1}],
        "annotations": [{"id": 1, "category_id": 1}],
        "categories": [{"id": 1, "name": "Cigarette"}]
    }

    file_path = tmp_path / "annotations.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file)

    loader = DatasetLoader(str(file_path))
    result = loader.load_annotations()

    assert result == data


def test_missing_annotation_file():
    loader = DatasetLoader("missing_annotations.json")

    with pytest.raises(FileNotFoundError):
        loader.load_annotations()
