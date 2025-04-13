# ml_regression_gjrich

Gabriel Richards / April 2025

## Auto MPG Regression Analysis

This project explores and builds predictive models for fuel efficiency (MPG) using the classic Auto MPG dataset from UCI.

View my notebook for yourself here!
https://github.com/gjrich/ml_regression_gjrich/blob/master/regression_gjrich.ipynb

## Overview

In this project, I apply regression modeling techniques to predict automobile fuel efficiency based on the features vehicle weight, model year, and car make. The analysis demonstrates how different regression approaches can improve prediction accuracy and reveals interesting patterns in automotive fuel efficiency.

As part of ths project, I also reviewed Philip Fowler's Notebook. My review is available here:
https://github.com/gjrich/ml_regression_gjrich/blob/master/PeerReview.md

His notebook and repository are available here:
https://github.com/drpafowler/ml-final/blob/main/regression_fowler.ipynb


## Dataset

The dataset used is the UCI Auto MPG dataset which contains fuel consumption data for various vehicles measured in miles per gallon (MPG), along with  other attributes of those automobiles. The vehicles are from the late 1970s and early 1980s. The dataset includes:

- MPG (miles per gallon) - our target variable
- Cylinders, displacement, horsepower, weight
- Acceleration
- Model year (70-82)
- Origin (America, Europe, Asia)
- Car name

## Features Explored

After review of correlation, the main features chosen for modeling were:
- Weight
- Model year
- Car make (extracted from car name)

These features were used due to their their ability to represent the traits of vehicles that influence fuel efficiency.

## Models and Techniques

Four different regression approaches were implemented and compared:

1. **Baseline Linear Regression** - A simple multivariate linear regression model
2. **Pipeline 1: Imputer → StandardScaler → Linear Regression**
3. **Pipeline 2: Imputer → Polynomial Features (degree=3) → StandardScaler → Linear Regression**
4. **Polynomial Regression** - As a bonus, tested various polynomial degrees (3, 4, 6, 9)

The project also included an in-depth test-train split evaluation - I took special attention in preserving the distribution of the target variable in both sets.

## Key Findings

- The polynomial regression model (degree 4) achieved the best performance with an R² score of 0.90 on the test set
  - Optimizing the polynomial degree was able to outperform all the other models, even the more complex Pipeline 1 and Pipeline 2
  - This is even though the polynomial optimization efforts removed the 'make' feature to avoid the categorical variable causing dimensionality problems
- Vehicle weight showed the strongest negative correlation with MPG
- Model year held a positive correlation with MPG, reflecting improvements in fuel efficiency over time
- Asian car manufacturers produced more fuel-efficient vehicles

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
