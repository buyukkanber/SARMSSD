# SARMSSD 
SARMSSD (SAR Multi-Scale Ship Detection) Dataset
<img width="1451" height="474" alt="image" src="https://github.com/user-attachments/assets/b6cbb20b-d4c7-426a-897f-524086377598" />

This repository provides the implementation of **deep learning-based ship detection in SAR imagery** using the **YOLO11** model, associated with our research paper **"Impact of Data Enhancement Methods on Ship Detection Using YOLO11 in SAR Imagery"** which we present in Machine Intelligence for GeoAnalytics and Remote Sensing (MIGARS 2025) International Conference. The study evaluates the effects of **image denoising** and **data augmentation** techniques on detection performance using a newly constructed dataset, **SARMSSD**, which combines three open-source SAR datasets (**SSDD, HRSID, and SRSDD**).

Accesss our paper --> [**https://doi.org/10.1109/MIGARS67156.2025.11231948**](https://doi.org/10.1109/MIGARS67156.2025.11231948)

## **Dataset Details**

- **Number of Total Images**: 7,430
- **Number of Total Ship Instances**: 22,195
- **Spatial Resolution**: Ranges from 0.5m to 15m
- **Image Resolution**: Varies between 300x300, 500x500, 800x800 and 1024x1024 pixels
- **Annotation Format**: YOLO
- **Annotation Style**: HBB (Horizontal Bounding Box)

Download --> [**SARMSSD Dataset**](https://drive.google.com/file/d/1zEDhNNlx4fXztBdGU3W3xXMQeXLW5bhg/view?usp=drive_link) 


## Impact of Data Enhancement Methods on Ship Detection Using YOLO11 in SAR Imagery

Ship detection in **synthetic aperture radar (SAR) imagery** is critical for **maritime surveillance, security, and environmental monitoring**. However, SAR images often contain **speckle noise and complex backgrounds**, affecting detection accuracy. 

This project explores:

**<details close><summary>Data Collection and Processing</summary>**

<img width="1654" height="543" alt="image" src="https://github.com/user-attachments/assets/9a0e6b88-269f-4173-8994-2d2b185a9b51" />


The **SARMSSD dataset** was constracted by merging the following publicly available SAR datasets:
- **[SSDD](https://github.com/TianwenZhang0825/Official-SSDD)**: 1,160 SAR images (obtained from RadarSat-2, TerraSAR-X and Sentinel-1 satellites) with 2,358 ship instances, having resolutions from 300x300 to 500x500 pixels and spatial resolutions ranging from 1m to 15m. This dataset has the PascalVOC annotation format, it has been converted to YOLO annotation format with [voc2yolo.py](https://github.com/buyukkanber/SARMSSD/blob/main/voc2yolo.py)
- **[HRSID](https://github.com/chaozhong2010/HRSID)**: 5,604 SAR images (obtained from Sentinel-1B, TerraSAR-X, and TanDEM-X satellites) with 16,951 ship instances, featuring a fixed resolution of 800x800 pixels and spatial resolutions between 0.5m and 3m. This dataset has the COCO annotation format, it has been converted to YOLO annotation format with [coco2yolo.py](https://github.com/buyukkanber/SARMSSD/blob/main/coco2yolo.py)
- **[SRSDD](https://github.com/HeuristicLU/SRSDD-V1.0)**: 666 SAR images (obtained from Chinese Gaofen-3 satellite) with 2,886 ship instances, all at 1024x1024 pixels with a spatial resolution of 1m. This dataset has the DOTA Oriented Bounding Box(OBB) annotation format, it has been converted to YOLO annotation format with [obb2hbb.py](https://github.com/buyukkanber/SARMSSD/blob/main/obb2hbb.py)
</details>

**<details close><summary>Noise Reduction Techniques</summary>**

To improve the quality of SAR images and reduce noise in the SARMSSD dataset, three enhancement techniques have been applied: Median filtering with 5x5 window [median.py](https://github.com/buyukkanber/SARMSSD/blob/main/median.py), BM3D method with sigma_psd set to 0.1 [apply_bm3d.py](https://github.com/buyukkanber/SARMSSD/blob/main/apply_bm3d.py), and a deep learning-based SAR-CAM method implemented in [test_sar-cam_sarmssd.ipynb](https://github.com/buyukkanber/SARMSSD/blob/main/test_sar-cam_sarmssd.ipynb) with utilizing our trained weight [SAR-CAM_best.pth](https://drive.google.com/file/d/18EveA4_66du_nwGkyouzFJ3MlS1i1jyv/view?usp=drive_link). These image processing methods yielded three enhanced variants of the original dataset which you can access them below:

Download --> [**SARMSSD-Median**](https://drive.google.com/file/d/1IgAjZf087W5CU1YwQRicek0jWKPBN0B7/view?usp=drive_link) Dataset 

Download --> [**SARMSSD-BM3D**](https://drive.google.com/file/d/1fQ0udsSA_DimltkUY_G3ggdvpVa6mtZU/view?usp=drive_link) Dataset

Download --> [**SARMSSD-SAR-CAM**](https://drive.google.com/file/d/1UywwOEqUApOnpCi1Ej2ijw504ipvVrjV/view?usp=drive_link) Dataset


</details>

**<details open><summary>YOLO11 Deep Learninig Experiments</summary>** 

Training and evaluation the **4 SARMSSD** datasets on YOLO11 algorithm & Comparing performance results.</details>

| Model                                                                                       | Dataset         | size<br><sup>(pixels) | Precision | Recall | mAP<sup>test<br>0.50 | mAP<sup>test<br>0.50:0.95 | params<br><sup>(M) |
| --------------------------------------------------------------------------------------------|-----------------|-----------------------|-----------|--------|----------------------|---------------------------|--------------------|
| [YOLO11x](https://github.com/buyukkanber/SARMSSD/releases/download/v1.0.0/sarmssd_yolo11x.pt)        | SARMSSD         |  640                  | 0.935     | 0.829  | 0.909                | 0.764                     | 56.9               | 
| [YOLO11x](https://github.com/buyukkanber/SARMSSD/releases/download/v1.0.0/sarmssd-median_yolo11x.pt)        | SARMSSD-Median  |  640                  | 0.938     | 0.824  | 0.911                | 0.718                     | 56.9               |
| [YOLO11x](https://github.com/buyukkanber/SARMSSD/releases/download/v1.0.0/sarmssd-bm3d_yolo11x.pt)        | SARMSSD-BM3D    |  640                  | 0.936     | 0.812  | 0.902                | 0.737                     | 56.9               | 
| [YOLO11x](https://github.com/buyukkanber/SARMSSD/releases/download/v1.0.0/sarmssd-sar-cam_yolo11x.pt)        | SARMSSD-SAR-CAM |  640                  | 0.950     | 0.815  | 0.908                | 0.770                     | 56.9               |

**<details open><summary>Data Augmentation Experiments:</summary>**

Mosaic, scale, and flip augmentations aplplied through **SARMSSD-SAR-CAM** dataset trainings to further improve ship detection accuracy.</details>


| Model                                                                                       |  Augmentation     | size<br><sup>(pixels) | Precision | Recall | mAP<sup>test<br>0.50 | mAP<sup>test<br>0.50:0.95 | params<br><sup>(M) |
| --------------------------------------------------------------------------------------------|--------------------|-----------|-----------|--------|----------------------|---------------------------|--------------------|
| YOLO11x       |      scale                 |  640       | 0.924 | 0.881 | 0.942 | 0.739 |56.9               | 
| YOLO11x       |      flip(lr) left-right   |  640       | 0.944 | 0.839 | 0.919 | 0.772 |56.9               | 
| [YOLO11x](https://github.com/buyukkanber/SARMSSD/releases/download/v1.0.0/sarmssd-sar-cam_yolo11x_aug.pt)    |      mosaic                |  640       | 0.951 | 0.881 | 0.945 | **0.788** |56.9               | 
| YOLO11x       |      mosaic, flip(lr)      |  640       | 0.922 | 0.888 | 0.940 | 0.754 |56.9               | 
| YOLO11x       |      scale, flip(lr)       |  640       | 0.921 | 0.869 | 0.939 | 0.711 | 56.9              | 
| YOLO11x       |      mosaic, scale         |  640       | 0.945 | 0.882 | 0.950 | 0.755 |56.9               | 
| YOLO11x      |  mosaic, scale & flip(lr)  |  640       | 0.929 | 0.885 | 0.948 | 0.733 | 56.9              | 

All experiments were conducted using the YOLO11-x architecture (56.9M parameters) and optimized with SGD (learning rate: 0.01, weight decay: 0.0005) for 100 epochs with a batch size of 16.

## **Citation**

If you make use of this research, please cite this repository. We will also add our paper citation soon!

```bibtex
@INPROCEEDINGS{11231948,
  author={Büyükkanber, Furkan and Yanalak, Mustafa and Musaoğlu, Nebiye},
  booktitle={2025 International Conference on Machine Intelligence for GeoAnalytics and Remote Sensing (MIGARS)}, 
  title={Impact of Data Enhancement Methods on Ship Detection Using YOLO11 in SAR Imagery}, 
  year={2025},
  volume={},
  number={},
  pages={1-4},
  keywords={Deep learning;Noise reduction;Data augmentation;Radar polarimetry;Data models;Reliability;Marine vehicles;Remote sensing;Machine intelligence;Image denoising;deep learning;ship detection;SAR dataset;image denoising;SAR-CAM;SARMSSD;YOLO11},
  doi={10.1109/MIGARS67156.2025.11231948}}
```

## **Contact**

For further information or any question, you can use the issues (https://github.com/buyukkanber/SARMSSD/issues) tab.

---------------------





