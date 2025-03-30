# Medical Image Processing Project
## Overview
This project demonstrates data engineering skills by processing the Kvasir and Kvasir-SEG datasets for polyp segmentation tasks. It includes data unpacking, loading, preprocessing, analysis, and visualization.
## Datasets
- **Kvasir**: Images of the GI tract with anatomical landmarks and pathological findings.
- **Kvasir-SEG**: 1000 polyp images with segmentation masks.

## Features
- Unpacks dataset archives (`kvasir-dataset.zip` and `kvasir-seg.zip`).
- Loads and preprocesses medical images (resize to 256x256, normalize).
- Analyzes dataset statistics (category counts, image sizes).
- Visualizes and saves image-mask pairs for Kvasir-SEG.
## Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd portfolio2