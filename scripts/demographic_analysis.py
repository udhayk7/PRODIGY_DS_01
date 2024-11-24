import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create sample demographic data
np.random.seed(42)
n_samples = 1000

# Generate age data with a normal distribution (mean age 35, std 15)
ages = np.random.normal(35, 15, n_samples)
ages = np.clip(ages, 0, 90).astype(int)  # Clip ages between 0 and 90

# Generate gender data
genders = np.random.choice(['Male', 'Female'], n_samples, p=[0.48, 0.52])

# Create a DataFrame
df = pd.DataFrame({
    'Age': ages,
    'Gender': genders
})

# 1. Age Distribution (Histogram)
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(data=df, x='Age', bins=30, kde=True)
plt.title('Age Distribution in Population')
plt.xlabel('Age')
plt.ylabel('Count')

# 2. Gender Distribution (Bar Plot)
plt.subplot(1, 2, 2)
gender_counts = df['Gender'].value_counts()
sns.barplot(x=gender_counts.index, y=gender_counts.values)
plt.title('Gender Distribution in Population')
plt.xlabel('Gender')
plt.ylabel('Count')

plt.tight_layout()
plt.show()

# 3. Age Distribution by Gender (Box Plot)
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Gender', y='Age')
plt.title('Age Distribution by Gender')
plt.show()

# Print some summary statistics
print("\nSummary Statistics:")
print("\nAge Statistics:")
print(df['Age'].describe())
print("\nGender Distribution:")
print(df['Gender'].value_counts(normalize=True).round(3) * 100, "%")
