import shutil
from pathlib import Path


def organize_jpg_files():
    """Move JPG and JPEG files into a destination folder."""
    source_text = input("Enter the folder path containing images: ").strip().strip('"')
    source_folder = Path(source_text).expanduser()

    if not source_folder.exists() or not source_folder.is_dir():
        print("Error: The source folder does not exist or is not a folder.")
        return

    destination_text = input("Enter the destination folder path: ").strip().strip('"')
    destination_folder = Path(destination_text).expanduser()

    # Avoid moving files into the same folder being scanned.
    if source_folder.resolve() == destination_folder.resolve():
        print("Error: Source and destination folders must be different.")
        return

    destination_folder.mkdir(parents=True, exist_ok=True)

    image_files = [
        path for path in source_folder.iterdir()
        if path.is_file() and path.suffix.lower() in {".jpg", ".jpeg"}
    ]

    if not image_files:
        print("No JPG or JPEG files were found in the source folder.")
        return

    moved_count = 0
    skipped_count = 0

    for image_path in image_files:
        destination_path = destination_folder / image_path.name

        # Do not overwrite an existing file with the same name.
        if destination_path.exists():
            print(f"Skipped '{image_path.name}': a file with that name already exists.")
            skipped_count += 1
            continue

        try:
            shutil.move(str(image_path), str(destination_path))
            print(f"Moved: {image_path.name}")
            moved_count += 1
        except OSError as error:
            print(f"Could not move '{image_path.name}': {error}")

    print("\n" + "=" * 40)
    print("FILE ORGANIZATION SUMMARY")
    print("=" * 40)
    print(f"Files moved:   {moved_count}")
    print(f"Files skipped: {skipped_count}")
    print(f"Destination:   {destination_folder.resolve()}")


if __name__ == "__main__":
    organize_jpg_files()
