import pandas as pd
import matplotlib.pyplot as plt

file_path = 'data.csv'

df = pd.read_csv(file_path)
# Remove every row that includes faulty value
df = df[df != -1].dropna()
# Select each column from the DataFrame
status = df['status']
accident_index = df['accident_index']
accident_year = df['accident_year']
accident_reference = df['accident_reference']
vehicle_reference = df['vehicle_reference']
casualty_reference = df['casualty_reference']
casualty_class = df['casualty_class']
sex_of_casualty = df['sex_of_casualty']
age_of_casualty = df['age_of_casualty']
age_band_of_casualty = df['age_band_of_casualty']
casualty_severity = df['casualty_severity']
pedestrian_location = df['pedestrian_location']
pedestrian_movement = df['pedestrian_movement']
car_passenger = df['car_passenger']
bus_or_coach_passenger = df['bus_or_coach_passenger']
pedestrian_road_maintenance_worker = df['pedestrian_road_maintenance_worker']
casualty_type = df['casualty_type']
casualty_home_area_type = df['casualty_home_area_type']
casualty_imd_decile = df['casualty_imd_decile']
lsoa_of_casualty = df['lsoa_of_casualty']


plt.hist(age_of_casualty, bins='auto', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.show()



