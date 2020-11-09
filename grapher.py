# Name: Plot Generator
# Date: 08/11/2020
# Authors: Robert Ciborowski, Derek Wang
# Description: This file generates some graphs of all types allowing us to
#              analyze data and make prediction and other findings that maybe
#              insightful.

import pandas as pd
import matplotlib.pyplot as plt


def plot_by_location(df):
    """
    Plot two graphs based on location numerically and by percentage
    :param df:
    :return:
    """
    regions = set()
    for index, row in df.iterrows():
        regions.add(row['Prov'])

    print(regions)
    regions.remove('ALL')
    plt.subplot(2, 1, 1)
    for prov in regions:
        x = df.loc[df['Measure'] == 'Tx']
        x = x.loc[df['Con_ACT'] == "ALL"]
        x = x.loc[df['Sex'] == 'ALL']
        x = x.loc[df['Age'] == 'ALL']
        x = x.loc[df['Prov'] == str(prov)]

        x = list(x.iloc[0, 6:].values)

        y = ['M' + str(i) for i in range(len(x))]

        plt.plot(y, x, label=prov)

    plt.xlabel("Months")
    plt.ylabel("Number of people")
    plt.title("People in the study LOCATION")
    plt.legend()

    plt.subplot(2, 1, 2)
    for prov in regions:
        x = df.loc[df['Measure'] == 'Tx']
        x = x.loc[df['Con_ACT'] == "ALL"]
        x = x.loc[df['Sex'] == 'ALL']
        x = x.loc[df['Age'] == 'ALL']
        x = x.loc[df['Prov'] == str(prov)]

        x1 = list(x.iloc[0, 6:].values)
        x = [x1[i]/x1[0] for i in range(len(x1))]
        y = ['M' + str(i) for i in range(len(x))]

        plt.plot(y, x, label=prov)

    plt.xlabel("Months")
    plt.ylabel("Percent of People")
    plt.title("Percent of People Remaining by LOCATION")

    plt.legend()
    plt.show()


def plot_by_con_act(df):
    """
    Plot graph based on people after each month based on changing Con_ACT
    :param df:
    :return:
    """
    others = set()
    for index, row in df.iterrows():
        others.add(row['Con_ACT'])

    others.remove('ALL')

    for con_act in others:
        x = df.loc[df['Measure'] == 'Tx']
        x = x.loc[df['Con_ACT'] == con_act]
        x = x.loc[df['Sex'] == 'ALL']
        x = x.loc[df['Age'] == 'ALL']
        x = x.loc[df['Prov'] == 'ALL']

        x = list(x.iloc[0, 6:].values)

        y = ['M' + str(i) for i in range(len(x))]

        plt.plot(y, x, label=con_act)

    plt.xlabel("Months")
    plt.ylabel("Number of people")
    plt.legend()
    plt.title("People in the study CON_ACT")
    plt.show()


def plot_by_sex(df):
    """
    Plot graph of people left each month based on sex
    :param df:
    :return:
    """
    sex = set()
    for index, row in df.iterrows():
        sex.add(row['Sex'])

    sex.remove("ALL")

    for s in sex:
        x = df.loc[df['Measure'] == 'Tx']
        x = x.loc[df['Con_ACT'] == 'ALL']
        x = x.loc[df['Sex'] == s]
        x = x.loc[df['Age'] == 'ALL']
        x = x.loc[df['Prov'] == 'ALL']

        x = list(x.iloc[0, 6:].values)

        y = ['M' + str(i) for i in range(len(x))]

        plt.plot(y, x, label=s)

    plt.xlabel("Months")
    plt.ylabel("Number of people")
    plt.title("People in the study SEX")
    plt.legend()
    plt.show()


def plot_by_age(df):
    """
    Plot graph of people left each month based on age

    :param df:
    :return:
    """
    age_group = set()
    for index, row in df.iterrows():
        age_group.add(row['Age'])

    age_group.remove("ALL")

    for age in age_group:
        x = df.loc[df['Measure'] == 'Tx']
        x = x.loc[df['Con_ACT'] == 'ALL']
        x = x.loc[df['Sex'] == "ALL"]
        x = x.loc[df['Age'] == age]
        x = x.loc[df['Prov'] == 'ALL']

        x = list(x.iloc[0, 6:].values)

        y = ['M' + str(i) for i in range(len(x))]

        plt.plot(y, x, label=age)

    plt.xlabel("Months")
    plt.ylabel("Number of people")
    plt.title("People in the study AGE")

    for age in age_group:
        x = df.loc[df['Measure'] == 'Tx']
        x = x.loc[df['Con_ACT'] == 'ALL']
        x = x.loc[df['Sex'] == "ALL"]
        x = x.loc[df['Age'] == age]
        x = x.loc[df['Prov'] == 'ALL']

        x = list(x.iloc[0, 6:].values)

        y = ['M' + str(i) for i in range(len(x))]

        plt.plot(y, x, label=age)
    plt.legend()
    plt.show()

# Not done
def age_pie(df):
    age_group = set()
    for index, row in df.iterrows():
        age_group.add(row['Age'])


    for age in age_group:
        x = df.loc[df['Measure'] == 'Tx']
        x = x.loc[df['Con_ACT'] == 'ALL']
        x = x.loc[df['Sex'] == "ALL"]
        x = x.loc[df['Age'] == age]
        x = x.loc[df['Prov'] == 'ALL']

        x = list(x.iloc[0, 6])
        print(x)


