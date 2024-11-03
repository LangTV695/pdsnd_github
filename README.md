
# Basic Data Exploration with Pandas on Bikeshare Data
_A Python project that utilizes pandas for analyzing bikeshare data._

## Project Overview

This project demonstrates the use of the pandas library along with basic statistical methods to conduct a descriptive analysis of bikeshare data from three prominent U.S. cities: **Chicago, Washington, and New York City**. The analysis provides insights into popular travel times, stations, trip durations, and user demographics, revealing trends like the busiest times of day and frequently used stations. 

## Table of Contents
- [Project Overview](#project-overview)
- [How to Run the Program](#how-to-run-the-program)
- [Program Functionality](#program-functionality)
- [Requirements](#requirements)
- [Project Data](#project-data)
- [Examples of Program Usage](#examples-of-program-usage)
- [Acknowledgments](#acknowledgments)

## How to Run the Program

To execute this program, enter the following command in your terminal:
```bash
python bikeshare.py
```

This guide assumes you're using **Anaconda's command prompt** on a **Windows 10 environment**. If using another environment, adjust the instructions accordingly. 

## Program Functionality

Upon running the program, users will be prompted to:
1. **Select a city** (Chicago, New York City, or Washington).
2. **Specify a month** for data filtering (e.g., January), or choose 'all' to include all months.
3. **Choose a day** of the week for filtering (e.g., Monday), or select 'all' to include all days.

The program will then display the following insights based on user choices:
- **Popular travel times**:
   - Most popular month
   - Most popular day of the week
   - Most popular hour of the day
- **Station statistics**:
   - Most frequented start station
   - Most frequented end station
   - Most common start-to-end station pair
- **Trip duration**:
   - Total duration of all trips
   - Average trip duration
- **User statistics**:
   - Count of users by type (e.g., subscribers and customers)
   - Count of users by gender (if data is available)
   - Age-related insights:
     - Oldest user (if data is available)
     - Youngest user (if data is available)
     - Most common birth year among users (if data is available)

The program will also ask if the user wants to **view the raw data**, initially displaying 5 rows. Users can continue to view more rows if desired.

Finally, users have the option to **restart the program** to analyze data for a different city, month, or day.

## Requirements

- **Python Version**: 3.6 or higher
- **Libraries**:
   - `pandas` - for data manipulation and analysis
   - `numpy` - for numerical operations
   - `time` - for tracking and formatting time-based operations

### Optional
Install the libraries using `pip`:
```bash
pip install pandas numpy
```

Or create a `requirements.txt` file and install them with:
```bash
pip install -r requirements.txt
```

## Project Data

The datasets are located in the `data` folder and sourced from Udacity. Each CSV file contains bikeshare data for a specific city, with attributes such as start time, end time, trip duration, start and end stations, and user information.

- **chicago.csv** - Contains bikeshare data for Chicago, including 'Gender' and 'Birth Year' data.
- **new_york_city.csv** - Contains bikeshare data for New York City, with 'Gender' and 'Birth Year' data.
- **washington.csv** - Contains bikeshare data for Washington. Note: This dataset does not include 'Gender' or 'Birth Year' information.

## Examples of Program Usage

Here's an example of how the program might proceed:
1. **User Input**:
   ```
   City: Chicago
   Month: June
   Day: Monday
   ```

2. **Output**:
   ```
   Most popular hour: 5 PM
   Most frequented start station: Streeter Dr & Grand Ave
   Most common user type: Subscriber
   Average trip duration: 12.6 minutes
   ```

3. **Prompt to View Raw Data**:
   ```
   Would you like to view raw data? Enter yes or no:
   ```

4. **Option to Restart**:
   ```
   Would you like to restart? Enter yes or no:
   ```

## Acknowledgments

This project is part of the Udacity Data Analyst Nanodegree program and uses bikeshare data provided by Motivate, a bike-sharing system provider for many major cities in the United States. Special thanks to Udacity for the guidance and resources.

---
