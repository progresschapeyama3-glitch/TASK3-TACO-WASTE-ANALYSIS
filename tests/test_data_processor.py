from src.data_processor import DataProcessor


def create_test_dataset():
    return {
        "images": [
            {"id": 1},
            {"id": 2},
            {"id": 3}
        ],
        "annotations": [
            {"id": 1, "category_id": 1},
            {"id": 2, "category_id": 1},
            {"id": 3, "category_id": 2}
        ],
        "categories": [
            {"id": 1, "name": "Cigarette"},
            {"id": 2, "name": "Bottle"}
        ]
    }


def test_image_count():
    processor = DataProcessor(create_test_dataset())
    assert processor.get_image_count() == 3


def test_annotation_count():
    processor = DataProcessor(create_test_dataset())
    assert processor.get_annotation_count() == 3


def test_category_count():
    processor = DataProcessor(create_test_dataset())
    assert processor.get_category_count() == 2


def test_category_counts():
    processor = DataProcessor(create_test_dataset())
    counts = processor.get_category_counts()

    assert counts[1] == 2
    assert counts[2] == 1