# Describe what is in the files

# Files contain data from NOAA CO-OPS (National Oceanic and Atmospheric Administration Center for Operational Oceanographic Products and Services)

# Data can be found at this link: https://tidesandcurrents.noaa.gov/products.html

# Files read in for this code are:
# "CO-OPS__CFR1624__cu.csv", "CO-OPS__8724580__ws.csv", "CO-OPS__8540433__ml.csv", "CO-OPS__8453662__vs.csv"

"""
from google.colab import files
uploaded = files.upload()

import pandas as pd
"""

# list of csv files

files = [
    "CO-OPS__CFR1624__cu.csv",
    "CO-OPS__8724580__ws.csv",
    "CO-OPS__8540433__ml.csv",
    "CO-OPS__8453662__vs.csv"
]

# for loop to read in list of csv files into dataframe and then print first few lines of each file

for file in files:
    print(f"--- {file} ---")
    try:
        df = pd.read_csv(file)
        print(df.info())
        print(df.head())
    except Exception as e:
        print(f"Error reading {file}: {e}")
    print("\n")


# Uncomment lines above in triple quotes if you need to read in the files again.

# Import libraries and load data
import pandas as pd
import matplotlib.pyplot as plt



# Extract Station IDs dynamically
current_station = ""
wind_station = ""
ml_station = ""
visibility_station = ""

# Loop through the files to find the correct parts of the filanemae and use that part to extract IDs
for file in files:
    # Split the filename by the double underscores "__"
    # Example: "CO-OPS__CFR1624__cu.csv" becomes ["CO-OPS", "CFR1624", "cu.csv"]
    parts = file.split('__')
    
    if "cu.csv" in file:
        current_station = parts[1]
    elif "ws.csv" in file:
        wind_station = parts[1]
    elif "ml.csv" in file:
        ml_station = parts[1]
    else:
        visibility_station = parts[1]

# Load the dataframes
# Note: Used skipinitialspace=True because many of these files have spaces in their headers
# index_col=False handles cases where there are more data columns than header columns
df_currents = pd.read_csv('CO-OPS__CFR1624__cu.csv', index_col=False, skipinitialspace=True)
df_wind = pd.read_csv('CO-OPS__8724580__ws.csv', index_col=False, skipinitialspace=True)
df_water = pd.read_csv('CO-OPS__8540433__ml.csv', index_col=False, skipinitialspace=True)
df_visibility = pd.read_csv('CO-OPS__8453662__vs.csv', index_col=False, skipinitialspace=True)


# Remove leading/trailing spaces
df_currents.columns = df_currents.columns.str.strip()
df_wind.columns = df_wind.columns.str.strip()
df_water.columns = df_water.columns.str.strip()
df_visibility.columns = df_visibility.columns.str.strip()


# Convert 'Date Time' columns to actual datetime objects for better plotting
# Skip df_water because ml.csv file does not contain a 'Date Time' column
df_currents['Date Time'] = pd.to_datetime(df_currents['Date Time'])
df_wind['Date Time'] = pd.to_datetime(df_wind['Date Time'])
df_visibility['Date Time'] = pd.to_datetime(df_visibility['Date Time'], usecols=[0, 1]) 
# By adding usecols=[0, 1] to pd.read_csv for vs.csv file, we explicitly ignore the extra trailing data that can cause a header mismatch.


# Plot High Frequency Current and Wind Data first

plt.figure(figsize=(14, 18)) # increased from plt.figure(figsize = (14, 6)) to fit 4 plots

fig, axes = plt.subplots(4, 1, figsize=(14, 22))

# Subplot 1: Current Speed
axes[0].plot(df_currents['Date Time'], df_currents['Speed'], color='blue', linewidth=0.5)
axes[0].set_title(f'Water Current Speed - Station {current_station}')
axes[0].set_ylabel('Speed (knots)')

# Subplot 2: Wind Speed and Gusts
axes[1].plot(df_wind['Date Time'], df_wind['Speed'], color='green', label='Wind Speed')
axes[1].plot(df_wind['Date Time'], df_wind['Gust'], color='orange', alpha=0.5, label='Wind Gust')
axes[1].set_title(f'Wind Speed and Gusts - Station {wind_station}')
axes[1].set_ylabel('Speed (m/s)')
axes[1].legend()

# Subplot 3: Monthly Water Levels
df_water['Label'] = df_water['Month'].astype(str) + "/" + df_water['Year'].astype(str)
axes[2].plot(df_water['Label'], df_water['Highest'], color='skyblue', label='Highest Level')
axes[2].plot(df_water['Label'], df_water['MSL'], color='red', marker='o', label='Mean Sea Level (MSL)')
axes[2].set_title(f'Monthly Water Levels - Station {ml_station}')
axes[2].set_ylabel('Level')
axes[2].legend()

# Subplot 4: Visibility
axes[3].plot(df_visibility['Date Time'], df_visibility['Visibility'], color='purple')
axes[3].set_title(f'Visibility Over Time - Station {visibility_station}')
axes[3].set_ylabel('Visibility')

##############################################################################################################
# Original subplot code, not optimal since it had bunched labels

# Subplot 1: Current Speed
#plt.subplot(4, 1, 1)
#plt.plot(df_currents['Date Time'], df_currents['Speed'], color='blue', label='Current Speed')
#plt.title(f'Water Current Speed Over Time for Station {current_station}')
#plt.ylabel('Current Speed')
#plt.legend()

# Subplot 2: Wind Speed and Gusts
#plt.subplot(4, 1, 2)
#plt.plot(df_wind['Date Time'], df_wind['Speed'], color='green', label='Wind Speed')
#plt.plot(df_wind['Date Time'], df_wind['Gust'], color='orange', alpha=0.5, label='Wind Gust')
#plt.title(f'Wind Speed and Gusts Over Time for Station {wind_station}')
#plt.ylabel('Speed')
#plt.legend()

# Subplot 3: Monthly Water Levels
# Create a string label for the Month/Year
#df_water['Label'] = df_water['Month'].astype(str) + "/" + df_water['Year'].astype(str)

#plt.subplot(4, 1, 3)
#plt.bar(df_water['Label'], df_water['Highest'], color='skyblue', label='Highest Water Level')
#plt.plot(df_water['Label'], df_water['MSL'], color='red', marker='o', label='Mean Sea Level (MSL)')
#plt.title(f'Monthly Water Level Extremes vs Mean Sea Level for station {ml_station}')
#plt.xlabel('Month/Year')
#plt.ylabel('Water Level')
#plt.legend()
#plt.xticks(rotation=45)

# Subplot 4: Visibility

#plt.subplot(4, 1, 4)
#plt.plot(df_visibility['Date Time'], df_visibility['Visibility'], color='purple')
#plt.title(f'Visibility Over Time for Station {visibility_station}')
#plt.xlabel('Date Time')
#plt.ylabel('Visibility')
#plt.grid(True, linestyle='--', alpha=0.7)
#plt.show()

#plt.tight_layout()
#plt.show()
