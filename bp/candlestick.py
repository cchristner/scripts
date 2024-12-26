"""
Takes BP data from spreadsheet and draws a candlestick graph
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

# Define the file path
file_path = r"C:\Users\corey\OneDrive\health\health_data.xlsx"

# Load the Excel data into a DataFrame
df = pd.read_excel(file_path, usecols=['Date', 'Systolic', 'Diastolic'])

# Ensure Date is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Prepare data for candlestick chart
df['Date_num'] = mdates.date2num(df['Date'])
ohlc = df[['Date_num', 'Systolic', 'Diastolic', 'Systolic', 'Diastolic']]

# Create the candlestick chart
fig, ax = plt.subplots()
candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red')

# Format the date on the x-axis
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

# Add horizontal lines at 120 and 80
plt.axhline(y=120, color='black', linestyle='-')
plt.axhline(y=80, color='black', linestyle='-')

# Set labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Blood Pressure')
plt.title('Blood Pressure Candlestick Chart')

# Display the plot
plt.show()