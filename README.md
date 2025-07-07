# 💧 Water Quality Predictor

An interactive machine learning web app to **predict water quality indicators** like **O₂ (oxygen levels)**, **BSK5**, and **Suspended Solids** based on key chemical features.

Built using:
- 🧠 Stacking Regressor (XGBoost + Linear Regression)
- ⚙️ Streamlit for UI
- 📦 Scikit-learn, Pandas, Joblib

---

## 🚀 Live Demo

✅ [Click here to try the app on Streamlit](https://water-quality-prediction-aicte.streamlit.app/)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://water-quality-prediction-aicte.streamlit.app/)

---

## 📊 Features

✅ Predict water quality indicators  
✅ Clean, interactive UI (dark theme)  
✅ Sidebar input sliders  
✅ Bar chart for visual predictions  
✅ Model built using real-world water dataset  
✅ Deployed with Streamlit

---

## 🧠 ML Model Overview

- Input features:
  - NH4, NO3, NO2, SO4, PO4, CL
- Predicted outputs:
  - O₂ (mg/L)
  - BSK5 (mg/L)
  - Suspended Solids (mg/L)
- Model:
  - `StackingRegressor` with `MultiOutputRegressor`
  - Preprocessing: `StandardScaler`
  - Exported using `joblib`

---

## 🛠 Installation

### 🔗 Clone the repository

```bash
git clone https://github.com/Manvi-bit-tech/Water_Quality_Analysis_AICTE.git
cd Water_Quality_Analysis_AICTE
```

### 📦 Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 📦 Install dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Run the app locally

```bash
streamlit run app.py
```

---

## 🖼 Preview

> You’ll see a sidebar to input pollutant levels.  
> Hit “Predict” and get results with a bar chart + values!

---

## 📁 Project Structure

```
├── app.py                 # Streamlit app
├── scaler.pkl            # StandardScaler used during training
├── stacking_model.pkl    # Final trained model
├── requirements.txt      # Required Python libraries
├── .streamlit/
│   └── config.toml       # Custom theme settings
└── README.md
```

---

## 🌈 Custom Theme

```toml
[theme]
base = "dark"
primaryColor = "#0b1d51"
backgroundColor = "#08ccde"
secondaryBackgroundColor = "#725cad"
textColor = "#ffffff"
```

---

## 🧠 Future Improvements

- Add CSV upload for batch predictions   
- Enhance UI with Lottie animations or charts  
- Add feedback form or download button for results  

---

## 👩‍💻 Author

Made with 💙 by **Manvi Dhamija**  
Connect on [LinkedIn](https://www.linkedin.com/in/manvi-dhamija) | GitHub: [@Manvi-bit-tech](https://github.com/Manvi-bit-tech)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
