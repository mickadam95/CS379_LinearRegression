#Adam Mick CS 379 Indiviual project 2 

import pandas as pd

def main():

    from sklearn.linear_model import LinearRegression

    taxData = pd.read_excel("dataset.xls", usecols=['TaxAmount']) #reading the tax amount from the dataset
    yearData = pd.read_excel("dataset.xls", usecols=['FiscalYear'])#Read the year data from the dataset


    y = taxData.iloc[:, :1].values #cleaning the data
    x = yearData.iloc[:, :1].values

    from sklearn.linear_model import LinearRegression

    regression = LinearRegression() #creating our linear regression
    regression.fit(x, y) #fit the data
    r_sq = regression.score(x, y)
    print("Coefficient of determination:", r_sq) #the results
    print("Intercept: ", regression.intercept_)
    print("Slope: ", regression.coef_)


    y_pred = regression.predict(x)
    print("Predicted response: ", y_pred, sep='\n')

    return 

main()