def avg_drop_rate(df):
    """
    Plots data in percentage of average drop rate each month and people left
    :param df:
    :return:
    """
    events = df.loc[df['Measure'] == 'events']
    events = events.loc[df['Sex'] == 'ALL']
    events = events.loc[df['Prov'] == 'ALL']
    events = events.loc[df['Sex'] == 'ALL']
    events = events.loc[df['Age'] == 'ALL']
    events = events.loc[df['Con_ACT'] == 'ALL']
    events = list(events.iloc[0, 6:].values)

    censor = df.loc[df['Measure'] == 'censored']
    censor = censor.loc[df['Sex'] == 'ALL']
    censor = censor.loc[df['Prov'] == 'ALL']
    censor = censor.loc[df['Sex'] == 'ALL']
    censor = censor.loc[df['Age'] == 'ALL']
    censor = censor.loc[df['Con_ACT'] == 'ALL']
    censor = list(censor.iloc[0, 6:].values)

    total_ppl = df.loc[df['Measure'] == 'Tx']
    total_ppl = total_ppl.loc[df['Sex'] == 'ALL']
    total_ppl = total_ppl.loc[df['Prov'] == 'ALL']
    total_ppl = total_ppl.loc[df['Sex'] == 'ALL']
    total_ppl = total_ppl.loc[df['Age'] == 'ALL']
    total_ppl = total_ppl.loc[df['Con_ACT'] == 'ALL']
    total_ppl = list(total_ppl.iloc[0, 6:].values)

    total_drop = []
    for i in range(len(events)):
        if not str(events[i]).isnumeric():
            events[i] = 0
        if not str(censor[i]).isnumeric():
            censor[i] = 0
        if not str(total_ppl[i]).isnumeric():
            total_ppl[i] = 0
        total_drop.append(events[i] + censor[i])

    y = ['M' + str(i) for i in range(len(total_ppl))]
    leave_percent = [0]
    event_percent = [0]
    censor_percent = [0]
    for i in range(1, len(y)):
        event_percent.append(events[i]/total_ppl[i-1])
        leave_percent.append(total_drop[i] / total_ppl[i - 1])
        censor_percent.append(censor[i] / total_ppl[i - 1])

    title="Monthly Discontinued/Event Rate"
    xlabel="Month"
    ylabel="Percent"
    x=event_percent
    plt.subplot(2, 1, 1)
    plt.plot(y, x)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    title2="Percent of People Left Monthly"
    xlabel2="Percent of People Left"
    plt.subplot(2, 1, 2)
    x=[total_ppl[i]/total_ppl[0] for i in range(len(total_ppl))]
    plt.plot(y, x)
    plt.title(title2)
    plt.xlabel(xlabel2)
    plt.ylabel(ylabel)
    plt.show()
    print(sum(x)/39)


def drop_count_bargraph(df):
    """
    Plot bar graph displaying people who leave each month along side
    reason for leaving (event or censored)
    :param df:
    :return:
    """
    # libraries
    import numpy as np
    events = df.loc[df['Measure'] == 'events']
    events = events.loc[df['Sex'] == 'ALL']
    events = events.loc[df['Prov'] == 'ALL']
    events = events.loc[df['Sex'] == 'ALL']
    events = events.loc[df['Age'] == 'ALL']
    events = events.loc[df['Con_ACT'] == 'ALL']
    events = list(events.iloc[0, 6:].values)

    censor = df.loc[df['Measure'] == 'censored']
    censor = censor.loc[df['Sex'] == 'ALL']
    censor = censor.loc[df['Prov'] == 'ALL']
    censor = censor.loc[df['Sex'] == 'ALL']
    censor = censor.loc[df['Age'] == 'ALL']
    censor = censor.loc[df['Con_ACT'] == 'ALL']
    censor = list(censor.iloc[0, 6:].values)

    total_drop = []
    for i in range(len(events)):
        if not str(events[i]).isnumeric():
            events[i] = 0
        if not str(censor[i]).isnumeric():
            censor[i] = 0
        total_drop.append(events[i] + censor[i])
    # set width of bar
    barWidth = 0.25

    # set height of bar

    bars1 = total_drop
    bars2 = events
    bars3 = censor

    # Set position of bar on X axis
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]

    # Make the plot
    plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white',
            label='Events + Censored')
    plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white',
            label='Events')
    plt.bar(r3, bars3, color='#fcca03', width=barWidth, edgecolor='white',
            label='Censored')

    # Add xticks on the middle of the group bars
    plt.xlabel('Months', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(bars1))],
               ['M' + str(i) for i in range(len(events))])

    plt.ylabel('Number of People', fontweight='bold')
    # Create legend & Show graphic
    plt.title('Number of patients discontinued each month')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    DATA = pd.read_excel('Octagon_data_set_TKI_2020.xlsx', sheet_name="Data_Table")
    DATA = DATA[9:]
    del DATA['Unnamed: 0']

    cols = 'Prov	Con_ACT	Sex	Age	Measure	M0	M1	M2	M3	M4	M5	M6	M7	M8	M9	M10	M11	M12	M13	M14	M15	M16	M17	M18	M19	M20	M21	M22	M23	M24	M25	M26	M27	M28	M29	M30	M31	M32	M33	M34	M35	M36	M37	M38	M39'
    DATA.columns = cols.split('\t')
    DATA.reset_index(inplace=True)

    plot_by_location(DATA)
    # plot_by_con_act(DATA)
    # plot_by_sex(DATA)
    # plot_by_age(DATA)
    # age_pie(DATA)
    # provincial_table(DATA)
    # drop_count_bargraph(DATA)
    # avg_drop_rate(DATA)
