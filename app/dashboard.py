import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Diabetes Analysis Dashboard", layout="wide")

# Paths
data_path = Path(__file__).parent.parent / "data/diabetes_cleaned.csv"
plots_dir = Path(__file__).parent.parent / "plots"
report_pdf = Path(__file__).parent.parent / "report/report.pdf"

# Load data
df = pd.read_csv(data_path)

# Sidebar filters
st.sidebar.header("Filters")
age_filter = st.sidebar.slider("Filter by Age", int(df["Age"].min()), int(df["Age"].max()), (20, 50))
outcome_filter = st.sidebar.selectbox("Outcome", ["All", "Non-Diabetic", "Diabetic"])

# Apply filters
df_filtered = df[(df["Age"] >= age_filter[0]) & (df["Age"] <= age_filter[1])]
if outcome_filter != "All":
    df_filtered = df_filtered[df_filtered["Outcome"] == (1 if outcome_filter=="Diabetic" else 0)]

# Main title
st.title("📊 Diabetes Analysis Dashboard")
st.markdown("Explore and visualize the [Kaggle Diabetes dataset](https://www.kaggle.com/datasets/mathchi/diabetes-data-set)")

# Scatter plot BMI vs Glucose
st.subheader("BMI vs Glucose")
fig = px.scatter(df_filtered, x="BMI", y="Glucose", color="Outcome",
                 title="Relationship between BMI and Glucose")
st.plotly_chart(fig, use_container_width=True)

# Descriptive statistics in an expander
with st.expander("📈 View Descriptive Statistics"):
    st.write(df_filtered.describe())

# Boxplots section
st.subheader("📊 Boxplots by Variable")
boxplot_files = [
    "boxplot_Pregnancies.png",
    "boxplot_Glucose.png",
    "boxplot_BloodPressure.png",
    "boxplot_SkinThickness.png",
    "boxplot_Insulin.png",
    "boxplot_BMI.png",
    "boxplot_DiabetesPedigreeFunction.png",
    "boxplot_Age.png"
]

# Display boxplots in 2 columns per row
cols = st.columns(2)
for idx, plot_file in enumerate(boxplot_files):
    plot_path = plots_dir / plot_file
    if plot_path.exists():
        with cols[idx % 2]:
            st.image(str(plot_path), caption=plot_file.replace("boxplot_", "").replace(".png", ""))
    else:
        st.warning(f"⚠️ File {plot_file} not found in {plots_dir}")

import base64

with st.expander("📄 View Full Report"):
    if report_pdf.exists():
        # Lecture du PDF et encodage en base64
        with open(report_pdf, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')

        # Création de l'iframe HTML
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

        # Bouton de téléchargement
        with open(report_pdf, "rb") as f:
            st.download_button("📥 Download PDF", f, file_name="Diabetes_Report.pdf")
    else:
        st.warning(f"⚠️ Report file not found at {report_pdf}")

