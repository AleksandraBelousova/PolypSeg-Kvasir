import os
import zipfile
from pathlib import Path
def unpack_archives() -> None:
    base_dir = Path("C:/Users/User-pc/Desktop/python/portfolio2")
    data_dir = base_dir / "data"
    archives = [
        base_dir / "kvasir-dataset.zip",
        base_dir / "kvasir-seg.zip"
    ]
    data_dir.mkdir(exist_ok=True)
    for archive in archives:
        if archive.exists():
            print(f"Unpacking {archive.name}...")
            with zipfile.ZipFile(archive, 'r') as zip_ref:
                zip_ref.extractall(data_dir)
            print(f"Successfully unpacked {archive.name} into {data_dir}")
        else:
            print(f"Error: {archive.name} not found")
if __name__ == "__main__":
    unpack_archives()