from datetime import datetime
from types import DynamicClassAttribute
from typing import Counter


#step2
def convert_mmddyyyy_date(date):
    '''Takes a date in the format mm/dd/yyyy and converts it to a datetime object.

    Args:
        date: string of a date in the mm/dd/yyyy format.

    Returns: a datetime object.
    '''
    return datetime.strptime(date, '%m/%d/%Y')


#step2a
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

    #pass
    


def output_overall_statistics(monthly_data):
    '''Prints a summary of the total number of nests, hatched nests, false
        crawls, hit rocks and nest predation.

    Args:
        monthly_data: a list of lists, where each sublist contains the month
        name and total values for that month.
    '''
    # print(monthly_data)
    # dates = []
    # nests = []
    # crawls = []
    # rocks = []
    # hatched = []
    # disterbed = []

    # for line in monthly_data[1:]:
    # # print(line)
    #     dates.append(line[0])
    #     nests.append(int(line[1]))
    #     crawls.append(int(line[2]))
    #     rocks.append(int(line[3]))
    #     hatched.append(int(line[4]))
    #     disterbed.append(int(line[5]))

    # count_nests = sum(nests)
    # count_crawls = sum(crawls)
    # count_rocks = sum(rocks)
    # count_hatched = sum(hatched)
    # count_disterbed = sum(disterbed)
    # print("Overall")
    # print(f"Nests :{count_nests}")
    # print(f"Hatched : {count_hatched}")
    # print(f"Crawls : {count_crawls}")
    # print(f"Rocks : {count_rocks}")
    # print(f"Nest Predation :{count_disterbed}")
    # pass


def output_monthly_statistics(monthly_data):
    '''Prints a summary of the total number of nests, hatched nests, false crawls,
       hit rocks and nest predation per month.

    Args:
        monthly_data: a list of lists, where each sublist contains the month
            name and total values for that month.
    '''
   
    # pass


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


    # print(C_Oct)

        # monthly [month] = 0
        # nest [month] = 0
        # false [month] = 0
        # rocks [month] = 0
        # hatched [month] = 0
        # disturbed [month] = 0
        # nest [month] = nest[month]+int(month[1])
        # false [month] = false[month]+int(month[2])
        # rocks [month] = rocks[month]+int(month[3])
        # hatched [month] = hatched[month]+int(month[4])
        # disturbed [month] = disturbed[month]+int(month[5])
    # print(monthly)
    




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
        # print(date)
        month = get_month_name(date)
        # print(month)
        # print(f"{items[1]}: {items[0]},{items[2]}")
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

        # print(month,day[1])
        # print(day[1])
    # print(f"monthly{monthly}")
    # print(nest)
    # print(f"false{false}")
    # print(rocks)
    # print(hatched)


    # for line in data[1:]:
    #     date = convert_mmddyyyy_date(day[0])
    #     # print(date)
    #     month = get_month_name(date)
    #     # print(month)
    #     # print(f"{items[1]}: {items[0]},{items[2]}")
    #     print(line)
        
    
        # print(month,day[1])
        # print(day[1])
        # print(monthly)

    return (monthly),(nest),(false),(rocks),(hatched)

    # for day in data:    
    #     monthly[month] = monthly[month] + [day[1:6]]
    # print(monthly)
    # for month in monthly.keys():
    #     days = monthly[month]
    #     nests = 0
    #     false_crawls = 0
    #     hit_rocks = 0
    #     hatched_nests = 0
    #     nest_pred = 0
    #     for day in days:
    #         nests += int(day[0])
    #         false_crawls += int(day[1])
    #         hit_rocks += int(day[2])
    #         hatched_nests += int(day[3])
    #         nest_pred += int(day[4])
    #     print([month, nests, hatched_nests, false_crawls, hit_rocks, nest_pred])
    # return [month, nests, hatched_nests, false_crawls, hit_rocks, nest_pred]

    

   
if __name__ == "__main__":
    all_data = read_csv_file('./data/2020_2021_turtle_data.csv')
    # print(all_data)

    monthly_data = transform_daily_to_monthly(all_data)

    print('2020/2021 Flatback Turtle Migration at Cemetery Beach')
    print()
    output_nests_per_month_graph(monthly_data)
    print()
    output_monthly_statistics(monthly_data)
    print()
    output_overall_statistics(monthly_data)
    print()
    #print(all_data)
    # print(monthly_data)