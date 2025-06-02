# 🧠 Stroke Risk Prediction using Machine Learning

This project leverages machine learning algorithms to predict the likelihood of a person experiencing a stroke based on health-related factors. Early detection of stroke risk is crucial for initiating timely preventive care and reducing fatal outcomes.

## 📌 Importance of Stroke Prediction

- Early prediction of stroke risk can save lives by enabling timely medical intervention.  
- The model analyzes health indicators to identify high-risk individuals.  
- Helps doctors prioritize care and support preventive strategies.  
- Reduces healthcare costs by avoiding stroke-related complications.  
- Enables data-driven decisions in public and personal health planning.

## 📊 Dataset Information

- Source: [Kaggle – Stroke Prediction Dataset](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset)
- Features:
  - Gender, Age, Hypertension, Heart Disease, Marital Status
  - Work Type, Residence Type, Average Glucose Level, BMI, Smoking Status
  - Target: `stroke` (0: No, 1: Yes)

## 🛠️ Tools & Technologies

- Python
- pandas, numpy
- matplotlib, seaborn
- scikit-learn (Random Forest, Logistic Regression, etc.)

## 🧪 Model Overview

- Preprocessing: Handling missing values, encoding categorical features, feature scaling
- Training: Using Random Forest Classifier (best performance)
- Evaluation Metrics: Accuracy, Precision, Recall, F1 Score, ROC AUC
- Performance: Achieved high accuracy and balanced recall for effective medical triage

## 📂 Repository Structure

```

stroke-prediction-ml/
│
├── stroke\_prediction.ipynb     # Jupyter notebook with full implementation
├── README.md                   # Project documentation
├── requirements.txt            # Dependencies list
├── .gitignore                  # Files to ignore
└── LICENSE                     # License (optional)

````

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/GUNALSABITHA/Forecasting-Stroke-Risk.git
   cd Forecasting-Stroke-Risk
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Open and run the notebook:

   ```bash
   jupyter notebook stroke_prediction.ipynb
   ```





