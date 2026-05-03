# 🫁 Lungs Cancer Detection

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
| Train Accuracy | ~98% |
| Val Accuracy | ~95% |

---

## 📁 Project Structure
```
LIDC-cancer-detection/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py            # Database connection & session management
│   ├── models/                # ML model (unchanged)
│   │   ├── __init__.py
│   │   ├── model.py
│   │   └── preprocess.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py            # signup, login, logout, token refresh
│   │   ├── predict.py         # prediction endpoint (requires auth)
│   │   └── history.py         # fetch user prediction history
│   ├── schemas/               # Pydantic models for request/response
│   │   ├── __init__.py
│   │   ├── user.py            # UserCreate, UserLogin, UserOut, Token
│   │   └── prediction.py      # PredictionResponse, PredictionHistory
│   ├── db_models/             # SQLAlchemy ORM models
│   │   ├── __init__.py
│   │   └── models.py          # User, Prediction tables
│   ├── static/
│   │   ├── style.css
│   │   └── script.js
│   └── templates/
│       ├── index.html         # prediction page (logged‑in view)
│       ├── login.html
│       └── signup.html
│
├── models/                    # trained .pth file
├── data/                      # image data
├── notebook/                  # jupyter model trained file
├── requirements.txt
└── README.md
```
