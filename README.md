# Computer Vision Praktikum Project, 2025 – Image Processing for Gaming Content
## University of Würzburg
A 3-part pipeline to make synthetic game images more realistic using ISP, Super-Resolution, and GAN discriminators. Improves color, detail, and realism with FID/KID evaluation against Cityscapes.

This repository contains a modular pipeline to enhance photorealism in synthetic video game imagery (GTA5) using three core components:

1. Image Signal Processing (ISP)

2. Super-Resolution (SR) and Image restoration

3. Lightweight Discriminator Models for GANs

Each branch contains code and documentation for one component, developed by a different team member.

## 📦 Structure
The project is split into three parts:

1. Neural Image Signal Processing (ISP) for Photorealism

Author: Shrineeth Kotian

Lightweight hybrid ISP pipeline that includes white balance, color correction, adaptive gamma, CLAHE, NILUT, vignette, sharpening, etc.

2. Enhancing Game Visuals using Super-Resolution and Image Restoration

Author: Ganesh Gopalakrishna 

Evaluation of SR models like RealESRGAN, SwinIR and StableSR, and Image restoration with NAFNET using synthetic degradation tailored for gaming imagery.

3. Lightweight Discriminator Architectures for Realism-Guided GANs

Author: Aishwarya Rao 

Benchmarking of efficient GAN discriminators (MobileNetV3, Swin-T, ConvNeXt, VGG) suitable for low-compute photorealism.

## ⚙ Installation

To run the notebooks:


```bash
  pip install -r requirements.txt
```

If using NILUT:

- Download pretrained NILUT weights from the official [NILUT GitHub repository](https://github.com/mv-lab/nilut)

- Place them under ./models/weights/nilutx3style.pt or update the path in your code

For FID/KID metrics:
```bash
pip install clean-fid
```

Ensure that datasets (e.g., Playing for Data, Cityscapes) are downloaded and placed in the expected folders.

## 🚀 Running the Pipelines

Each team member’s code is self-contained in their branch:

- branch: isp-pipeline → Shrineeth

- branch: super-resolution → Ganesh

- branch: gan-discriminators → Aishwarya

To test any pipeline:

1. Switch to the respective branch.

2. Open the .ipynb notebook file.

3. Follow the in-notebook instructions (dataset paths, parameters, model loading).

4. Output will be saved to /kaggle/working/ or configured path.

## 🗃 Dataset Used

We use the GTA5 subset from the Kaggle dataset: [Playing For Data (GTA5)](https://www.kaggle.com/datasets/aishwaryagrao/playing-for-data)

To use this dataset:

1. Go to the above link.
2. Download the dataset (you may need a Kaggle account).
3. Extract the images and place them inside a folder like `dataset/` within the ISP pipeline directory.
4. The folder structure should look like:
```bash
dataset/
└── 01_images/
    └── images/
        ├── 00001.png
        ├── 00002.png
        └── ...
```

## 🧪 Evaluation

- Evaluation is performed using FID and KID metrics with Cityscapes as the ground truth.

- Consistent folder structure and image counts are used for fair comparison with previous baselines (CUT, MUNIT, Color Transfer).

- Example:

```bash
FID (Raw GTA): ~120   |  KID (Raw GTA): >100
FID (Final ISP): 53.54  |   KID (Final ISP): 60.97
```

## 👥 Authors

- Shrineeth Kotian – shrineeth.kotian@stud-mail.uni-wuerzburg.de

- Ganesh Gopalakrishna – ganesh-maudghalya.hassan-gopalakrishna@stud-mail.uni-wuerzburg.de

- Aishwarya G. Rao – aishwarya.rao@stud-mail.uni-wuerzburg.de

## 📃 [Final Report (Google Drive)](https://drive.google.com/file/d/1TEPzNhwM1OxkG3kbKZwBEA2nVXaVkgjZ/view?usp=sharing)

## 📄 References:

[1] Salmi et al. “Generative Adversarial Shaders for Real-Time Realism Enhancement.” ArXiv, 2023.

[2] NILUT: https://github.com/mv-lab/nilut

[3] Playing for Data: Synthetic dataset from GTA5

[4] Cityscapes Dataset for Real-World Benchmarking
