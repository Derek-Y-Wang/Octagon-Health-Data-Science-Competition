import pandas as pd


def past_nine_months(df):

    print(df.loc[df['Measure']=='Tx'][['Prov','Con_ACT', 'Sex', 'Age', 'Measure','M9']])


if __name__ == '__main__':
    DATA = pd.read_excel('Octagon_data_set_TKI_2020.xlsx', sheet_name="Data_Table")
    DATA = DATA[9:]
    del DATA['Unnamed: 0']

    cols = 'Prov	Con_ACT	Sex	Age	Measure	M0	M1	M2	M3	M4	M5	M6	M7	M8	M9	M10	M11	M12	M13	M14	M15	M16	M17	M18	M19	M20	M21	M22	M23	M24	M25	M26	M27	M28	M29	M30	M31	M32	M33	M34	M35	M36	M37	M38	M39'
    DATA.columns = cols.split('\t')
    DATA.reset_index(inplace=True)

    past_nine_months(DATA)
