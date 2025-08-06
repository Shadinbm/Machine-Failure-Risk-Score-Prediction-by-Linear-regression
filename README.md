

---

### 📄 `README.md`

````markdown
# ⚙️ Machine Failure Risk Prediction Model

This project uses a **Linear Regression** model to predict machine failure risk scores based on key parameters like temperature, vibration, pressure, motor current, and more. It's built for **predictive maintenance** to help anticipate equipment health and reduce unexpected breakdowns.

---

## 📂 Files Included

- `scoremodel.py`: Core Python script for model training and prediction
- `dat.csv`: Dataset used for training (sensor readings and risk scores)
- `new.csv`: (optional) File where predictions can be appended/stored

---

## 🧠 Model Details

- **Algorithm**: Linear Regression
- **Input Features**:
  - `temperature_celsius`
  - `vibration_mm_per_sec`
  - `pressure_bar`
  - `motor_current_amp`
  - `oil_temperature_celsius`
  - `rotational_speed_rpm`
  - `power_consumption_kw`
- **Target**: `failure_risk_score` (0–100)

---

## 🎯 Prediction Output

The model returns a risk score and categorizes it as:

- ✅ **Good Condition**: score < 50  
- ⚠️ **Maintenance Required**: 50 ≤ score < 90  
- 🚨 **Critical Condition**: score ≥ 90  

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/Shadinbm/machine-failure-risk-model.git
   cd machine-failure-risk-model
````

2. Make sure `dat.csv` and `new.csv` exist in the same directory.

3. Run the script:

   ```bash
   python scoremodel.py
   ```

4. Enter the values as prompted (temperature, vibration, etc.)
   The model will print the **failure risk score** and the **equipment condition**.

---

## 📈 Example Input & Output

```text
Enter temperature: 40  
Enter vibration: 5.1  
Enter pressure: 2.3  
Enter motor current: 11.2  
Enter oil temperature: 80  
Enter rotation speed rpm: 1400  
Enter power consumption: 6.5  

Machine failure Risk Score = [72.3]  
Maintenance Required
```

---

## 🧰 Built With

* Python
* Pandas
* Scikit-learn

---

## 📧 Contact

**Author**: Muhammed Shadin Bm
📬 **Email**: [bmshadin43@gmail.com](mailto:bmshadin43@gmail.com)
🔗 **LinkedIn**: [muhammed-shadin-bm](https://www.linkedin.com/in/muhammed-shadin-bm-23871432b)

---

> 💡 *Predict before it breaks. Stay ahead with data-driven maintenance.*

```

---

