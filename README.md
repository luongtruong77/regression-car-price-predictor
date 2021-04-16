# Car Price Predictor using Regression Model
---
by Steven L Truong
## Abstract
---
In this project, I will use the data scraped from [cars.com](https://www.cars.com/) and build predictive model for people who want to predict the car's price. Buying and selling used cars is always a big decision if we have little-to-no knowledge about the market or automotive industry. After gathering data, I will analyze and seek insights from it before start modeling. In order to optimize my results, I engineer features from the original dataset and try multiple algorithms and present the outcomes. Furthermore, I also build the interactive web app to predict the car's price based on user's input features.

## Design
---
- This project is to predict the resonable price for most of the cars from general compact to luxury and sport. Within the predicted price with some margin errors, one can negotiate the best deal for selling and buying based on the predicted price.
- I will do exploratory analysis on my dataset to seek insights. After that, I will try different algorithms for my models and fine tune the parameters in order to acheive the best outcomes possible.

## Data
---
 **The main dataset**: the dataset is scraped from [cars.com](https://www.cars.com/) using `BeautifulSoup` and being analyzed in `Jupyter notebook` with `Python` and its libraries. The original dataset has `187168` rows and `15` columns. I engineer more features and drop irrelevant features to achieve the ready-to-work-with data set that has `122351` rows and `18` columns, `8` of which are categorical features.

## Algorithms
---
##### Feature Engineering
I observe that some features of the dataset contains different information, some of which can be indepent feature, I decide to extract them from the original features.
- Extract the `Make, Car Model, Model Year` from `Name`.
- Construct polynomial features.
- Convert categorical features to binary dummy variables to be suitable for buidling models.
- Try to build the models on different combination of numerical and categorical features.

##### Building models
I use linear regression, polynomial regression, random forest regressor, gradient boosted regressor, and extreme gradient boosting (XGBoost). Linear model performs very good, but the XGBoost has the best performance. Feature importance ranking is extracted from the XGBoost model to refine the models. 

##### Evaluation, models fine tunning and selection.
- I choose R^2 score and RMSE as my metrics. The entire dataset is split into 60-20-20 train/validation/test to train and test models. I also use L1 and L2 regularization to fine-tune my models. Later after narrowing down to 2 best candidates (Linear and XGBoost), I again split the data into 80-20 and using K-fold cross validation to conclude the results.
- Final performance results:
- - Linear Regression Model:
    - R^2 for train set: 0.871
    - R^2 for validation set: 869
    - RMSE = 4787.90
- - Lasso Model:
    -   R^2 for train set: 0.870
    -   R^2 for validation set: 866
- - Ridge Model:
    -   R^2 for train set: 0.871
    -   R^2 for validation set: 865
- - Extreme Gradient Boosting (XGBoost):
    -   R^2 for train set: 0.932
    -   R^2 for validation set: 0.920
    -   RMSE = 3749.5




## Tools
---
- BeautifulSoup, Numpy and Pandas for data scraping, data cleaning and manipulation.
- Matplotlib, yellowbrick and Seaborn for plotting and visualizing.
- Scikit-learn and xgboost for modeling.
- Streamlit and Heroku for building interactice app and deploying model to the cloud.


## Communication
---
- The presentation in pdf file is included to logically and visually convey the results of the process of buidling models. 
- In addition to the slides, the minimal predictive app for users is also being deployed to the cloud for testing and trying. 
![](https://github.com/luongtruong77/regression_proj/blob/main/figures/app1.png?raw=true)
![](https://github.com/luongtruong77/regression_proj/blob/main/figures/app2.png?raw=true)

