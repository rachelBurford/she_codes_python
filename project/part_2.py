import csv
import plotly.express as px
from datetime import datetime


def read_csv_file(file_name):
    '''Reads a csv file and returns the data as a list.

    Args:
        file_name: a string representing the path and name of a csv file.

    Returns: a list.
    '''
    pass


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


def output_total_summary(all_data):
    '''Prints a summary of the total number of nests, hatched nests,
    false crawls, hit rocks and nest predation.

    Args:
        all_data: a list of lists, where each sublist contains monthly data
        for the season.
    '''
    pass


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
    pass


def transform_daily_to_monthly(data, date_format):
    '''Transform the data from daily to monthly format.

    Args:
        data: a list of lists, where each sublist represents data
            for a specific day.

    Returns: a list of lists, where each sublist represents data
        for a whole month.
    '''
    pass


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
