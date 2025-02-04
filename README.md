# Bikeshare Data Analysis

This project is a Python-based analysis of US bikeshare data for three cities: Chicago, New York City, and Washington. The program loads data for a specific city and provides various statistics based on user input, such as the most frequent times of travel, popular stations, and user demographics.

## Requirements
- Python 3.x
- Pandas
- Numpy

## How to Run
1. Clone this repository.
2. Install the necessary libraries:
   ```bash
   pip install -r requirements.txt
   
Bike Share Data Analysis
Project Overview
This project allows you to explore and analyze bike share usage data from three major cities in the United States: Chicago, New York City, and Washington, D.C.. The data provides insights into bike-sharing system usage patterns, including the most common times for travel, popular stations, trip durations, and demographic information about users. The goal is to help stakeholders better understand the trends and behaviors of bike-share users.
Data Overview
The dataset consists of data collected over the first six months of 2017. The data files contain the following columns:
	•	Start Time: The start timestamp for the bike trip (e.g., 2017-01-01 00:07:57).
	•	End Time: The end timestamp for the bike trip (e.g., 2017-01-01 00:20:53).
	•	Trip Duration: Duration of the trip in seconds (e.g., 776).
	•	Start Station: The name of the station where the bike was picked up (e.g., Broadway & Barry Ave).
	•	End Station: The name of the station where the bike was returned (e.g., Sedgwick St & North Ave).
	•	User Type: The type of user (Subscriber or Customer).
	•	Gender (for Chicago and New York City): The gender of the user (Male, Female).
	•	Birth Year (for Chicago and New York City): The birth year of the user.
Functionality
The program provides the following features:
1. City, Month, and Day Filters
Users can select a city, a month, and a day of the week to filter the data based on their preferences.
2. Time Statistics
Displays statistics on the most frequent times of travel, such as:
	•	The most common month
	•	The most common day of the week
	•	The most common start hour
3. Station Statistics
Displays statistics on the most popular stations and trips, such as:
	•	The most commonly used start station
	•	The most commonly used end station
	•	The most frequent combination of start and end stations
4. Trip Duration Statistics
Displays statistics on the total and average trip duration, such as:
	•	Total travel time
	•	Average travel time
5. User Statistics
Displays statistics on bikeshare users, such as:
	•	Counts of user types (Subscribers and Customers)
	•	Counts of genders (for Chicago and New York City)
	•	Earliest, most recent, and most common birth years (for Chicago and New York City)
6. Restart Option
After displaying the results for a selected city, month, and day, the program prompts the user to restart the process with different parameters if desired.
Requirements
To run this project, you will need:
	•	Python 3.x or later
	•	pandas: Data analysis library used for data manipulation.
	•	numpy: Library for numerical operations.
	•	time: Library for measuring execution time.
You can install the required libraries by running:

pip install pandas numpy
How to Run the Project
	1	Clone or download the project repository to your local machine.
	2	Make sure you have the required CSV data files for the cities (chicago.csv, new_york_city.csv, washington.csv) in the same directory as the script.
	3	Run the Python script:

python bikeshare_2.py
	4	Follow the prompts in the terminal to explore the bike share data:
	◦	Select a city (chicago, new york city, washington)
	◦	Select a month (january, february, march, ..., june, or 'all')
	◦	Select a day of the week (monday, tuesday, ..., sunday, or 'all')
	5	The program will output the statistics based on your selections and will ask if you'd like to restart the process.
Example Output
The program will display results similar to the following:
Which city would you like to explore? (chicago, new york city, washington): chicago
Which month would you like to explore? (january, february, march, april, may, june, or 'all'): may
Which day of the week would you like to explore? (monday, tuesday, ..., sunday, or 'all'): monday
----------------------------------------

Calculating The Most Frequent Times of Travel...
The most common month is: May
The most common day of the week is: Monday
The most common start hour is: 17:00
This took 0.002 seconds.
----------------------------------------

Calculating The Most Popular Stations and Trip...
The most common start station is: Streeter Dr & Grand Ave
The most common end station is: Streeter Dr & Grand Ave
The most common trip is from Lake Shore Dr & Monroe St to Streeter Dr & Grand Ave
This took 0.005 seconds.
----------------------------------------

Calculating Trip Duration...
Total travel time is: 12697151 seconds
Average travel time is: 1051.09 seconds
This took 0.0001 seconds.
----------------------------------------

Calculating User Stats...
User types count:
Subscriber: 8962
Customer: 3118
Gender count:
Male: 6717
Female: 2246
Earliest birth year: 1906
Most recent birth year: 2001
Most common birth year: 1989
This took 0.002 seconds.
----------------------------------------

Would you like to restart? Enter yes or no.
Contributing
Feel free to fork this repository and contribute! If you have any suggestions or bug fixes, please submit a pull request. You can also open issues for any bugs or questions related to the project.
