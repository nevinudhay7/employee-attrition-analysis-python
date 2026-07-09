import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
os.makedirs("images", exist_ok=True)

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

print("\nFIRST 5 ROWS")
print(df.head())

print("\nSHAPE")
print(df.shape)

print("\nCOLUMNS")
print(df.columns)

print("\nDATASET INFO")
df.info()

print("\nSTATISTICAL SUMMARY")
print(df.describe())

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nATTRITION COUNT")
print(df["Attrition"].value_counts())

print("\nATTRITION PERCENTAGE")
print(df["Attrition"].value_counts(normalize=True)*100)

plt.figure(figsize=(6,4))
sns.countplot(x="Attrition", data=df)
plt.title("Employee Attrition")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")
plt.savefig("images/attrition.png", dpi=300, bbox_inches="tight")
plt.show()

print(df.groupby("Department")["Attrition"].value_counts())
print(pd.crosstab(df["Department"], df["Attrition"]))

plt.figure(figsize=(8,5))
sns.countplot(x="Department", hue="Attrition", data=df)
plt.title("Department-wise Attrition")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.savefig("images/department.png", dpi=300, bbox_inches="tight")
plt.show()

print(pd.crosstab(df["OverTime"], df["Attrition"]))

plt.figure(figsize=(6,4))
sns.countplot(x="OverTime", hue="Attrition", data=df)
plt.title("OverTime vs Attrition")
plt.xlabel("OverTime")
plt.ylabel("Number of Employees")
plt.savefig("images/overtime.png", dpi=300, bbox_inches="tight")
plt.show()

print(df.groupby("Attrition")["MonthlyIncome"].mean())

plt.figure(figsize=(8,5))
sns.boxplot(x="Attrition", y="MonthlyIncome", data=df)
plt.title("Monthly Income vs Attrition")
plt.savefig("images/income.png", dpi=300, bbox_inches="tight")
plt.show()

print(pd.crosstab(df["JobSatisfaction"], df["Attrition"]))

plt.figure(figsize=(8,5))
sns.countplot(x="JobSatisfaction", hue="Attrition", data=df)
plt.title("Job Satisfaction vs Attrition")
plt.savefig("images/jobsatisfaction.png", dpi=300, bbox_inches="tight")
plt.show()

print(pd.crosstab(df["WorkLifeBalance"], df["Attrition"]))

plt.figure(figsize=(8,5))
sns.countplot(x="WorkLifeBalance", hue="Attrition", data=df)
plt.title("Work-Life Balance vs Attrition")
plt.savefig("images/worklifebalance.png", dpi=300, bbox_inches="tight")
plt.show()

print(df.groupby("Attrition")["Age"].mean())

plt.figure(figsize=(8,5))
sns.boxplot(x="Attrition", y="Age", data=df)
plt.title("Age vs Attrition")
plt.savefig("images/age.png", dpi=300, bbox_inches="tight")
plt.show()

plt.figure(figsize=(14,10))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.savefig("images/heatmap.png", dpi=300, bbox_inches="tight")
plt.show()

plt.figure(figsize=(6,6))
df["Attrition"].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.title("Attrition Percentage")
plt.ylabel("")
plt.savefig("images/piechart.png", dpi=300, bbox_inches="tight")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x="Age", y="MonthlyIncome", hue="Attrition", data=df, alpha=0.7)
plt.title("Age vs Monthly Income")
plt.xlabel("Age")
plt.ylabel("Monthly Income")
plt.savefig("images/scatter.png", dpi=300, bbox_inches="tight")
plt.show()

print("PROJECT COMPLETED SUCCESSFULLY!")
