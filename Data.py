import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os

# File path validation
while True:
    file_path = input('Enter the File path(type "data.csv" for default):')
    try:
        if not os.path.exists(file_path):
            print("File path does not exist.")
        else:
            print("File path is valid.")
            break
    except Exception as e:
        print(f"An error occurred: {e}")

# CSV file open
df = pd.read_csv(file_path)
df_clean = df[(df['age_of_casualty'] >= 0) & ((df['sex_of_casualty'] == 1) |
                                              (df['sex_of_casualty'] == 2))]

# Shape of the dataset
shape = df.shape
# Data types of the columns
data_types = df.dtypes
# Check for missing values
missing_values = df.isnull().sum()
# Descriptive statistics of the numerical columns
descriptive_stats = df.describe()
# Count of unique values for each column
unique_counts = df.nunique()
# Print the results
print("Description of the DataFrame")
print(shape, "--------------------")
print(data_types, "--------------------")
print(descriptive_stats, "--------------------")
print(unique_counts, "--------------------")
# Menu print
print('Analysis List :')
print('1. Distribution by Gender')
print('2. Distribution by Age')
print('3. Distribution by Severity')
print('4. Accident Severity by Casualty Class')
print('5. Severity by Sex Distribution')
print('6. Distribution of Casualty Home Area Type')
print('7. Severity by Home Area Type')
print('8. Distribution of Casualty class')
print('9. Distribution of Vehicle Type')
# While loop to keep the menu going
while True:
    # User input
    inp = input('Enter the Number of your desired analysis(enter anything '
                'else to end):')
    # If clauses for user inputs
    if inp == '1':
        plt.figure(figsize=(8, 6))
        sns.countplot(x='sex_of_casualty', data=df_clean)
        plt.title('Distribution of Accidents by Gender')
        plt.xlabel('Gender')
        plt.xticks([0, 1], ['Male', 'Female'])
        plt.show()
    elif inp == '2':
        plt.figure(figsize=(8, 6))
        sns.histplot(df_clean['age_of_casualty'], bins=10, kde=True)
        plt.title('Distribution of Age')
        plt.xlabel('Age')
        plt.show()
    elif inp == '3':
        plt.figure(figsize=(8, 6))
        sns.countplot(x='casualty_severity', data=df)
        plt.title('Distribution of Accident Severities')
        plt.xlabel('Casualty Severity')
        plt.show()
    elif inp == '4':
        plt.figure(figsize=(8, 6))
        sns.countplot(x='casualty_severity', hue='casualty_class', data=df)
        plt.title('Casualty Severity by Casualty Class')
        plt.xlabel('Casualty Severity')
        plt.legend(title='Casualty Class',
                   labels=['Driver', 'Passenger', 'Pedestrian'])
        plt.show()
    elif inp == '5':
        plt.figure(figsize=(8, 6))
        sns.countplot(x='casualty_severity', hue='sex_of_casualty', data=df)
        plt.title('Casualty Severity by Sex')
        plt.xlabel('Casualty Severity')
        plt.legend(title='Sex of Casualty',
                   labels=['Unknown', 'Male', 'Female'])
        plt.show()
    elif inp == '6':
        plt.figure(figsize=(8, 6))
        sns.countplot(x='casualty_home_area_type', data=df_clean)
        plt.title('Distribution of Accidents by Casualty Home Area Type')
        plt.xlabel('Home Area Type')
        plt.xticks([0, 1, 2], ['Urban', 'Semi-Urban', 'Rural'])
        plt.show()
    elif inp == '7':
        plt.figure(figsize=(8, 6))
        sns.countplot(x='casualty_home_area_type', hue='casualty_severity',
                      data=df)
        plt.title('Casualty Severity by Home Area Type')
        plt.xlabel('Casualty Severity')
        plt.legend(title='Home Area Type',
                   labels=['Unknown', 'Urban', 'Semi-Urban', 'Rural'])
        plt.show()
    elif inp == '8':
        plt.figure(figsize=(8, 6))
        sns.countplot(x='casualty_class', data=df)
        plt.title('Distribution of Casualty CLass')
        plt.xlabel('Casualty Class')
        plt.show()
    elif inp == '9':
        plt.figure(figsize=(10, 8))
        sns.countplot(x='vehicle_reference', data=df_clean)
        plt.title('Distribution of Vehicle Type Reference')
        plt.xlabel('Vehicle Type')
        plt.show()
    else:
        break
