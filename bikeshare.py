import time
import pandas as pd
import numpy as np

# ## City Data Dictionary
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# ## Get Filters: Asks user to specify city, month, and day
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city
    while True:
        city = input("Which city would you like to explore? (chicago, new york city, washington): ").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Invalid input. Please enter a valid city name (chicago, new york city, washington).")

    # Get user input for month
    while True:
        month = input("Which month would you like to explore? (january, february, march, april, may, june, or 'all'): ").lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Invalid month. Please choose from january, february, ..., june, or 'all'.")

    # Get user input for day of the week
    while True:
        day = input("Which day of the week would you like to explore? (monday, tuesday, ..., sunday, or 'all'): ").lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Invalid day. Please enter a valid day of the week (monday, tuesday, ..., sunday, or 'all').")

    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    """
    # Load data based on selected city
    df = pd.read_csv(CITY_DATA[city])

    # Ensure Start Time is converted to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month, day of the week, and hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour  # Extract hour from Start Time

    # Filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1  # Convert month to its respective number
        df = df[df['month'] == month]

    # Filter by day if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    # Check if the dataframe is empty after filtering
    if df.empty:
        print(f"No data available for {city.capitalize()} in {month} and on {day.title()}.")

    # Return the dataframe after filtering
    return df


def display_raw_data(df):
    """
    Asks the user if they want to see 5 rows of raw data, and continues until the user says 'no' or data is exhausted.
    """
    index = 0
    while True:
        # Ask the user if they want to see the next 5 rows of raw data
        show_data = input("Would you like to see 5 lines of raw data? Enter 'yes' or 'no': ").lower()
        
        if show_data == 'yes':
            # Show the next 5 rows of data
            print(df.iloc[index:index + 5])
            index += 5  # Increment index to show next 5 rows
            
            # Check if we have reached the end of the dataset
            if index >= len(df):
                print("You have reached the end of the data.")
                break
        elif show_data == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")



#This function time_stats calculates and displays the most frequent times of travel, including the most common month, day of the week, 
# and start hour for bike-share trips, based on the provided dataset.
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    most_common_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print(f"The most common month is: {months[most_common_month - 1]}")

    # Display the most common day of the week
    most_common_day = df['day_of_week'].mode()[0]
    print(f"The most common day of the week is: {most_common_day}")

    # Display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print(f"The most common start hour is: {most_common_hour}:00")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def station_stats(df):
    """Displays statistics on the most popular stations and trips."""
    
    print('\nCalculating the Most Popular Stations and Trips...\n')
    start_time = time.time()

    # Most common start station
    most_common_start_station = df['Start Station'].mode()[0]
    print(f"Most common start station: {most_common_start_station}")

    # Most common end station
    most_common_end_station = df['End Station'].mode()[0]
    print(f"Most common end station: {most_common_end_station}")

    # Most frequent combination of start and end station trip
    most_common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"Most common trip: {most_common_trip[0]} to {most_common_trip[1]}")

    # Output time taken for the calculations
    elapsed_time = time.time() - start_time
    print(f"\nThis took {elapsed_time:.2f} seconds.")
    print('-' * 40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time is: {total_travel_time} seconds")

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"Average travel time is: {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print("User types count:")
    print(user_type_counts)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nGender count:")
        print(gender_counts)
    else:
        print("\nGender data is not available.")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print(f"\nEarliest birth year: {earliest_birth_year}")
        print(f"Most recent birth year: {most_recent_birth_year}")
        print(f"Most common birth year: {most_common_birth_year}")
    else:
        print("\nBirth Year data is not available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Call the display_raw_data function to display raw data
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
