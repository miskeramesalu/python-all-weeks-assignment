# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style for better looking plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Task 1: Load and Explore the Dataset
try:
    # Load the Titanic dataset from a URL
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)
    
    print("Titanic dataset loaded successfully!")
    print(f"Dataset shape: {df.shape}")
    
except Exception as e:
    print(f"Error loading dataset: {e}")
    # Fallback: try to load from local file if available
    try:
        df = pd.read_csv("titanic.csv")
        print("Loaded Titanic dataset from local file.")
    except:
        print("Could not load Titanic dataset. Please check your internet connection.")
        exit()

# Display the first few rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Explore the structure of the dataset
print("\nDataset information:")
print(df.info())

print("\nChecking for missing values:")
print(df.isnull().sum())

# Clean the dataset
print("\nCleaning the dataset...")
# Fill missing age values with median age
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill missing embarked values with the most common value
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop cabin column as it has too many missing values
df.drop('Cabin', axis=1, inplace=True)

# Check if any missing values remain
print("Missing values after cleaning:")
print(df.isnull().sum())

# Task 2: Basic Data Analysis
# Compute basic statistics for numerical columns
print("\nBasic statistics of numerical columns:")
print(df.describe())

# Group by passenger class and compute mean of numerical columns
print("\nMean of numerical columns by passenger class:")
class_group = df.groupby('Pclass').mean(numeric_only=True)
print(class_group)

# Group by survival status and compute mean of numerical columns
print("\nMean of numerical columns by survival status:")
survival_group = df.groupby('Survived').mean(numeric_only=True)
print(survival_group)

# Identify patterns or interesting findings
print("\nInteresting findings:")
print("1. First-class passengers had a higher survival rate than other classes.")
print("2. Females had a much higher survival rate than males.")
print("3. Passengers with higher fares were more likely to survive.")
print("4. Children (Age < 18) had a higher survival rate than adults.")

# Task 3: Data Visualization
# Create a figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Titanic Dataset Analysis', fontsize=16, fontweight='bold')

# 1. Line chart showing age distribution (using index as pseudo-time)
sorted_by_age = df.sort_values('Age')
axes[0, 0].plot(sorted_by_age.index, sorted_by_age['Age'], color='blue', alpha=0.7)
axes[0, 0].set_title('Age Distribution of Passengers (Sorted)')
axes[0, 0].set_xlabel('Passenger Index')
axes[0, 0].set_ylabel('Age')
axes[0, 0].grid(True, alpha=0.3)

# 2. Bar chart showing survival rate by passenger class
survival_by_class = df.groupby('Pclass')['Survived'].mean()
survival_by_class.plot(kind='bar', ax=axes[0, 1], color=['lightcoral', 'lightblue', 'lightgreen'])
axes[0, 1].set_title('Survival Rate by Passenger Class')
axes[0, 1].set_xlabel('Passenger Class')
axes[0, 1].set_ylabel('Survival Rate')
axes[0, 1].tick_params(axis='x', rotation=0)

# 3. Histogram of passenger ages
axes[1, 0].hist(df['Age'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
axes[1, 0].set_title('Age Distribution of Passengers')
axes[1, 0].set_xlabel('Age')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].grid(True, alpha=0.3)

# 4. Scatter plot to visualize relationship between age and fare
scatter = axes[1, 1].scatter(df['Age'], df['Fare'], alpha=0.6, c=df['Survived'], cmap='coolwarm')
axes[1, 1].set_title('Age vs Fare (Color indicates survival)')
axes[1, 1].set_xlabel('Age')
axes[1, 1].set_ylabel('Fare')
# Create legend for survival
legend_labels = {0: 'Did Not Survive', 1: 'Survived'}
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Did Not Survive'),
           plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Survived')]
axes[1, 1].legend(handles=handles, title='Survival Status')

plt.tight_layout()
plt.savefig('titanic_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Additional visualizations with seaborn for enhanced styling
plt.figure(figsize=(12, 8))
sns.boxplot(x='Pclass', y='Age', hue='Survived', data=df)
plt.title('Age Distribution by Passenger Class and Survival Status')
plt.xlabel('Passenger Class')
plt.ylabel('Age')
plt.savefig('age_class_boxplot.png', dpi=300, bbox_inches='tight')
plt.show()

# Survival rate by gender
plt.figure(figsize=(8, 6))
survival_by_gender = df.groupby('Sex')['Survived'].mean()
survival_by_gender.plot(kind='bar', color=['pink', 'lightblue'])
plt.title('Survival Rate by Gender')
plt.xlabel('Gender')
plt.ylabel('Survival Rate')
plt.xticks(rotation=0)
plt.savefig('survival_by_gender.png', dpi=300, bbox_inches='tight')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap of Numerical Features')
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nAnalysis completed successfully!")
print("Visualizations have been saved as PNG files.")