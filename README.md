
# Basic Data Exploration with Pandas on Bikeshare Data
_A Python project that utilizes pandas for analyzing bikeshare data._

## Project Overview

This project demonstrates the use of the pandas library along with basic statistical methods to conduct a descriptive analysis of bikeshare data sourced from three prominent U.S. cities: Chicago, Washington, and New York City. The analysis reveals insights such as the most frequented days and the busiest stations.

### How to Run the Program

To execute this program, enter the following command in your terminal: `python bikeshare.py`. This guide assumes you're using Anaconda's command prompt on a Windows 10 environment.

### Program Functionality

The program prompts the user to select a city (e.g., Chicago), specify a month for data retrieval (e.g., January; with an option for 'all'), and choose a day for viewing data (e.g., Monday; also featuring an 'all' option).

After receiving the user inputs, it will inquire whether the user wants to view the raw data (initially displaying 5 rows). Based on the user's choices, the program will present the following insights:

- Most popular month
- Most popular day of the week
- Most popular hour of the day
- Most frequented start station
- Most frequented end station
- Most common pair of start and end stations
- Total duration of all trips
- Average trip duration
- Count of users by type
- Count of users by gender (if data is available)
- The oldest user (if data is available)
- The youngest user (if data is available)
- Most common birth year among users (if data is available)

Finally, users are given the option to restart the program.

## Requirements

- **Language**: Python 3.6 or higher
- **Libraries**: pandas, numpy, time

## Project Data

- **chicago.csv** - Located in the data folder, this dataset contains comprehensive bikeshare data for Chicago as provided by Udacity.

- **new_york_city.csv** - This dataset comprises bikeshare information for New York City, also sourced from Udacity.

- **washington.csv** - This file contains bikeshare data for Washington, provided by Udacity. Note: This dataset does not include 'Gender' or 'Birth Year' information.
