import logging
from pathlib import Path
import cv2
import numpy as np
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def load_data(data_dir: str) -> tuple[dict, list, list]:
    kvasir_path = Path(data_dir) / "kvasir-dataset"
    kvasir_data = {folder.name: [cv2.imread(str(img)) for img in folder.glob("*.jpg")]
                   for folder in kvasir_path.iterdir() if folder.is_dir()}

    seg_img_dir = Path(data_dir) / "kvasir-seg" / "images"
    seg_mask_dir = Path(data_dir) / "kvasir-seg" / "masks"
    seg_images = [cv2.imread(str(img)) for img in sorted(seg_img_dir.glob("*.jpg"))]
    seg_masks = [cv2.imread(str(mask), cv2.IMREAD_GRAYSCALE) for mask in sorted(seg_mask_dir.glob("*.jpg"))]

    return kvasir_data, seg_images, seg_masks

def preprocess(image: np.ndarray, target_size: tuple = (256, 256)) -> np.ndarray:
    return cv2.resize(image, target_size, interpolation=cv2.INTER_AREA) / 255.0

def visualize_and_save(images: list, masks: list, output_dir: Path, num_samples: int = 3) -> None:
    output_dir.mkdir(exist_ok=True)
    for i in range(min(num_samples, len(images))):
        plt.figure(figsize=(8, 4))
        plt.subplot(1, 2, 1)
        plt.imshow(images[i])
        plt.title(f"Sample {i+1} - Image")
        plt.axis("off")
        plt.subplot(1, 2, 2)
        plt.imshow(masks[i], cmap="gray")
        plt.title(f"Sample {i+1} - Mask")
        plt.axis("off")
        plt.savefig(output_dir / f"sample_{i+1}.png")
        plt.show()

def analyze_data(kvasir_data: dict, seg_images: list) -> None:
    logger.info("Kvasir dataset statistics:")
    for category, images in kvasir_data.items():
        logger.info(f"Category '{category}': {len(images)} images")

    sizes = [img.shape[:2] for img in seg_images]
    unique_sizes = set(sizes)
    logger.info(f"Kvasir-SEG unique image sizes: {unique_sizes}")

def main() -> None:
    logger.info("Loading data")
    kvasir_data, seg_images, seg_masks = load_data("data")
    logger.info(f"Kvasir categories: {len(kvasir_data)}, Kvasir-SEG pairs: {len(seg_images)}")

    logger.info("Analyzing data")
    analyze_data(kvasir_data, seg_images)

    logger.info("Preprocessing Kvasir-SEG data")
    seg_images_proc = [preprocess(img) for img in seg_images]
    seg_masks_proc = [preprocess(mask) for mask in seg_masks]

    logger.info("Visualizing and saving samples")
    output_dir = Path("output")
    visualize_and_save(seg_images_proc, seg_masks_proc, output_dir)

if __name__ == "__main__":
    main()