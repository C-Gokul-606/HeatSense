# 🌡️ HeatSense

### Urban Heat Intelligence powered by Machine Learning

HeatSense is a machine-learning powered web application that analyzes environmental conditions and classifies urban heat risk into three levels:

**Low · Moderate · High**

The project uses historical Bengaluru weather data from **2020–2025** and a trained Logistic Regression classification pipeline.

---

## 🚀 Live Demo

Coming soon — deployed with Streamlit Community Cloud.

---

## ✨ Features

- 🌡️ Real-time heat-risk classification
- 🤖 Machine learning powered predictions
- 🎛️ Interactive What-If Simulator
- 📊 Historical temperature analysis
- 🕐 Hourly temperature intelligence
- 📈 Bengaluru weather insights
- 📋 Model performance dashboard
- 🌙 Modern dark glassmorphism interface
- ⚡ Interactive environmental controls

---

## 🧠 Machine Learning

### Model

**Logistic Regression**

The model classifies environmental conditions into:

| Risk Level | Description |
|---|---|
| 🟢 Low | Lower heat-risk conditions |
| 🟡 Moderate | Elevated heat-risk conditions |
| 🔴 High | Higher heat-risk conditions |

### Performance

| Metric | Result |
|---|---:|
| Test Accuracy | **97.55%** |
| Time-Series CV Accuracy | **97.24%** |
| CV Standard Deviation | **0.18%** |

The model was evaluated using a held-out test set and time-series cross-validation.

---

## 📊 Dataset

HeatSense uses hourly weather data for **Bengaluru** covering:

**January 2020 → December 2025**

The dataset contains **52,608 hourly observations**.

### Environmental variables

- Temperature
- Relative Humidity
- Precipitation
- Wind Speed
- Shortwave Solar Radiation

### Engineered features

- Hour
- Day
- Month
- Day of Year
- Season

---

## 🎛️ What-If Simulator

HeatSense allows users to modify environmental conditions and immediately observe how the trained model responds.

Users can experiment with:

- Temperature
- Humidity
- Wind Speed

The simulator sends the modified conditions through the same trained ML pipeline used for the main prediction.

---

## 📈 Historical Intelligence

HeatSense provides historical analysis of the Bengaluru weather dataset, including:

- Average temperature by month
- Average temperature by hour
- Highest recorded temperature
- Overall average temperature
- Number of historical observations
- Six years of weather data

---

## 🖥️ Tech Stack

### Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib

### Application

- Streamlit

### Visualization

- Streamlit native charts
- Pandas

### Development

- Google Colab
- GitHub

---

## 📁 Project Structure

HeatSense/

├── app.py
├── heatsense_model.pkl
├── weather_data.csv
├── model_metadata.json
├── requirements.txt
├── .gitignore
└── README.md

---

## ⚙️ Run Locally

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/HeatSense.git

cd HeatSense

### 2. Install dependencies

pip install -r requirements.txt

### 3. Start the application

streamlit run app.py

The application will open in your browser.

---

## 🔬 Model Pipeline

Environmental Conditions

↓

Feature Engineering

↓

Logistic Regression

↓

Heat Risk Classification

Low · Moderate · High

---

## 🔮 Future Improvements

- Short-term heat-risk forecasting
- Support for additional cities
- Weather API integration
- Satellite and land-surface temperature data
- Explainable AI
- Heatwave alerts
- Urban heat-island analysis
- Automated model updates

---

## 👨‍💻 Author

**Gokul C**

BTech (Hons) Computer Science

RV University, Bengaluru

---

## ⭐ Project

HeatSense demonstrates how environmental data and machine learning can be transformed into an interactive decision-support application.

**Data → Feature Engineering → Machine Learning → Interactive Visualization**