### 🩺 Diabetes Data Analysis Dashboard

This project is a **Streamlit-based interactive dashboard** for exploring and analyzing the Diabetes dataset from Kaggle. It includes **data cleaning, visualization, and an auto-generated PDF report**.

-----

### 📌 Features

  - Upload, clean, and analyze the Diabetes dataset.
  - Visualize distributions with **interactive boxplots**.
  - Generate and download a **full PDF report**.
  - View the dataset source directly from the app.

-----

### 📊 Dataset

We are using the dataset from Kaggle:
[**Kaggle Diabetes Dataset**](https://www.kaggle.com/datasets/mathchi/diabetes-data-set)

-----

### 🛠️ Installation & Setup

#### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/diabetes-dashboard.git
cd diabetes-dashboard
```

#### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
```

  - **Windows**:

<!-- end list -->

```bash
venv\Scripts\activate
```

  - **Mac/Linux**:

<!-- end list -->

```bash
source venv/bin/activate
```

#### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

-----

### 🚀 Run the Application

Once inside the `venv`:

```bash
streamlit run app/dashbord.py
```

The dashboard will open in your browser.

-----

### 📂 Project Structure

```
project/
│── app/                 # Streamlit app code
│── code/                # code used to clean the datas
│── data/                # data used
│── plots/               # Generated plots
│── report/              # Generated PDF reports
│── requirements.txt     # Python dependencies
│── README.md            # Documentation
```

-----

### 📄 Generating the PDF Report

Inside the dashboard, after loading the dataset, you can:

1.  Explore the visualizations.
2.  Click the **"Generate Report"** button.
3.  Preview and download the PDF.

-----

### 💡 Notes

  - Make sure you are inside the virtual environment when running the app.
  - The dataset is not included; download it from the Kaggle link above.
  - This project requires **Python 3.8+**.

-----

### 📜 License

This project is open-source and available under the MIT License.

