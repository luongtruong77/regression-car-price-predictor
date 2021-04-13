# Regression Project MVP
- This project is to build the model to predict car's price based on its chosen features.
- After gathering and cleaning data, I have my final data set with the shape of `(65796, 18)` (65796 rows and 18 columns). Furthermore, I have carefully engineered more features and dummified the dataset's categorical features to have the dataframe of `(65796, 532)`.
 ![](https://github.com/luongtruong77/regression_proj/blob/main/figures/df_shape.png?raw=true)
- I've chosen the simple validation scheme `train/val/test (60-20-20)` (since my dataset is relatively large) to validate my model and built the simple linear regression model with:
    - R^2 score on validation set : 0.8622
    - R^2 score on test set: 0.8656
    - Mean Absolute Error: 3515.30
    - Root Mean Squared Error (RMSE): 4940.82

    ![](https://github.com/luongtruong77/regression_proj/blob/main/figures/metrics_p1.png?raw=true)

- I also plot the `residual plot` with `Q-Q plot`:
![](https://github.com/luongtruong77/regression_proj/blob/main/figures/residual_plot.png?raw=true)

> Not too bad for preliminary model building!

