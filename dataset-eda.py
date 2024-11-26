import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pytest

# Paths to the dataset files
scores_file = 'dataset/scores_summary.csv'
metadata_file = 'dataset/metadata.csv'

# Read both datasets
scores_df = pd.read_csv(scores_file)
metadata_df = pd.read_csv(metadata_file)

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

# Most common error
columns_to_plot = [
    'rotation', 'overlapping_difficulty', 'simplication', 'fragmentation', 'retrogression',
    'perseveration', 'collision', 'impotence', 'closure_difficulty', 'motor_incoordination',
    'angulation', 'cohesion', 'time'
]

mean_values = df[columns_to_plot].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=mean_values.index, y=mean_values.values)
plt.title('Mean Values of Parameters Ordered from Largest to Smallest')
plt.xlabel('Parameter')
plt.ylabel('Mean Value')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Pytest for CSV reading ---
def test_pd_read_scores():
    """Test if the scores CSV is read correctly"""
    scores_df = pd.read_csv(scores_file)
    
    # Check if the DataFrame is not empty
    assert not scores_df.empty, "Scores DataFrame is empty"
    
    # Check if the required columns exist
    required_columns = [
        'id', 'rotation', 'overlapping_difficulty', 'simplication', 'fragmentation',
        'retrogression', 'perseveration', 'collision', 'impotence', 'closure_difficulty',
        'motor_incoordination', 'angulation', 'cohesion', 'time', 'total_score', 'diagnose'
    ]
    for column in required_columns:
        assert column in scores_df.columns, f"Column '{column}' not found in scores DataFrame"
    
    # Check if the number of rows matches the expected value (use len to check row count)
    expected_row_count = 20 
    assert len(scores_df) == expected_row_count, f"Expected {expected_row_count} rows, but found {len(scores_df)}"

def test_pd_read_metadata():
    """Test if the metadata CSV is read correctly"""
    metadata_df = pd.read_csv(metadata_file)
    
    # Check if the DataFrame is not empty
    assert not metadata_df.empty, "Metadata DataFrame is empty"
    
    # Check if the required columns exist
    required_columns = ['id', 'age', 'nacionality', 'education_level', 'taken_test_before']
    for column in required_columns:
        assert column in metadata_df.columns, f"Column '{column}' not found in metadata DataFrame"
    
    # Check if the number of rows matches the expected value
    expected_row_count = 20  
    assert len(metadata_df) == expected_row_count, f"Expected {expected_row_count} rows, but found {len(metadata_df)}"

if __name__ == "__main__":
    pytest.main()
