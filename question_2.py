from Constants import *
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.linear_model import LinearRegression

from SelectKBest import selectKBestAndGetBestValues


def getNumberOfSuccesses(data, row):
    sum = 0

    for i in range(MONTHS_COLUMN_START + 1, MONTHS_COLUMN_START + 10, 1):
        sum += data.iloc[row + 1, i]

    return sum

def addSuccessfulTherapyColumn(data):
    values = []

    for i in range(0, len(data.index), 3):
        row = [data["Prov"].iloc[i], data["Con_ACT"].iloc[i],
               data["Sex"].iloc[i], data["Age"].iloc[i]]

        if "ALL" in row:
            continue

        successes = getNumberOfSuccesses(data, i)
        row.append(successes / data.iloc[i, MONTHS_COLUMN_START])
        values.append(row)

    columns = ["Prov", "Con_ACT", "Sex", "Age", "Success_Rate"]
    successData = pd.DataFrame(values, columns=columns)
    return successData

def findMostCorrelatedColumns(data: pd.DataFrame):
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

    print("Please note that we are skipping rows with the \"ALL\" value.")
    print("* Most correlated column to success:")
    print(best_1)
    print("* Top 3 values for this column that get the highest success:")
    print(best_1_combos)

    print("* 2 most correlated columns to success:")
    print(best_2)
    print("* Top 3 values for these 2 columns that get the highest success:")
    print(best_2_combos)

    print("* 3 most correlated columns to success:")
    print(best_3)
    print("* Top 3 values for these 3 columns that get the highest success:")
    print("* Top 3 values for these 3 columns that get the highest success:")
    print(best_3_combos)

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
    print("====== Question 2 ======")
    data_successful_therapy = addSuccessfulTherapyColumn(data)
    findMostCorrelatedColumns(data_successful_therapy)


if __name__ == '__main__':
    main()
