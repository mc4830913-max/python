##Ordinary Least Squares (OLS) Regression
##This section performs Ordinary Least Squares (OLS) regression using scikit-learn to find the optimal values for p (slope) and c (intercept) in a linfrom sklearn.linear_model import LinearRegression
import pandas as pd


work_experience = [12, 3,3, 25, 7, 18, 1, 30, 14, 9, 22,
                   5, 27, 16, 2, 20, 11, 6, 28, 15, 24,
                   8, 19, 4, 26, 13, 10, 21, 29, 17, 23]

salary = [109442, 44444, 15267, 203328, 73332, 152774, 30000, 239438, 123886, 87776, 181662,
          58888, 210550, 145552, 37222, 167218, 102220, 66110, 217772, 131108, 174440,
          80554, 159996, 51666, 196106, 116664, 94998, 188884, 232216, 138330, 166662]


df = pd.DataFrame()

df['work_exp'] = work_experience
df['salary'] = salary

df['means'] = df['salary']/df['work_exp']

p = (df['salary']/df['work_exp']).mean()

df.sort_values(by = 'work_exp')
##print(df)


from sklearn.linear_model import LinearRegression
import numpy as np

# Prepare the data for OLS
X = df['work_exp'].values.reshape(-1, 1) # Reshape to a 2D array
y = df['salary'].values

# Create and fit the OLS model
model = LinearRegression()
model.fit(X, y)

# Extract the slope (p) and intercept (c)
p_ols = model.coef_[0]
c_ols = model.intercept_

print(f"OLS Slope (p): {p_ols}")
print(f"OLS Intercept (c): {c_ols}")
##ear model (y = px + c) that predicts salary based on work_exp.


import plotly.express as px
import numpy as np

fig = px.scatter(df, x='work_exp', y='salary', title='Interactive_Salary vs. Work_Experience')
fig.update_layout(xaxis_title='Work Experience (Years)', yaxis_title='Salary',
                    xaxis=dict(gridcolor='gray'),
    yaxis=dict(gridcolor='gray'),
                    plot_bgcolor='black',     # inside plot area
    paper_bgcolor='black',    # whole figure background
    font=dict(color='green') )

p = 7000
c = 25000

# Generate points for the linear prediction model
x_years = np.arange(1, 31) # Work experience from 1 to 30

y_predicted = x_years * p_ols + c_ols

# Add the predicted line to the plot
fig.add_scatter(x=x_years, y=y_predicted, mode='lines', name='Predicted Salary (y = x * p)', line=dict(color='yellow'))

fig.show()












