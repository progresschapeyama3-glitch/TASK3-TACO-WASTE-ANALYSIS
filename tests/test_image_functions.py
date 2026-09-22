from main import find_taco_images


def test_find_taco_images(tmp_path):
    image_folder = tmp_path / "batch_1"
    image_folder.mkdir()

    image1 = image_folder / "image1.jpg"
    image2 = image_folder / "image2.jpg"

    image1.touch()
    image2.touch()

    result = find_taco_images(tmp_path)

    assert len(result) == 2


def test_missing_image_directory(tmp_path):
    missing_folder = tmp_path / "does_not_exist"

    result = find_taco_images(missing_folder)

    assert result == []
