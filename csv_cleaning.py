import csv
import pandas as pd

def csv_data_generate():
    # Simulated raw data
    data = [
        ["patient_id", "name", "age", "visit_date", "diagnosis"],
        [1, "John Doe", 28, "2024-12-01", "Flu"],
        [2, "", 35, "2025-01-15", "Cold"],
        [3, "Alice Smith", "", "2025-01-17", ""],
        [4, "David Lee", 41, "", "Allergy"],
        [5, "", "", "", ""],
        [6, "Mary Stone", 29, "2025-01-20", "Headache"]
    ]

    # Generate a CSV file with the specified columns and 1000 rows of data
    with open('patient_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for index, row in enumerate(data, start=1):
            try:
                writer.writerow(row)
            except Exception as e:
                print(f"Error writing row {index}: {row} - {e}")
                raise  # Re-raise the exception after logging
    
    print("patient_data.csv generated successfully.")

def impute_missing_values(df):
    df['name']= df['name'].fillna('Unknown')
    df['age']= df['age'].fillna(df['age'].mean().astype(int))
    df['visit_date']= df['visit_date'].fillna('Unknown').astype(str)
    df['diagnosis']= df['diagnosis'].fillna('Unknown')

    return df

def to_datetime(column, df):
    # Convert the specified column to datetime format
    df[column] = pd.to_datetime(df[column], errors='coerce')
    return df

def sort_asc(column, df):
    # Sort the DataFrame by the specified column in ascending order
    df = df.sort_values(by=column, ascending=True)
    return df

def csv_data_clean():
    # Read the CSV file
    df = pd.read_csv('patient_data.csv')
    # Remove full empty rows (patient_id is not empty)
    df = df.dropna(subset=['name', 'age', 'visit_date', 'diagnosis'], how='all')
    # Convert 'visit_date' to datetime format
    df = to_datetime('visit_date', df)
    # Imput missing values
    df = impute_missing_values(df)
    # Sort the DataFrame by 'visit_date' in ascending order
    df = sort_asc('visit_date', df)
    # add a new column 'needs_followup'
    df['needs_followup'] = df['diagnosis'].apply(lambda x: 'TRUE' if x == 'Unknown' else 'FALSE')

    # Save the cleaned data to a new CSV file
    df.to_csv('patient_data_cleaned.csv', index=False)
    print("patient_data_cleaned.csv generated successfully.")

def main():
    # Generate the CSV file
    #csv_data_generate()
    # Clean the CSV file
    csv_data_clean()

if __name__ == "__main__":
    main()