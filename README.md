# ml_regression_gjrich

# Auto MPG Regression Analysis

This project explores, analyzes, and builds predictive models for fuel efficiency (MPG) using the classic Auto MPG dataset from UCI.

## Overview

In this project, I apply various regression modeling techniques to predict automobile fuel efficiency based on the features vehicle weight, model year, and car make. The analysis demonstrates how different regression approaches can improve prediction accuracy and reveals interesting patterns in automotive fuel efficiency.

## Dataset

The dataset used is the UCI Auto MPG dataset which contains fuel consumption information in miles per gallon (MPG) along with various attributes of automobiles from the late 1970s and early 1980s. The dataset includes:

- MPG (miles per gallon) - our target variable
- Cylinders, displacement, horsepower, weight
- Acceleration
- Model year (70-82)
- Origin (America, Europe, Asia)
- Car name

## Features Explored

After careful analysis, the main features used for modeling include:
- Weight
- Model year
- Car make (extracted from car name)

These features were chosen due to their strong correlation with MPG and their ability to represent important characteristics of vehicles that influence fuel efficiency.

## Models and Techniques

Three different regression approaches were implemented and compared:

1. **Baseline Linear Regression** - A simple multivariate linear regression model
2. **Pipeline with StandardScaler** - Linear regression with standardized features
3. **Polynomial Regression** - Testing various polynomial degrees (3, 4, 6, 9)

The project includes careful test-train split evaluation, with special attention to preserving the distribution of the target variable in both sets.

## Key Findings

- The polynomial regression model (degree 3) achieved the best performance with an R² score of 0.885 on the test set
- Vehicle weight showed the strongest negative correlation with MPG
- Model year demonstrated a positive correlation with MPG, reflecting improvements in fuel efficiency over time
- Asian car manufacturers generally produced more fuel-efficient vehicles compared to American and European manufacturers

## Files in this Repository

- `regression_gjrich.ipynb`: The main Jupyter notebook containing the full analysis
- `data/auto-mpg.csv`: The dataset used for analysis
- `REGRESSION_PROJECT.md`: The original project specification and requirements

## Getting Started

### Prerequisites

To run this notebook locally, you'll need:
- Python 3.x
- Jupyter Notebook
- The following Python libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn

### Installation

1. Clone this repository:
```
git clone https://github.com/yourusername/ml_regression_gjrich.git
cd ml_regression_gjrich
```

2. Create and activate a virtual environment (optional):
```
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```
pip install -r requirements.txt
```

4. Launch Jupyter Notebook:
```
jupyter notebook
```

5. Open `regression_gjrich.ipynb` in the Jupyter interface

## License

This project is available for educational purposes. The original dataset is from the UCI Machine Learning Repository.

## Acknowledgments

- UCI Machine Learning Repository for providing the dataset
- Special thanks to the instructors who designed this challenging project
