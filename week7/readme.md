Titanic Dataset Analysis
https://img.shields.io/badge/Python-3.8%252B-blue
https://img.shields.io/badge/Pandas-1.3%252B-orange
https://img.shields.io/badge/Matplotlib-3.4%252B-blue
https://img.shields.io/badge/Seaborn-0.11%252B-red

A comprehensive data analysis project exploring the famous Titanic dataset to uncover patterns and relationships between passenger characteristics and survival rates.

📊 Project Overview
This project performs an end-to-end analysis of the Titanic passenger dataset, including:

Data loading and exploration

Data cleaning and preprocessing

Statistical analysis

Multiple data visualizations to identify key patterns

🎯 Key Findings
Class Disparity: First-class passengers had a significantly higher survival rate (63%) compared to second-class (47%) and third-class (24%) passengers.

Gender Bias: Females had a much higher survival rate (74%) compared to males (19%), reflecting the "women and children first" protocol.

Age Factor: Children (under 18) had a higher survival rate than adults, though the relationship between age and survival is complex.

Economic Factor: Passengers who paid higher fares were more likely to survive, likely because they were in higher classes.

📈 Visualizations
The analysis includes several informative visualizations:

Age Distribution: Line chart showing the spread of passenger ages

Survival by Class: Bar chart comparing survival rates across passenger classes

Age vs Fare: Scatter plot showing relationship between age, fare, and survival

Age Distribution: Histogram of passenger ages

Age by Class and Survival: Box plot showing age distribution across classes and survival status

Survival by Gender: Bar chart comparing survival rates between males and females

Correlation Heatmap: Visual representation of correlations between numerical features

📁 Files
titanic_analysis.py: Main Python script containing the complete analysis

titanic_analysis.png: Composite visualization of key charts

age_class_boxplot.png: Box plot of age by class and survival status

survival_by_gender.png: Bar chart of survival rates by gender

correlation_heatmap.png: Heatmap of feature correlations

🛠️ Requirements
To run this analysis, you'll need:

bash
pip install pandas matplotlib seaborn numpy
🚀 Usage
Clone or download the project files

Install required packages: pip install pandas matplotlib seaborn numpy

Run the script: python titanic_analysis.py

The script will automatically:

Download the Titanic dataset from GitHub

Clean and preprocess the data

Perform statistical analysis

Generate and save all visualizations

📋 Dataset Information
The Titanic dataset contains information about 891 passengers aboard the Titanic, including:

Survival status (0 = No, 1 = Yes)

Passenger class (1st, 2nd, 3rd)

Name, Sex, Age

Number of siblings/spouses aboard

Number of parents/children aboard

Ticket number, Fare, Cabin, Embarkation port

💡 Insights for Further Research
This analysis could be extended by:

Building a predictive model for survival

Analyzing family relationships and their impact on survival

Examining specific passenger stories that deviate from the general trends

Comparing survival rates across different embarkation points

📚 Learning Outcomes
This project demonstrates fundamental data analysis techniques including:

Data cleaning and preprocessing

Exploratory data analysis (EDA)

Statistical analysis

Data visualization using multiple chart types

Working with popular Python data science libraries

🔄 Alternative Data Source
If the GitHub dataset is unavailable, the script will attempt to load from a local titanic.csv file. You can download the dataset from Kaggle and place it in the same directory as the script.