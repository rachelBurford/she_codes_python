import csv
from re import template
# import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from os import linesep


def read_csv_file(file_name):
    '''Reads a csv file and returns the data as a list.

    Args:
        file_name: a string representing the path and name of a csv file.

    Returns: a list.
    '''
    import csv

    turtles = []
    # count = 0

    with open(file_name, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            turtles.append(line)

    return turtles  


def convert_mmddyyyy_date(date):
    '''Takes a date in the format mm/dd/yyyy and converts it to a datetime object.

    Args:
        date: string of a date in the mm/dd/yyyy format.

    Returns: a datetime object.
    '''
    return datetime.strptime(date, '%m/%d/%Y')


def convert_ddmmyyyy_date(date):
    '''Takes a date in the format dd/mm/yyyy and converts it to a datetime object.

    Args:
        date: string of a date in the dd/mm/yyyy format.

    Returns: a datetime object.
    '''
    return datetime.strptime(date, '%d/%m/%Y')


def get_month_name(date):
    '''Gets the month name from a datetime object.

    Args:
        date: a datetime object.

    Returns: the month name from the given date
            (e.g. 'January', 'February', etc).
    '''
    return date.strftime('%B')


def format_text(text, spaces):
    '''Formats a string to be left aligned and take up a certain number of
    characters.

    Args:
        text: a string.
        spaces: the number of spaces the string should take up.

    Returns: the formatted string.
    '''
    return f'{text:<{spaces}}'

# 1
def output_total_summary(all_data):
    '''Prints a summary of the total number of nests, hatched nests,
    false crawls, hit rocks and nest predation.

    Args:
        all_data: a list of lists, where each sublist contains monthly data
        for the season.
    '''
    # for line in all_data:
    #     print(line)
    # print(all_data)
    month = ["October","November","December","January","February","March"]
    actions = ["Nests","Hatched Nests","False Crawls","Hit Rocks","Nest Predation"]

    max_len = 25
    
    out = [item for t in all_data for item in t]

    nests_19 = (out[1][f"{month[0]}"])+(out[1][f"{month[1]}"])+(out[1][f"{month[2]}"])+(out[1][f"{month[3]}"])+(out[1][f"{month[4]}"])
    f_crawls_19 = (out[2][f"{month[0]}"])+(out[2][f"{month[1]}"])+(out[2][f"{month[2]}"])+(out[2][f"{month[3]}"])+(out[2][f"{month[4]}"])
    hitrocks_19 = (out[3][f"{month[0]}"])+(out[3][f"{month[1]}"])+(out[3][f"{month[2]}"])+(out[3][f"{month[3]}"])+(out[3][f"{month[4]}"])
    hatched_19 = (out[4][f"{month[0]}"])+(out[4][f"{month[1]}"])+(out[4][f"{month[2]}"])+(out[4][f"{month[3]}"])+(out[4][f"{month[4]}"])
    nest_p_19 = (out[5][f"{month[0]}"])+(out[5][f"{month[1]}"])+(out[5][f"{month[2]}"])+(out[5][f"{month[3]}"])+(out[5][f"{month[4]}"])

    out = [item for t in all_data for item in t]


    # for num in range(6,10,1):

    nests_20 = (out[7][f"{month[0]}"])+(out[7][f"{month[1]}"])+(out[7][f"{month[2]}"])+(out[7][f"{month[3]}"])+(out[7][f"{month[4]}"])
    f_crawls_20 = (out[8][f"{month[0]}"])+(out[8][f"{month[1]}"])+(out[8][f"{month[2]}"])+(out[8][f"{month[3]}"])+(out[8][f"{month[4]}"])
    hitrocks_20 = (out[9][f"{month[0]}"])+(out[9][f"{month[1]}"])+(out[9][f"{month[2]}"])+(out[9][f"{month[3]}"])+(out[9][f"{month[4]}"])
    hatched_20 = (out[10][f"{month[0]}"])+(out[10][f"{month[1]}"])+(out[10][f"{month[2]}"])+(out[10][f"{month[3]}"])+(out[10][f"{month[4]}"])
    nest_p_20 = (out[11][f"{month[0]}"])+(out[11][f"{month[1]}"])+(out[11][f"{month[2]}"])+(out[11][f"{month[3]}"])+(out[11][f"{month[4]}"])
  
    
    overall_19 = []
    overall_19.append(nests_19)
    overall_19.append(hatched_19)
    overall_19.append(f_crawls_19)
    overall_19.append(hitrocks_19)
    overall_19.append(nest_p_19)

    overall_20 = []
    overall_20.append(nests_20)
    overall_20.append(hatched_20)
    overall_20.append(f_crawls_20)
    overall_20.append(hitrocks_20)
    overall_20.append(nest_p_20)

    # print(overall_19,overall_20)

    print("Overall:")
    # formatted_text = format_text("Nests",((max_length) - (len("Nests"))))
    print(f" {format_text('',20)}{format_text('2019/20',17)}{format_text('2020/21',17)}")
    print(f" {format_text('Nests',((max_len) - (len('Nests'))))}{format_text((nests_19),17)}{format_text((nests_20),17)}")
    print(f" {format_text('Hatched Nests',((max_len) - (len('Nests'))))}{format_text((hatched_19),17)}{format_text((hatched_20),17)}")
    print(f" {format_text('False Crawls',((max_len) - (len('Nests'))))}{format_text((f_crawls_19),17)}{format_text((f_crawls_20),17)}")
    print(f" {format_text('Hit Rocks',((max_len) - (len('Nests'))))}{format_text((hitrocks_19),17)}{format_text((hitrocks_20),17)}")
    print(f" {format_text('Nest Predation',((max_len) - (len('Nests'))))}{format_text((nest_p_19),17)}{format_text((nest_p_20),17)}")


    # return (overall_19),(overall_20)



#2
def generate_summary_graph(all_data):
    '''Outputs a graph of the total number of nests, hatched nests,
    false crawls, hit rocks and nest predation per season.

    Args:
        all_data: a list of lists, where each sublist contains monthly data
        for the season.
    '''
    month = ["October","November","December","January","February","March"]
    actions = ["Nests","Hatched Nests","False Crawls","Hit Rocks","Nest Predation"]
   
    out = [item for t in all_data for item in t]
    nests_19 = (out[1][f"{month[0]}"])+(out[1][f"{month[1]}"])+(out[1][f"{month[2]}"])+(out[1][f"{month[3]}"])+(out[1][f"{month[4]}"])
    f_crawls_19 = (out[2][f"{month[0]}"])+(out[2][f"{month[1]}"])+(out[2][f"{month[2]}"])+(out[2][f"{month[3]}"])+(out[2][f"{month[4]}"])
    hitrocks_19 = (out[3][f"{month[0]}"])+(out[3][f"{month[1]}"])+(out[3][f"{month[2]}"])+(out[3][f"{month[3]}"])+(out[3][f"{month[4]}"])
    hatched_19 = (out[4][f"{month[0]}"])+(out[4][f"{month[1]}"])+(out[4][f"{month[2]}"])+(out[4][f"{month[3]}"])+(out[4][f"{month[4]}"])
    nest_p_19 = (out[5][f"{month[0]}"])+(out[5][f"{month[1]}"])+(out[5][f"{month[2]}"])+(out[5][f"{month[3]}"])+(out[5][f"{month[4]}"])
    nests_20 = (out[7][f"{month[0]}"])+(out[7][f"{month[1]}"])+(out[7][f"{month[2]}"])+(out[7][f"{month[3]}"])+(out[7][f"{month[4]}"])
    f_crawls_20 = (out[8][f"{month[0]}"])+(out[8][f"{month[1]}"])+(out[8][f"{month[2]}"])+(out[8][f"{month[3]}"])+(out[8][f"{month[4]}"])
    hitrocks_20 = (out[9][f"{month[0]}"])+(out[9][f"{month[1]}"])+(out[9][f"{month[2]}"])+(out[9][f"{month[3]}"])+(out[9][f"{month[4]}"])
    hatched_20 = (out[10][f"{month[0]}"])+(out[10][f"{month[1]}"])+(out[10][f"{month[2]}"])+(out[10][f"{month[3]}"])+(out[10][f"{month[4]}"])
    nest_p_20 = (out[11][f"{month[0]}"])+(out[11][f"{month[1]}"])+(out[11][f"{month[2]}"])+(out[11][f"{month[3]}"])+(out[11][f"{month[4]}"])
  
    
    overall_19 = []
    overall_19.append(nests_19)
    overall_19.append(hatched_19)
    overall_19.append(f_crawls_19)
    overall_19.append(hitrocks_19)
    overall_19.append(nest_p_19)

    overall_20 = []
    overall_20.append(nests_20)
    overall_20.append(hatched_20)
    overall_20.append(f_crawls_20)
    overall_20.append(hitrocks_20)
    overall_20.append(nest_p_20)

    # print(overall_19,overall_20)

    fig = go.Figure(data=[
        go.Bar(
            name="2019",
            x=actions,
            y=overall_19
        ),
        go.Bar(
            name="2020",
            x=actions,
            y=overall_20
        )
    ])
    
    fig.update_layout(
        title="Overall Stats",
        xaxis_title="Statistic",
        yaxis_title="Number Recorded",
        legend_title="variable"
    )

    fig.write_html("overall_stats.html")
    # return (overall_19),(overall_20)

    pass


def generate_nests_per_month_graph(all_data):
    '''Prints a graph of the total number of nests found per month.

    Args:
        all_data: a list of lists, where each sublist contains monthly data
        for the season.
    '''
    twenty_19_nests = []
    twenty_20_nests = []

    for month in data_2019[1:2]:
        October = month["October"]
        November = month["November"]
        December = month["December"]
        January = month["January"]
        February = month["February"]
        March = 0
    
    
    # print(month)
    
    # print()

    for month in data_2020[1:2]:
        October_a = month["October"]
        November_a = month["November"]
        December_a = month["December"]
        January_a = month["January"]
        February_a = month["February"]
        March_a = month["March"]
         
    twenty_19_nests.append(October)
    twenty_19_nests.append(November)
    twenty_19_nests.append(December)
    twenty_19_nests.append(January)
    twenty_19_nests.append(February)
    twenty_19_nests.append(March)
    # print()
    # print()
    twenty_20_nests.append(October_a)
    twenty_20_nests.append(November_a)
    twenty_20_nests.append(December_a)
    twenty_20_nests.append(January_a)
    twenty_20_nests.append(February_a)
    twenty_20_nests.append(March_a)

    month = ["october","November","Dececember","January","February","March"]

    fig = go.Figure(data=[
        go.Scatter(
            name="Nests 19",
            x=month,
            y=twenty_19_nests
        ),
        go.Scatter(
            name="Nests 20",
            x=month,
            y=twenty_20_nests
        )
    ])
    fig.update_layout(
        title="Nests per Month",
        xaxis_title="Month",
        yaxis_title="Number Recorded",
        legend_title="variable"

    )

    fig.write_html("nests_monthly.html")



def transform_daily_to_monthly(data, date_format):
    '''Transform the data from daily to monthly format.

    Args:
        data: a list of lists, where each sublist represents data
            for a specific day.

    Returns: a list of lists, where each sublist represents data
        for a whole month.
    '''


    monthly = {}
    nest = {}
    filse = {}
    rocks = {}
    hatched = {}
    disturbed = {}

    for day in data:

        # print("test")
        # print(len(day))
        # print("test")

        if date_format == 'ddmmyyyy':
            date = convert_ddmmyyyy_date(day[0])
        else:
            date = convert_mmddyyyy_date(day[0])
        month = get_month_name(date)

        if month not in monthly.keys():
            monthly[month] = 0
            nest[month] = 0
            filse[month] = 0
            rocks[month] = 0
            hatched[month] = 0
            disturbed[month] = 0
        # print(month)
        # print(type(month))
        # nest[month] = nest[month] + int(day[1])

        if day[1]:
            nest[month] = nest[month] + int(day[1])
        else:
            day[1]= 0

        if day[2]:
            filse[month] = filse[month] + int(day[2])
        else:
            day[2]= 0

        if day[3]:
            rocks[month] = rocks[month]+int(day[3])
        else:
            day[3]= 0
        
        if day[4]:
            hatched[month] = hatched[month]+int(day[4])
        else:
            day[4]= 0

        if(len(day))==6:
            if day[5]:
                disturbed[month] = disturbed[month]+int(day[5])
            else:
                day[5]= 0

    return (monthly),(nest),(filse),(rocks),(hatched),(disturbed)


if __name__ == '__main__':

    raw_2019_data = read_csv_file('data/2019_2020_turtle_data.csv')
    raw_2019_data = raw_2019_data[2:]
    data_2019 = transform_daily_to_monthly(raw_2019_data, 'ddmmyyyy')

    raw_2020_data = read_csv_file('data/2020_2021_turtle_data.csv')
    raw_2020_data = raw_2020_data[1:]
    data_2020 = transform_daily_to_monthly(raw_2020_data, 'mmddyyyy')

    all_data = [data_2019, data_2020]
    output_total_summary(all_data)
    print()
    generate_nests_per_month_graph(all_data)
    print()
    generate_summary_graph(all_data)
    print()
