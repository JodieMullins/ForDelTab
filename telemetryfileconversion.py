import pandas as pd

# read in json data to document
json_telemetry = pd.read_json('deldata/daikibo-telemetry-data.json')





# convert json to csv

csv_data = json_telemetry.copy()

csv_telemetry = csv_data.to_csv('deldata/telemetrydaikibo.csv', index=False)
