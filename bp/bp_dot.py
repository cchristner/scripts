"""
Takes BP data from spreadsheet and draws a dot graph
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Define the file path
file_path = r"C:\Users\corey\OneDrive\health\health_data.xlsx"

# Load the Excel data into a DataFrame
df = pd.read_excel(file_path, usecols=['Date', 'Systolic', 'Diastolic'])

# Ensure Date is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Prepare data for dot graph
df['Date_num'] = mdates.date2num(df['Date'])

# Create the dot graph
fig, ax = plt.subplots()

# Plot Systolic and Diastolic data points
ax.plot(df['Date_num'], df['Systolic'], 'o', label='Systolic', color='blue')
ax.plot(df['Date_num'], df['Diastolic'], 'o', label='Diastolic', color='orange')

# Add vertical lines connecting Systolic and Diastolic points
for i in range(len(df)):
    ax.plot([df['Date_num'][i], df['Date_num'][i]], [df['Systolic'][i], df['Diastolic'][i]], color='black')

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
plt.title('Blood Pressure')

# Add a legend
plt.legend()

# Display the plot
plt.show()
