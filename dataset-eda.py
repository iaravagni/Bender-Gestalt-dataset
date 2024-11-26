import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read both datasets
scores_df = pd.read_csv('dataset/scores_summary.csv')
metadata_df = pd.read_csv('dataset/metadata.csv')

# Merge the datasets on 'id'
df = pd.merge(scores_df, metadata_df, on='id')

# Basic dataset info
print("Dataset Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())

# Distribution of diagnoses
plt.figure(figsize=(10, 6))
df['diagnose'].value_counts().plot(kind='bar')
plt.title('Distribution of Diagnoses')
plt.xlabel('Diagnosis')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Create correlation matrix only for numeric columns
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = df[numeric_cols].corr()

# Plot correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Numeric Variables')
plt.tight_layout()
plt.show()



# Create the boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='education_level', y='total_score')
plt.title('Total Scores by Education Level')
plt.xticks(rotation=45)
plt.xlabel('Education Level')
plt.ylabel('Total Score')
plt.tight_layout()
plt.show()

# Taken test before
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='taken_test_before', y='total_score')
plt.title('Total Scores by Previous Test Experience')
plt.xlabel('Has Taken Test Before')
plt.ylabel('Total Score')
plt.tight_layout()
plt.show()
