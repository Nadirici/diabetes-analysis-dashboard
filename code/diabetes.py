import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# -------------------------------
# Step 0: Create plots folder if not exists
# -------------------------------
os.makedirs("plots", exist_ok=True)

# -------------------------------
# Step 1: Load the original dataset
# -------------------------------
df = pd.read_csv("data/diabetes.csv")

# -------------------------------
# Step 2: Missing / Invalid Values Before Cleaning
# -------------------------------
cols_to_check = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

print("=== Missing / Invalid Values Before Cleaning ===")
for col in df.columns:
    if col in cols_to_check:
        missing_count = (df[col] == 0).sum()
    else:
        missing_count = df[col].isnull().sum()
    print(f"{col}: {missing_count} missing/invalid values")


# -------------------------------
# Step 3: Clean dataset (replace 0 by median)
# -------------------------------
for col in cols_to_check:
    median = df[col].median()
    df[col] = df[col].replace(0, median)

print("\n=== After cleaning zeros ===")
for col in cols_to_check:
    print(f"{col}: {(df[col]==0).sum()} zero values remaining")

# Export cleaned dataset
df.to_csv("data/diabetes_cleaned.csv", index=False)
print("\nCleaned dataset saved as 'data/diabetes_cleaned.csv'")


# -------------------------------
# Step 4: Boxplots by Outcome
# -------------------------------
for col in df.columns[:-1]:  # exclude Outcome
    plt.figure()
    sns.boxplot(x="Outcome", y=col, data=df)
    plt.title(f'{col} by Outcome')
    plt.tight_layout()
    plt.savefig(f'plots/boxplot_{col}.png')
    plt.close()

# -------------------------------
# Step 5: Correlation Heatmap
# -------------------------------
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Matrix")
plt.tight_layout()
plt.savefig('plots/correlation_heatmap.png')
plt.close()


print("\nAll plots saved in the 'plots/' folder")
