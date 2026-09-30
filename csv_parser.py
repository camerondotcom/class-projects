"""
Name: Cameron Chen
Course: CS242 | Fall 2026
Project: CSV Parser
Description:
    This script reads a CSV file and prints a summary of its contents.
    It shows the column names, the total number of rows, and the first
    few rows so you can quickly see what is in the file.
"""

import csv
import sys


def parse_csv(file_path):
    # Try to open the file and read it as a CSV
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

            # If the file has no data rows, let the user know
            if not rows:
                print("The CSV file is empty.")
                return

            # Print basic info about the file
            print("File:", file_path)
            print("Columns:", ", ".join(reader.fieldnames))
            print("Total rows:", len(rows))

            # Print the first 5 rows so the user can preview the data
            print("\nFirst 5 rows:")
            for row in rows[:5]:
                print(row)

    # Handle the case where the file does not exist
    except FileNotFoundError:
        print("Error: The file '" + file_path + "' was not found.")

    # Handle any other unexpected errors
    except Exception as e:
        print("An error occurred:", e)


# Only run the parser if this file is executed directly
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python csv_parser.py <file.csv>")
    else:
        parse_csv(sys.argv[1])
