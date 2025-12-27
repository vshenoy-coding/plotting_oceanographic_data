# Describe what is in the files

# Files contain data from NOAA CO-OPS (National Oceanic and Atmospheric Administration Center for Operational Oceanographic Products and Services)

# Data can be found at this link: https://tidesandcurrents.noaa.gov/products.html

# Files read in for this code are:
# "CO-OPS__CFR1624__cu.csv", "CO-OPS__8724580__ws.csv", "CO-OPS__8540433__ml.csv", "CO-OPS__8453662__vs.csv"

# CFR1624 is Station ID for Southport, northwest of Cape Fear, NC
# https://tidesandcurrents.noaa.gov/cdata/StationInfo?id=CFR1624

# 854033 is Station ID for Marcus Hook, PA in southeastern Delaware County, PA: https://tidesandcurrents.noaa.gov/stations.html?type=Water+Levels
# https://tidesandcurrents.noaa.gov/waterlevels.html?id=8540433
# CSV file obtained via Data Only > Export to CSV

# 8724580 is Station ID for Key West, FL, southernmost point in the Continental United States (CONUS)
# https://tidesandcurrents.noaa.gov/waterlevels.html?id=8724580

# 8453662 is Station ID for Providence Visibility, RI
# https://tidesandcurrents.noaa.gov/met.html?id=8453662

# cu: water current; ws: wind speed; ml: monthly mean water levels; vs: visibility
# cu data from 4/1/2016 12:00 AM EDT through 4/30/2016 11:54 PM EDT inclusive (6 minute intervals)
# ws data from 6/1/2021 12:00 AM EDT through 6/30/2021 10:00 AM EDT inclusive (6 minute intervals)
# ml data from 02/2022 through 02/2023 inclusive (1 month intervals)
# vs data from 3/31/2023 00:00 EDT through 3/31/2023 21:48 EDT (6 minute intervals)

# Upload files into Google Colab
from google.colab import files
uploaded = files.upload()

# import data frame to read in files
import pandas as pd

# create list of files
files = [
    "CO-OPS__CFR1624__cu.csv",
    "CO-OPS__8724580__ws.csv",
    "CO-OPS__8540433__ml.csv",
    "CO-OPS__8453662__vs.csv"
]

# use for loop to read in dataframe from each file in list of files
# and print information from the top of file
for file in files:
    print(f"--- {file} ---")
    try:
        df = pd.read_csv(file)
        print(df.info())
        print(df.head())
    except Exception as e:
        print(f"Error reading {file}: {e}")
    print("\n")



