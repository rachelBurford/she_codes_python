from datetime import datetime
from types import DynamicClassAttribute
from typing import Counter

MAX_WIDTH = 20

def convert_mmddyyyy_date(date):
    '''Takes a date in the format mm/dd/yyyy and converts it to a datetime object.

    Args:
        date: string of a date in the mm/dd/yyyy format.

    Returns: a datetime object.
    '''
    return datetime.strptime(date, '%m/%d/%Y')



def get_month_name(date):
    '''Gets the month name from a datetime object.

    Args:
        date: a datetime object.

    Returns: the month name from the given date
        (e.g. "January", "February", etc).
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
    return f"{text:<{spaces}}"


def read_csv_file(file_name):
    '''Reads a csv file and returns the data as a list.

    Args:
        file_name: a string representing the path and name of a csv file.
        Returns: a list.
    '''
    
    import csv

    turtles = []

    with open(file_name, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            turtles.append(line)
    return turtles
   


def output_overall_statistics(monthly_data):
    '''Prints a summary of the total number of nests, hatched nests, false
        crawls, hit rocks and nest predation.

    Args:
        monthly_data: a list of lists, where each sublist contains the month
        name and total values for that month.
    '''
    nest = []
    best = []
    west = []
    lest = []
    test = []
    jest = []
    actions = [ "Month","Nests","Hatched Nests","False Crawls","Hit Rocks","Nest Predation" ]
 

    for month in monthly_data[1:]:
        nest.append(month["October"])
        best.append(month["November"])
        west.append(month["December"])
        lest.append(month["January"])
        test.append(month["February"])
        jest.append(month["March"])

    Nests = (nest[0]+best[0]+west[0]+lest[0]+test[0]+jest[0])
    Hatched = (nest[1]+best[1]+west[1]+lest[1]+test[1]+jest[1])
    Fal = (nest[2]+best[2]+west[2]+lest[2]+test[2]+jest[2])
    Hit = (nest[3]+best[3]+west[3]+lest[3]+test[3]+jest[3])
    Pred = (nest[4]+best[4]+west[4]+lest[4]+test[4]+jest[4])
    # print("Overall")
    # print(f" Nests           {Nests}")
    # print(f" Hatched Nests   {Hatched}")
    # print(f" False Crawls    {Fal}")
    # print(f" Hit Rocks       {Hit}")
    # print(f" Nest Predation  {Pred}")

    overall = ["Nests","Hatched Nests","False Crawls","Hit Rocks","Nest Predation"]
    

    # print(len(max_len))
    max_length = MAX_WIDTH


    #14

    print("Overall")
    # formatted_text = format_text("Nests",((max_length) - (len("Nests"))))
    print(f" {format_text('Nests',((max_length) - (len('Nests'))))} {Nests}")
    print(f" {format_text('Hatched Nests',((max_length) - (len('Hatched Nests'))))}   {Hatched}")
    print(f" {format_text('False Crawls',((max_length) - (len('False Crawls'))))}    {Fal}")
    print(f" {format_text('Hit Rocks',((max_length) - (len('Hit Rocks'))))}      {Hit}")
    print(f" {format_text('Nest Predation',((max_length) - (len('Nest Predation'))))}   {Pred}")

    
    # print(f" Nests {Nests}")
    # print(f" Hatched Nests{Hatched}")
    # print(f" False Crawls{Fal}")
    # print(f" Hit Rocks{Hit}")
    # print(f" Nest Predation{Pred}")



def output_monthly_statistics(monthly_data):
    '''Prints a summary of the total number of nests, hatched nests, false crawls,
       hit rocks and nest predation per month.

    Args:
        monthly_data: a list of lists, where each sublist contains the month
            name and total values for that month.
    '''
    nest = []
    best = []
    west = []
    lest = []
    test = []
    jest = []
    actions = [ "Month","Nests","Hatched Nests","False Crawls","Hit Rocks","Nest Predation" ]
 

    for month in monthly_data[1:]:
        nest.append(month["October"])
        best.append(month["November"])
        west.append(month["December"])
        lest.append(month["January"])
        test.append(month["February"])
        jest.append(month["March"])


    print("Montly Statistics")

    print(f"  {actions[0]}     {actions[1]}    {actions[2]}   {actions[3]} {actions[4]} {actions[5]}  ")    
    print(f"  October     {nest[0]}        {nest[1]}              {nest[2]}              {nest[3]}          {nest[4]}")
    print(f"  November    {best[0]}       {best[1]}             {best[2]}             {best[3]}          {best[4]}")
    print(f"  December    {west[0]}      {west[1]}             {west[2]}              {west[3]}          {west[4]}")
    print(f"  January     {lest[0]}       {lest[1]}              {lest[2]}              {lest[3]}          {lest[4]}")
    print(f"  February    {test[0]}         {test[1]}              {test[2]}              {test[3]}          {test[4]}")
    print(f"  March       {jest[0]}         {jest[1]}              {jest[2]}              {jest[3]}          {jest[4]}")



def output_nests_per_month_graph(monthly_data):
    '''Prints a graph of the total number of nests found per month.

    Args:
        monthly_data: a list of lists, where each sublist contains the month
            name and total values for that month.
    '''

    print("Number of Nests recorded per month (X = 5 nests):") 

    x = 5

    for month in monthly_data[1:2]:
        October = month["October"]
        November = month["November"]
        December = month["December"]
        January = month["January"]
        February = month["February"]
        March = month["March"]
    
    oct_chart = ""
    for num in range(0,October,x):
        oct_chart = oct_chart + "X"
    nov_chart = ""
    for num in range(0,November,x):
        nov_chart = nov_chart + "X"
    dec_chart = ""
    for num in range(0,December,x):
        dec_chart = dec_chart + "X"
    jan_chart = ""
    for num in range(0,January,x):
        jan_chart = jan_chart + "X"
    feb_chart = ""
    for num in range(0,February,x):
        feb_chart = feb_chart + "X"
    mar_chart = ""
    for num in range(0,March,x):
        mar_chart = mar_chart + "X"
    
    print(f"  October : {October} {oct_chart}")
    print(f"  November : {November} {nov_chart}")
    print(f"  December : {December} {dec_chart}")
    print(f"  January : {January} {jan_chart}")
    print(f"  February : {February} {feb_chart}")
    print(f"  March : {March} {mar_chart}")



def transform_daily_to_monthly(data):
    '''Transform the data from daily to monthly format.

    Args:
        data: a list of lists, where each sublist represents data
            for a specific day.

    Returns: a list of lists, where each sublist represents data
        for a whole month.

    call helper functions in the step2 and step2a - use a dictonary
    
    start with  a dictonay with maybe months

    do a for loop that changes to the right day and month uses helper functions
    def convert_mmddyyyy_date(date):
    get_month_name


    '''
    monthly = {}
    nest = {}
    false = {}
    rocks = {}
    hatched = {}
    disturbed = {}

    for day in data[1:]:
        date = convert_mmddyyyy_date(day[0])
 
        month = get_month_name(date)

        if month not in monthly.keys():
            monthly [month] = 0
            nest [month] = 0
            false [month] = 0
            rocks [month] = 0
            hatched [month] = 0
            disturbed [month] = 0
        nest [month] = nest[month]+int(day[1])
        false [month] = false[month]+int(day[2])
        rocks [month] = rocks[month]+int(day[3])
        hatched [month] = hatched[month]+int(day[4])
        disturbed [month] = disturbed[month]+int(day[5])


    return (monthly),(nest),(hatched),(false),(rocks),(disturbed)



   
if __name__ == "__main__":
    all_data = read_csv_file('./data/2020_2021_turtle_data.csv')

    monthly_data = transform_daily_to_monthly(all_data)

    print('2020/2021 Flatback Turtle Migration at Cemetery Beach')
    print()
    output_nests_per_month_graph(monthly_data)
    print()
    output_monthly_statistics(monthly_data)
    print()
    output_overall_statistics(monthly_data)
    print()
