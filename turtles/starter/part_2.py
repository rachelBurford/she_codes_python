import csv
# import plotly.express as px
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
    # print(turtles)

        # for item in turtles:
        #     print(item)
        #     count = int(count) + 1
        #     print(count)
        # print(turtles[0])

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


#2
def generate_summary_graph(all_data):
    '''Outputs a graph of the total number of nests, hatched nests,
    false crawls, hit rocks and nest predation per season.

    Args:
        all_data: a list of lists, where each sublist contains monthly data
        for the season.
    '''
    pass


def generate_nests_per_month_graph(all_data):
    '''Prints a graph of the total number of nests found per month.

    Args:
        all_data: a list of lists, where each sublist contains monthly data
        for the season.
    '''

    for month in data_2019[1:2]:
        October = month["October"]
        November = month["November"]
        December = month["December"]
        January = month["January"]
        February = month["February"]
        March = 0
        
    print(month)
    
    print()

    for month in data_2020[1:2]:
        October_a = month["October"]
        November_a = month["November"]
        December_a = month["December"]
        January_a = month["January"]
        February_a = month["February"]
        March_a = month["March"]
         
    

    print(f"  October : {October}")
    print(f"  November : {November}")
    print(f"  December : {December}")
    print(f"  January : {January}")
    print(f"  February : {February}")
    print(f"  March : {March}")
    print()
    print()
    print(f"  October : {October_a}")
    print(f"  November : {November_a}")
    print(f"  December : {December_a}")
    print(f"  January : {January_a}")
    print(f"  February : {February_a}")
    print(f"  March : {March_a}")




    # print("data 2019:")
    # print(data_2019)
    # print()
    # print("data 20:")
    # print(data_2020)

    
    print()
    
    pass


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

        if date_format == 'ddmmyyyy':
            date = convert_ddmmyyyy_date(day[0])
        else:
            date = convert_mmddyyyy_date(day[0])
        month = get_month_name(date)

        # print(month)

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

        if(len(day))>6:
            if day[5]:
                disturbed[month] = disturbed[month]+int(day[5])
            else:
                day[5]= 0
             

        # # filse[month] = filse[month]+int(day[2])
        # print(day[3],"day3")
        # print(type(day[3]))
        # rocks [month] = rocks[month]+int(day[3])
        # hatched [month] = hatched[month]+int(day[4])
        # disturbed [month] = disturbed[month]+int(day[5])

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
