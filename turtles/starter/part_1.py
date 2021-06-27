from datetime import datetime



def convert_mmddyyyy_date(date):
    '''Takes a date in the format mm/dd/yyyy and converts it to a datetime object.

    Args:
        date: string of a date in the mm/dd/yyyy format.

    Returns: a datetime object.
    '''
    for date in data[1:]:


    return datetime.strptime(date, '%m/%d/%Y')



def get_month_name(date):
    '''Gets the month name from a datetime object.

    Args:
        date: a datetime object.

    Returns: the month name from the given date
        (e.g. "January", "February", etc).
    '''
    for lines in turtles[1:]:
#     # print(lines)
#     # print(lines[0])
#     # print(type(lines[0]))
        dated = lines[0]
        date = (datetime.strptime(dated, '%m/%d/%Y'))
    # print(x)
        monthed = (date.strftime("%B"))

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
    dates = []
    nests = []
    crawls = []
    rocks = []
    hatched = []
    disterbed = []

    for line in all_data[1:]:
    # print(line)
        dates.append(line[0])
        nests.append(int(line[1]))
        crawls.append(int(line[2]))
        rocks.append(int(line[3]))
        hatched.append(int(line[4]))
        disterbed.append(int(line[5]))

    count_nests = sum(nests)
    count_crawls = sum(crawls)
    count_rocks = sum(rocks)
    count_hatched = sum(hatched)
    count_disterbed = sum(disterbed)
    print("Overall")
    print(f"Nests :{count_nests}")
    print(f"Hatched : {count_hatched}")
    print(f"Crawls : {count_crawls}")
    print(f"Rocks : {count_rocks}")
    print(f"Nest Predation :{count_disterbed}")
    pass


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
    pass



def transform_daily_to_monthly(data):
    '''Transform the data from daily to monthly format.

    Args:
        data: a list of lists, where each sublist represents data
            for a specific day.

    Returns: a list of lists, where each sublist represents data
        for a whole month.
    '''
   
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
