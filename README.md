# 🫁 LIDC Cancer Detection

Deep Learning model to classify lung nodules as **Benign** or **Malignant** using CT scan patches from the LIDC-IDRI dataset.

---

## 📊 Dataset

| | Details |
|---|---|
| **Name** | LIDC-IDRI Slices |
| **Source** | Kaggle |
| **Total Images** | 15,548 PNG patches |
| **Classes** | Benign (nodule-0) / Malignant (nodule-1+) |

🔗 **Download Dataset:** [LIDC-IDRI on Kaggle](https://www.kaggle.com/datasets/zhangweiled/lidcidri)

> ⚠️ Dataset is not included in this repo due to large size (10GB+).  
> Download manually from Kaggle and place it as `LIDC-IDRI-slices/` in root folder.

---

## 🧠 Model

- **Architecture:** ResNet18 (Pretrained on ImageNet)
- **Framework:** PyTorch
- **Train / Test Split:** 80% / 20%
- **Epochs:** 10

---

## 🚀 How to Run
```bash
git clone https://github.com/YOUR_USERNAME/lidc-cancer-detection.git
cd lidc-cancer-detection
pip install -r requirements.txt
jupyter notebook
```

---

## 📈 Results

| Metric | Score |
|---|---|
| Train Accuracy | ~85% |
| Val Accuracy | ~81% |

---

## 📁 Project Structure
```
lidc-cancer-detection/
├── LIDC-pytorch.ipynb   ← main notebook
├── README.md
└── .gitignore
```
