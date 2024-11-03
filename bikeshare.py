import time
import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

MONTHS = {month: index for index, month in enumerate(['january', 'february', 'march', 
              'april', 'may', 'june', 'july', 'august', 'september', 
              'october', 'november', 'december'], start=1)}

DAYS = {day: index for index, day in enumerate(['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])}

def get_filters():
    print('Welcome to the bikeshare data analysis tool!')
    city = get_city_input()
    month = get_month_input()
    day = get_day_input()
    print('-' * 40)
    return city, month, day

def get_city_input():
    while True:
        city = input('Please select a city: Chicago, New York City, or Washington:\n').strip().lower()
        if city in CITY_DATA:
            return city
        print('Invalid selection. Choose from Chicago, New York City, or Washington.')

def get_month_input():
    while True:
        month = input("Enter the month (all, January, February, ..., December): ").strip().lower()
        if month in ['all'] + list(MONTHS.keys()):
            return month
        print('Invalid month. Please enter a valid month or "all".')

def get_day_input():
    while True:
        day = input("Enter the day (all, Monday, Tuesday, ..., Sunday): ").strip().lower()
        if day in ['all'] + list(DAYS.keys()):
            return day
        print('Invalid day. Please enter a valid day or "all".')

def load_data(city, month, day):
    print(f'\nLoading data for {city.title()}...')
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    if month != 'all':
        df = df[df['Start Time'].dt.month == MONTHS[month]]
        print(f'Filtered by month: {month.title()}')

    if day != 'all':
        df = df[df['Start Time'].dt.dayofweek == DAYS[day]]
        print(f'Filtered by day: {day.title()}')

    print('Data loaded successfully.\n')
    return df

def calculate_time_stats(df):
    print('\nCalculating the most frequent travel times...\n')
    start_time = time.time()

    common_month = df['Start Time'].dt.month.mode()[0]
    common_day = df['Start Time'].dt.dayofweek.mode()[0]
    common_hour = df['Start Time'].dt.hour.mode()[0]

    print(f'Most common month: {list(MONTHS.keys())[common_month - 1].title()}')
    print(f'Most common day: {list(DAYS.keys())[common_day].title()}')
    print(f'Most common hour: {common_hour}')

    print(f"\nTime stats calculation completed in {time.time() - start_time:.2f} seconds.")
    print('-' * 40)

def calculate_station_stats(df):
    print('\nFinding the most popular stations and trips...\n')
    start_time = time.time()

    common_start = df['Start Station'].mode()[0]
    common_end = df['End Station'].mode()[0]
    common_trip = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]

    print(f'Most popular start station: {common_start}')
    print(f'Most popular end station: {common_end}')
    print(f'Most common trip: {common_trip}')

    print(f"\nStation stats calculation completed in {time.time() - start_time:.2f} seconds.")
    print('-' * 40)

def calculate_trip_duration_stats(df):
    print('\nCalculating total trip durations...\n')
    start_time = time.time()

    total_time = df['Trip Duration'].sum()
    mean_time = df['Trip Duration'].mean()

    print(f'Total travel time: {total_time}')
    print(f'Average travel time: {mean_time:.2f}')

    print(f"\nTrip duration stats calculation completed in {time.time() - start_time:.2f} seconds.")
    print('-' * 40)

def calculate_user_stats(df):
    print('\nCompiling user statistics...\n')
    start_time = time.time()

    if 'User Type' in df:
        print('Counts of user types:\n', df['User Type'].value_counts())

    if 'Gender' in df:
        print('Counts of genders:\n', df['Gender'].value_counts())

    if 'Birth Year' in df:
        print('Earliest birth year:', int(df['Birth Year'].min()))
        print('Most recent birth year:', int(df['Birth Year'].max()))
        print('Most common birth year:', int(df['Birth Year'].mode()[0]))

    print(f"\nUser stats compilation completed in {time.time() - start_time:.2f} seconds.")
    print('-' * 40)

def display_data(df):
    start_loc = 0
    while True:
        view_data = input("Would you like to see 5 rows of trip data? Enter y/n: ").strip().lower()
        if view_data != 'y':
            break
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        if start_loc >= len(df):
            print("No more data to display.")
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        calculate_time_stats(df)
        calculate_station_stats(df)
        calculate_trip_duration_stats(df)
        calculate_user_stats(df)
        display_data(df)

        if input('\nWould you like to run the analysis again? (y/n): ').lower() != 'y':
            break

if __name__ == "__main__":
    main()
