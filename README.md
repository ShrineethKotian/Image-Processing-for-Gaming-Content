# Image-Processing-for-Gaming-Content
A 3-part pipeline to make synthetic game images more realistic using ISP, Super-Resolution, and GAN discriminators. Improves color, detail, and realism with FID/KID evaluation against Cityscapes.

# CV Praktikum – Photorealism Enhancement Pipeline
This repository contains a modular pipeline to enhance photorealism in synthetic video game imagery (GTA5) using three core components:

1. Image Signal Processing (ISP)

2. Super-Resolution (SR)

3. Lightweight Discriminator Models for GANs

Each branch contains code and documentation for one component, developed by a different team member.

📦 Structure
The project is split into three parts:

1. Neural Image Signal Processing (ISP) for Photorealism
Author: Shrineeth Kotian
Lightweight hybrid ISP pipeline that includes white balance, color correction, adaptive gamma, CLAHE, NILUT, vignette, sharpening, etc.

2. Enhancing Game Visuals using Super-Resolution and Image Restoration
Author: Ganesh Gopalakrishna 
Evaluation of SR models like RealESRGAN, SwinIR, StableSR, and NAFNET using synthetic degradation tailored for gaming imagery.

3. Lightweight Discriminator Architectures for Realism-Guided GANs
Author: Aishwarya G. Rao 
Benchmarking of efficient GAN discriminators (MobileNetV3, Swin-T, ConvNeXt, VGG) suitable for low-compute photorealism.

⚙️ Installation
To run the notebooks:

'''pip install -r requirements.txt'''

```bash
  pip install -r requirements.txt
```
