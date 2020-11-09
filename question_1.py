# Name: Question 1
# Date: 08/11/2020
# Authors: Robert Ciborowski, Derek Wang
# Description: Answers question 1 of the competition:
#              How many patients stay on treatment for at least 9 months?
#              We look at how many patients leave the program each month
#              generate a plot and look at remaining patients after at M9


import pandas as pd
import matplotlib.pyplot as plt


def past_nine_months(df):
    """
    Shows dataframe of all Tx measures and retenation rate after 9 months
    :param df:
    :return:
    """
    df = df.loc[df['Measure']=='Tx'][['Prov','Con_ACT', 'Sex', 'Age', 'Measure','M0', 'M9']]
    overall = df.loc[df['Prov']=='ALL'][['Prov','Con_ACT', 'Sex', 'Age', 'Measure', 'M0', 'M9']]

    overall = overall.loc[df['Sex']=='ALL'][['Prov','Con_ACT', 'Sex', 'Age', 'Measure', 'M0', 'M9']]
    overall = overall.loc[df['Age']=='ALL'][['Prov','Con_ACT', 'Sex', 'Age', 'Measure', 'M0','M9']]
    overall = overall.loc[df['Con_ACT'] == 'ALL'][['Prov', 'Con_ACT', 'Sex', 'Age', 'Measure', 'M0','M9']]
    # print(df.iloc[354])
    print("Overall left after 9 month")
    print(overall)
    print('================')

    new_col = []
    for index, row in df.iterrows():

        if row['M0'] == 'Nan':
            row['M0'] = 0
        if row['M9'] == 'Nan':
            row['M9'] = 0

        if row['M0'] == 0:
            new_col.append(0)
        else:
            new_col.append(row['M9']/row['M0'])
    df["%after 9months"] = new_col
    print(df)


def plot_for_all(df):
    """
    Plot data for participants remaining after each month.
    :param df:
    :return:
    """
    x = df.loc[df['Measure']=='Tx']
    x = x.loc[df['Sex']=='ALL']
    x = x.loc[df['Prov']=='ALL']
    x = x.loc[df['Sex']=='ALL']
    x = x.loc[df['Age']=='ALL']
    x = x.loc[df['Con_ACT']=='ALL']
    x = list(x.iloc[0, 6:].values)

    y = ['M' + str(i) for i in range(len(x))]

    plt.plot(y, x, label='ALL data')
    plt.xlabel("Months")
    plt.ylabel("Number of people")
    plt.title("People in the study ALL")
    plt.show()
    # print(x)


def main():
    DATA = pd.read_excel('Octagon_data_set_TKI_2020.xlsx',
                         sheet_name="Data_Table")
    DATA = DATA[9:]
    del DATA['Unnamed: 0']

    cols = 'Prov	Con_ACT	Sex	Age	Measure	M0	M1	M2	M3	M4	M5	M6	M7	M8	M9	M10	M11	M12	M13	M14	M15	M16	M17	M18	M19	M20	M21	M22	M23	M24	M25	M26	M27	M28	M29	M30	M31	M32	M33	M34	M35	M36	M37	M38	M39'
    DATA.columns = cols.split('\t')
    DATA.reset_index(inplace=True)

    past_nine_months(DATA)
    plot_for_all(DATA)


if __name__ == '__main__':
    main()
