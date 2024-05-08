"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd

def cleanStats(frame):

    # Remove the 'FT' column
    frame = frame.drop('FT', axis=1)

    # Create new columns for makes and attempts for FG
    fg_makes = frame['FG'].where(frame['FG%'] == 'Make', 0)
    fg_attempts = frame['FG'].where(frame['FG%'] == 'Attempt', 1)

    # Insert the new columns into the DataFrame
    frame.insert(frame.columns.get_loc('FG%') + 1, 'FGM', fg_makes)
    frame.insert(frame.columns.get_loc('FG%') + 2, 'FGA', fg_attempts)

    # Create new columns for makes and attempts for 3PT
    three_makes = frame['3PT'].where(frame['3PT'] == 'Make', 0)
    three_attempts = frame['3PT'].where(frame['3PT'] == 'Attempt', 1)

    # Insert the new columns into the DataFrame
    frame.insert(frame.columns.get_loc('3PT') + 1, 'FG3M', three_makes)
    frame.insert(frame.columns.get_loc('3PT') + 2, 'FG3A', three_attempts)

    # Return the cleaned DataFrame
    return frame

def main():
    """Creates the data frame and view and starts the app."""
    frame = pd.read_csv("cleanbrogdonstats.csv")
    frame = cleanStats(frame)
    HoopStatsView(frame)


if __name__ == "__main__":
    main()
