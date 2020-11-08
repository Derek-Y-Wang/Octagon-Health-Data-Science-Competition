import itertools
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.linear_model import LinearRegression

def selectKBestAndGetBestValues(data, X_train, X_train_enc, y_train_enc, k=1):
    # Finds the k most correlated columns to our output using the Chi-Squared
    # Test of Independence. The Chi-Squared test is used to determine the extent
    # of relationship or dependence between two categorical variables.
    fs1 = SelectKBest(score_func=chi2, k=k)
    fs1.fit(X_train_enc, y_train_enc)

    best_columns = []

    for i in range(4):
        if fs1.get_support()[i] == True:
            best_columns.append(X_train.columns[i])

    # This encodes our columns (x data).
    oe = OrdinalEncoder()
    raw_best_columns = np.array(data[best_columns].to_numpy())
    oe.fit(raw_best_columns)
    best_X = oe.transform(raw_best_columns)

    y = data.iloc[:, 4].to_list()
    model = LinearRegression().fit(best_X, y)

    stats = []
    category_combos = list(itertools.product(*oe.categories_))

    for combo in category_combos:
        input = oe.transform(np.asarray([combo]))
        stats.append(model.predict(input)[0])

    indices = [i for i in range(len(stats))]
    bestCombos = []

    for i in range(3):
        index = np.where(stats == np.max(stats))[0][0]
        bestCombos.append(category_combos[indices[index]])
        stats.pop(index)
        indices.pop(index)

    return best_columns, bestCombos
