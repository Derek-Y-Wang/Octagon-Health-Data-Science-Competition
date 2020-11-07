import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import mutual_info_classif
from sklearn.linear_model import LogisticRegression
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


def getMostCorrelatedColumns(data: pd.DataFrame):
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33,
                                                        random_state=1)

    # instantiate the OrdinalEncoder class to encode categorical input features
    oe = OrdinalEncoder()
    # fit the OrdinalEncoder class on training set
    oe.fit(X_train)
    # transform training and test sets and convert to DFs
    X_train_enc = pd.DataFrame(oe.transform(X_train), columns=X_train.columns)
    X_test_enc = pd.DataFrame(oe.transform(X_test), columns=X_test.columns)

    # instantiate the LabelEncoder class to encode the categorical target class
    le = LabelEncoder()
    # fit the LabelEncoder class on training set
    le.fit(y_train)
    # transform training and test target variables and convert to DFs
    y_train_enc = pd.DataFrame(le.transform(y_train))
    y_test_enc = pd.DataFrame(le.transform(y_test))

    # instantiate SelectKBest class to select the best 4 features
    # use score_func=mutual_info_classif for Mutual Information
    # Use k='all' to see the scores for all features
    fs = SelectKBest(score_func=chi2, k=4)
    # fit on training features and target
    fs.fit(X_train_enc, y_train_enc)
    # transform training and test features and convert to DFs. These will be fed to the ML algorithm for model training
    X_train_fs = pd.DataFrame(fs.transform(X_train_enc),
                              columns=X_train_enc.columns[fs.get_support()])
    X_test_fs = pd.DataFrame(fs.transform(X_test_enc),
                             columns=X_test_enc.columns[fs.get_support()])


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
    pass


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
