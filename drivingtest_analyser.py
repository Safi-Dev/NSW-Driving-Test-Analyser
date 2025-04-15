import csv
from collections import defaultdict
# Note Data Sourced From https://opendata.transport.nsw.gov.au/data/dataset/transport-nsw-driver-licence-test-statistics/resource/417488f7-b266-455c-b921-c212082203a6?inner_span=True as at april 2025

def analyse_driving_test_data(filepath):
    """
    Analyses driving test data from a CSV file for 'C Driving Test'.

    Calculates:
    - Pass rates by Local Government Area (LGA)
    - Average attempts by LGA
    - Pass rates by Age Group
    - Pass rates by Gender

    Args:
        filepath (str): The path to the CSV file.

    Returns:
        tuple: A tuple containing dictionaries:
               (lga_analysis, age_analysis, gender_analysis)
               Returns (None, None, None) if analysis failed.
    """
    # Initialise dictionaries to store statistics
    lga_stats = defaultdict(lambda: {'total': 0, 'passes': 0, 'attempt_sum': 0})
    age_stats = defaultdict(lambda: {'total': 0, 'passes': 0})
    gender_stats = defaultdict(lambda: {'total': 0, 'passes': 0})

    try:
        with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter='|', quotechar='"')
            header = next(reader)
            print(f"CSV Header: {header}") # Verify header

            # Find column indices
            try:
                licence_type_col = header.index("LICENCE TEST TYPE")
                result_col = header.index("RESULT")
                lga_col = header.index("CUSTOMER ADDRESS LGA")
                attempt_col = header.index("ATTEMPT NUMBER")
                age_col = header.index("AGE GROUP")
                gender_col = header.index("GENDER")
            except ValueError as e:
                print(f"Error: Missing expected column in CSV header - {e}. ")
                return None, None, None

            # Process each row
            for row in reader:
                 if len(row) == len(header):
                    licence_test_type = row[licence_type_col]

                    # Filter for 'C Driving Test' only
                    if licence_test_type == "C Driving Test":
                        result = row[result_col]
                        lga = row[lga_col]
                        age_group = row[age_col]
                        gender = row[gender_col]

                        # Handle Attempt Number, defaulting to 1 if invalid
                        try:
                            attempt_num = int(row[attempt_col])
                        except ValueError:
                            attempt_num = 1

                        # Aggregate LGA Stats
                        if lga and lga != "Not Applicable":
                            lga_stats[lga]['total'] += 1
                            lga_stats[lga]['attempt_sum'] += attempt_num
                            if result == "Pass":
                                lga_stats[lga]['passes'] += 1

                        # Aggregate Age Group Stats
                        if age_group and age_group != "Not Applicable":
                            age_stats[age_group]['total'] += 1
                            if result == "Pass":
                                age_stats[age_group]['passes'] += 1

                        # Aggregate Gender Stats
                        if gender and gender != "Not Applicable":
                           gender_stats[gender]['total'] += 1
                           if result == "Pass":
                                gender_stats[gender]['passes'] += 1
                 else:
                     # Notify about rows that don't match the header length
                     print(f"Skipping malformed row: {row}")

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None, None, None
    except Exception as e:
        print(f"An error occurred during file processing: {e}")
        return None, None, None

    # Calculate final metrics
    lga_analysis = {}
    for lga, stats in lga_stats.items():
        pass_rate = (stats['passes'] / stats['total']) if stats['total'] > 0 else 0.0
        avg_attempts = (stats['attempt_sum'] / stats['total']) if stats['total'] > 0 else 0.0
        lga_analysis[lga] = {'pass_rate': pass_rate, 'avg_attempts': avg_attempts, 'total_tests': stats['total']}

    age_analysis = {}
    for age, stats in age_stats.items():
        pass_rate = (stats['passes'] / stats['total']) if stats['total'] > 0 else 0.0
        age_analysis[age] = {'pass_rate': pass_rate, 'total_tests': stats['total']}

    gender_analysis = {}
    for gen, stats in gender_stats.items():
        pass_rate = (stats['passes'] / stats['total']) if stats['total'] > 0 else 0.0
        gender_analysis[gen] = {'pass_rate': pass_rate, 'total_tests': stats['total']}

    # Return analysis results
    return lga_analysis, age_analysis, gender_analysis

def print_analysis_results(lga_analysis, age_analysis, gender_analysis):
    """Prints the calculated driving test analysis results."""

    print("\n--- C Driving Test Analysis ---")

    # LGA Analysis Results
    if lga_analysis:
        print("\n--- Analysis by LGA ---")
        # Sort alphabetically by LGA name for consistent output
        for lga in sorted(lga_analysis.keys()):
            stats = lga_analysis[lga]
            print(f"{lga}: Pass Rate={stats['pass_rate']:.2%}, Avg Attempts={stats['avg_attempts']:.2f} (Total Tests: {stats['total_tests']})")
    else:
        print("\nNo LGA data available.")

    # Age Group Analysis Results
    if age_analysis:
        print("\n--- Analysis by Age Group ---")
        # Sort by Age Group
        for age_group in sorted(age_analysis.keys()):
             stats = age_analysis[age_group]
             print(f"{age_group}: Pass Rate={stats['pass_rate']:.2%}, (Total Tests: {stats['total_tests']})")
    else:
        print("\nNo Age Group data available.")

    # Gender Analysis Results
    if gender_analysis:
        print("\n--- Analysis by Gender ---")
        # Sort by Gender
        for gender in sorted(gender_analysis.keys()):
             stats = gender_analysis[gender]
             print(f"{gender}: Pass Rate={stats['pass_rate']:.2%}, (Total Tests: {stats['total_tests']})")
    else:
        print("\nNo Gender data available.")

    print("\n-----------------------------")


# --- Main Script Execution ---
if __name__ == "__main__":
    # --- Configuration ---
    # IMPORTANT: Specify the correct path to your CSV file.
    # Use a raw string (r"...") or forward slashes (/) for Windows paths to avoid errors.

    csv_file_path = r"c:\path\to\your\TfNSW_Driver_Licence_Tests_date.csv"
    # --- End Configuration ---

    # Call the analysis function
    lga_data, age_data, gender_data = analyse_driving_test_data(csv_file_path)

    # Print the results if analysis was successful
    if lga_data is not None:
        print_analysis_results(lga_data, age_data, gender_data)
    else:
        print("Analysis could not be completed due to errors.")
