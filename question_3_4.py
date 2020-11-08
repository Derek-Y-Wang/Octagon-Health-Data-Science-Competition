import itertools

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import mutual_info_classif
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score

NUM_MONTHS = 40
MONTHS_COLUMN_START = 6
MONTHS_COLUMNS = ["M" + str(i) for i in range(NUM_MONTHS)]

def getDropOutForRow(data: pd.DataFrame, row: int):
    values = []

    for i in range(MONTHS_COLUMN_START, MONTHS_COLUMN_START + NUM_MONTHS, 1):
        values.append(data.iloc[row + 1, i]) # + data.iloc[row + 2, i]

    return values

def getDropoutRates(data: pd.DataFrame):
    values = [getDropOutForRow(data, 342)]
    columnData = pd.DataFrame(values, columns=MONTHS_COLUMNS)
    return columnData

def getNumberOfDropouts(data: pd.DataFrame, row: int):
    sum = 0

    for i in range(MONTHS_COLUMN_START, MONTHS_COLUMN_START + NUM_MONTHS, 1):
        sum += data.iloc[row + 1, i]

    return sum


def getNumberOfCensors(data: pd.DataFrame, row: int):
    sum = 0

    for i in range(MONTHS_COLUMN_START, MONTHS_COLUMN_START + NUM_MONTHS, 1):
        sum += data.iloc[row + 2, i]

    return sum


def selectKBestAndGetBestValues(data, X_train, X_train_enc, y_train_enc, k=1):
    fs1 = SelectKBest(score_func=chi2, k=k)
    fs1.fit(X_train_enc, y_train_enc)

    best_1 = []

    for i in range(4):
        if fs1.get_support()[i] == True:
            best_1.append(X_train.columns[i])

    oe_1 = OrdinalEncoder()
    raw_best_1 = np.array(data[best_1].to_numpy())
    oe_1.fit(raw_best_1)
    best_1_X = oe_1.transform(raw_best_1)

    transformed_Y = data.iloc[:, 4].to_list()
    model_1 = LinearRegression().fit(best_1_X, transformed_Y)

    stats = []
    category_combos = list(itertools.product(*oe_1.categories_))

    for combo in category_combos:
        input = oe_1.transform(np.asarray([combo]))
        stats.append(model_1.predict(input)[0])

    indices = [i for i in range(len(stats))]
    bestCombos = []

    for i in range(3):
        index = np.where(stats == np.max(stats))[0][0]
        bestCombos.append(category_combos[indices[index]])
        stats.pop(index)
        indices.pop(index)

    return best_1, bestCombos

def getMostCorrelatedColumns(data: pd.DataFrame):
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33,
                                                        random_state=1)

    oe = OrdinalEncoder()
    oe.fit(X_train)
    X_train_enc = pd.DataFrame(oe.transform(X_train), columns=X_train.columns)
    X_test_enc = pd.DataFrame(oe.transform(X_test), columns=X_test.columns)

    le = LabelEncoder()
    le.fit(y_train)
    y_train_enc = pd.DataFrame(le.transform(y_train))
    # y_test_enc = pd.DataFrame(le.transform(y_test))

    best_1, best_1_combos = selectKBestAndGetBestValues(data, X_train, X_train_enc, y_train_enc, k=1)
    best_2, best_2_combos = selectKBestAndGetBestValues(data, X_train, X_train_enc, y_train_enc, k=2)
    best_3, best_3_combos = selectKBestAndGetBestValues(data, X_train, X_train_enc, y_train_enc, k=3)

    print("* Most correlated column to discontinuation:")
    print(best_1)
    print("* Top 3 values for this column that get the highest discontinuation:")
    print(best_1_combos)

    print("* 2 most correlated columns to discontinuation:")
    print(best_2)
    print("* Top 3 values for these 2 columns that get the highest discontinuation:")
    print(best_2_combos)

    print("* 3 most correlated columns to discontinuation:")
    print(best_3)
    print("* Top 3 values for these 3 columns that get the highest discontinuation:")
    print(best_3_combos)

def findDiscontinuationReasons(data):
    values = []

    for i in range(0, len(data.index), 3):
        row = [data["Prov"].iloc[i], data["Con_ACT"].iloc[i], data["Sex"].iloc[i], data["Age"].iloc[i]]
        dropOuts = getNumberOfDropouts(data, i)
        row.append(dropOuts / data.iloc[i, MONTHS_COLUMN_START])
        values.append(row)

    # Average dropout = dropout / month
    columns = ["Prov", "Con_ACT", "Sex", "Age", "Average_Dropout"]
    discontinuationData = pd.DataFrame(values, columns=columns)
    print(discontinuationData)

    # Find the most correlated columns
    getMostCorrelatedColumns(discontinuationData)


def main():
    # This reads the data and sets up a dataframe.
    data = pd.read_excel('Octagon_data_set_TKI_2020.xlsx',
                         sheet_name="Data_Table")
    data = data[9:]
    del data['Unnamed: 0']
    cols = 'Prov	Con_ACT	Sex	Age	Measure	M0	M1	M2	M3	M4	M5	M6	M7	M8	M9	M10	M11	M12	M13	M14	M15	M16	M17	M18	M19	M20	M21	M22	M23	M24	M25	M26	M27	M28	M29	M30	M31	M32	M33	M34	M35	M36	M37	M38	M39'
    data.columns = cols.split('\t')
    data.reset_index(inplace=True)
    data = data.fillna(0)

    # Question 3
    print("====== Question 3 ======")
    # print(getDropoutRates(data))

    # Question 4
    print(findDiscontinuationReasons(data))


if __name__ == '__main__':
    main()
