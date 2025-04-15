# NSW Driving Test Analyser

## Description

This Python script analyses driver licence test data from Transport for NSW (TfNSW), provided in a specific CSV format. It focuses on Class C driving tests, calculating and presenting various statistics like pass rates and average attempts across different demographic breakdowns (LGA, Age Group, Gender).

## Features

* Analyses Class C driving test results from a pipe-delimited CSV file.
* Calculates pass rates by Local Government Area (LGA).
* Calculates the average number of attempts per test by LGA.
* Calculates pass rates by age group.
* Calculates pass rates by gender.
* Prints a summary of the analysis to the console.

## Requirements

* Python 3.x
* Standard Python libraries (`csv`, `collections`) - no external packages needed.

## Input Data Format

The script expects a CSV file delimited by pipes (`|`) with the following header columns:
LICENCE TEST REPORTING CATEGORY|PARENT LICENCE TEST TYPE|LICENCE TEST TYPE|GENDER|AGE GROUP|RESULT|ATTEMPT NUMBER|TEST LANGUAGE|INTERPRETER LANGUAGE|CUSTOMER ADDRESS LGA|COUNT

Example Row:
"C Class Driving Test"|"Driving Test"|"C Driving Test"|"Female"|"16-17"|"Pass"|"3"|"Not Applicable"|"Not Applicable"|"Randwick"|"<=5"

*(Note: The script currently focuses on rows where `LICENCE TEST TYPE` is `"C Driving Test"`)*

## Usage
Data Source: https://opendata.transport.nsw.gov.au/data/dataset/transport-nsw-driver-licence-test-statistics/resource/417488f7-b266-455c-b921-c212082203a6?inner_span=True
1.  **Save the Script:** Download or save the Python code as `drivingtest_analyser.py` (or your preferred name).
2.  **Place your Data:** Ensure the TfNSW driver licence test CSV file is accessible on your computer.
3.  **Configure File Path:** Open the script (`drivingtest_analyser.py`) in a text editor and **modify the `csv_file_path` variable** within the `# --- Configuration ---` section to point to the exact location of your CSV file. Remember to use a raw string (`r"..."`) or forward slashes (`/`) for the path if you are on Windows:

    ```python
    # --- Configuration ---
    # IMPORTANT: Specify the correct path to your CSV file.
    # Use a raw string (r"...") or forward slashes (/) for Windows paths to avoid errors.
    csv_file_path = r"c:\path\to\your\TfNSW_Data.csv"
    # --- End Configuration ---
    ```

4.  **Run the Script:** Open a terminal or command prompt, navigate to the directory where you saved the script, and run it using:

    ```bash
    python drivingtest_analyser.py
    ```

## Output

The script will print the analysis results directly to your terminal, including:

1.  Confirmation of the CSV header found.
2.  A breakdown of C Driving Test results by LGA, showing:
    * Pass Rate (percentage)
    * Average Attempts (decimal)
    * Total Tests counted for that LGA
3.  A breakdown by Age Group, showing Pass Rate and Total Tests.
4.  A breakdown by Gender, showing Pass Rate and Total Tests.

*(Any rows skipped due to formatting issues will also be noted in the output.)*
 ```EXAMPLE OUTPUT FOR MARCH 2025
--- C Driving Test Analysis ---

--- Analysis by LGA ---
Albury: Pass Rate=56.52%, Avg Attempts=1.57 (Total Tests: 46)
Armidale Regional: Pass Rate=58.33%, Avg Attempts=1.58 (Total Tests: 48)
Ballina: Pass Rate=65.62%, Avg Attempts=1.34 (Total Tests: 32)
Balranald: Pass Rate=54.55%, Avg Attempts=1.36 (Total Tests: 11)
Bathurst Regional: Pass Rate=59.65%, Avg Attempts=1.68 (Total Tests: 57)
Bayside: Pass Rate=47.92%, Avg Attempts=2.08 (Total Tests: 144)
Bega Valley: Pass Rate=51.28%, Avg Attempts=1.64 (Total Tests: 39)
Bellingen: Pass Rate=60.00%, Avg Attempts=1.60 (Total Tests: 10)
Berrigan: Pass Rate=66.67%, Avg Attempts=1.83 (Total Tests: 18)
Blacktown: Pass Rate=48.33%, Avg Attempts=2.16 (Total Tests: 180)
Bland: Pass Rate=42.86%, Avg Attempts=1.50 (Total Tests: 14)
Blayney: Pass Rate=85.71%, Avg Attempts=1.29 (Total Tests: 7)
Blue Mountains: Pass Rate=55.00%, Avg Attempts=1.75 (Total Tests: 40)
Bogan: Pass Rate=41.67%, Avg Attempts=1.25 (Total Tests: 12)
Bourke: Pass Rate=37.50%, Avg Attempts=1.12 (Total Tests: 8)
Brewarrina: Pass Rate=0.00%, Avg Attempts=1.00 (Total Tests: 1)
Broken Hill: Pass Rate=57.89%, Avg Attempts=1.47 (Total Tests: 19)
Burwood: Pass Rate=43.64%, Avg Attempts=2.07 (Total Tests: 110)
Byron: Pass Rate=55.26%, Avg Attempts=1.71 (Total Tests: 38)
Cabonne: Pass Rate=50.00%, Avg Attempts=2.01 (Total Tests: 98)
Camden: Pass Rate=46.59%, Avg Attempts=1.98 (Total Tests: 88)
Campbelltown: Pass Rate=47.24%, Avg Attempts=2.06 (Total Tests: 127)
Canada Bay: Pass Rate=44.44%, Avg Attempts=2.11 (Total Tests: 126)
Canterbury-Bankstown: Pass Rate=46.74%, Avg Attempts=2.14 (Total Tests: 184)
Carrathool: Pass Rate=33.33%, Avg Attempts=1.33 (Total Tests: 6)
Central Coast: Pass Rate=52.46%, Avg Attempts=2.08 (Total Tests: 122)
Central Darling: Pass Rate=75.00%, Avg Attempts=1.50 (Total Tests: 4)
Cessnock: Pass Rate=57.89%, Avg Attempts=1.88 (Total Tests: 57)
Clarence Valley: Pass Rate=48.98%, Avg Attempts=1.65 (Total Tests: 49)
Cobar: Pass Rate=41.67%, Avg Attempts=1.25 (Total Tests: 12)
Coffs Harbour: Pass Rate=48.00%, Avg Attempts=2.00 (Total Tests: 75)
Coolamon: Pass Rate=57.14%, Avg Attempts=1.36 (Total Tests: 14)
Coonamble: Pass Rate=57.14%, Avg Attempts=1.71 (Total Tests: 7)
Cootamundra-Gundagai Regional: Pass Rate=51.72%, Avg Attempts=1.55 (Total Tests: 29)
Cowra: Pass Rate=52.38%, Avg Attempts=1.76 (Total Tests: 21)
Cumberland: Pass Rate=45.83%, Avg Attempts=2.19 (Total Tests: 192)
Dubbo Regional: Pass Rate=49.38%, Avg Attempts=1.98 (Total Tests: 81)
Dungog: Pass Rate=77.78%, Avg Attempts=1.33 (Total Tests: 9)
Edward River: Pass Rate=72.22%, Avg Attempts=1.33 (Total Tests: 18)
Eurobodalla: Pass Rate=77.78%, Avg Attempts=1.37 (Total Tests: 27)
Fairfield: Pass Rate=44.24%, Avg Attempts=2.10 (Total Tests: 165)
Federation: Pass Rate=70.59%, Avg Attempts=1.29 (Total Tests: 17)
Forbes: Pass Rate=40.00%, Avg Attempts=1.92 (Total Tests: 25)
Georges River: Pass Rate=48.87%, Avg Attempts=2.08 (Total Tests: 133)
Gilgandra: Pass Rate=57.14%, Avg Attempts=1.14 (Total Tests: 7)
Glen Innes Severn: Pass Rate=44.44%, Avg Attempts=1.22 (Total Tests: 9)
Goulburn Mulwaree: Pass Rate=63.64%, Avg Attempts=1.57 (Total Tests: 44)
Greater Hume Shire: Pass Rate=45.00%, Avg Attempts=1.55 (Total Tests: 20)
Griffith: Pass Rate=52.73%, Avg Attempts=1.60 (Total Tests: 55)
Gunnedah: Pass Rate=56.00%, Avg Attempts=1.24 (Total Tests: 25)
Gwydir: Pass Rate=68.18%, Avg Attempts=1.45 (Total Tests: 22)
Hawkesbury: Pass Rate=53.12%, Avg Attempts=1.67 (Total Tests: 64)
Hay: Pass Rate=20.00%, Avg Attempts=1.20 (Total Tests: 5)
Hilltops: Pass Rate=53.12%, Avg Attempts=1.69 (Total Tests: 32)
Hornsby: Pass Rate=47.76%, Avg Attempts=1.99 (Total Tests: 134)
Hunters Hill: Pass Rate=45.24%, Avg Attempts=1.81 (Total Tests: 42)
Inner West: Pass Rate=49.14%, Avg Attempts=1.98 (Total Tests: 116)
Inverell: Pass Rate=78.95%, Avg Attempts=1.42 (Total Tests: 19)
Junee: Pass Rate=83.33%, Avg Attempts=1.33 (Total Tests: 6)
Kempsey: Pass Rate=56.00%, Avg Attempts=1.60 (Total Tests: 25)
Kiama: Pass Rate=50.00%, Avg Attempts=1.44 (Total Tests: 18)
Ku-ring-gai: Pass Rate=47.17%, Avg Attempts=2.00 (Total Tests: 106)
Kyogle: Pass Rate=61.11%, Avg Attempts=1.56 (Total Tests: 18)
Lachlan: Pass Rate=30.77%, Avg Attempts=1.69 (Total Tests: 13)
Lake Macquarie: Pass Rate=49.48%, Avg Attempts=1.79 (Total Tests: 97)
Lane Cove: Pass Rate=46.67%, Avg Attempts=1.77 (Total Tests: 75)
Leeton: Pass Rate=58.33%, Avg Attempts=1.58 (Total Tests: 36)
Lismore: Pass Rate=53.85%, Avg Attempts=1.44 (Total Tests: 39)
Lithgow: Pass Rate=68.00%, Avg Attempts=1.52 (Total Tests: 25)
Liverpool: Pass Rate=44.23%, Avg Attempts=2.12 (Total Tests: 156)
Liverpool Plains: Pass Rate=45.45%, Avg Attempts=1.91 (Total Tests: 11)
Lockhart: Pass Rate=44.44%, Avg Attempts=1.22 (Total Tests: 9)
Maitland: Pass Rate=50.00%, Avg Attempts=1.85 (Total Tests: 82)
Mid-Coast: Pass Rate=53.73%, Avg Attempts=1.72 (Total Tests: 67)
Mid-Western Regional: Pass Rate=54.55%, Avg Attempts=1.52 (Total Tests: 33)
Missing/Unknown: Pass Rate=49.15%, Avg Attempts=1.64 (Total Tests: 59)
Moree Plains: Pass Rate=54.55%, Avg Attempts=1.36 (Total Tests: 22)
Mosman: Pass Rate=67.74%, Avg Attempts=1.55 (Total Tests: 31)
Murray River: Pass Rate=61.54%, Avg Attempts=1.42 (Total Tests: 26)
Murrumbidgee: Pass Rate=73.68%, Avg Attempts=1.74 (Total Tests: 19)
Muswellbrook: Pass Rate=64.29%, Avg Attempts=1.71 (Total Tests: 28)
Nambucca Valley: Pass Rate=60.00%, Avg Attempts=1.52 (Total Tests: 25)
Narrabri: Pass Rate=48.48%, Avg Attempts=1.55 (Total Tests: 33)
Narrandera: Pass Rate=70.00%, Avg Attempts=1.40 (Total Tests: 10)
Narromine: Pass Rate=33.33%, Avg Attempts=1.67 (Total Tests: 12)
Newcastle: Pass Rate=48.21%, Avg Attempts=1.99 (Total Tests: 112)
North Sydney: Pass Rate=44.83%, Avg Attempts=1.92 (Total Tests: 87)
Northern Beaches: Pass Rate=51.33%, Avg Attempts=1.88 (Total Tests: 113)
Oberon: Pass Rate=72.73%, Avg Attempts=1.45 (Total Tests: 11)
Orange: Pass Rate=55.56%, Avg Attempts=1.56 (Total Tests: 54)
Parkes: Pass Rate=56.67%, Avg Attempts=1.83 (Total Tests: 30)
Parramatta: Pass Rate=45.16%, Avg Attempts=2.15 (Total Tests: 186)
Penrith: Pass Rate=47.46%, Avg Attempts=1.97 (Total Tests: 118)
Port Macquarie-Hastings: Pass Rate=54.55%, Avg Attempts=1.64 (Total Tests: 55)
Port Stephens: Pass Rate=51.79%, Avg Attempts=1.96 (Total Tests: 56)
Queanbeyan-Palerang Regional: Pass Rate=50.68%, Avg Attempts=1.93 (Total Tests: 73)
Randwick: Pass Rate=51.09%, Avg Attempts=1.89 (Total Tests: 92)
Richmond Valley: Pass Rate=61.54%, Avg Attempts=1.54 (Total Tests: 26)
Ryde: Pass Rate=48.53%, Avg Attempts=2.07 (Total Tests: 136)
Shellharbour: Pass Rate=49.23%, Avg Attempts=1.85 (Total Tests: 65)
Shoalhaven: Pass Rate=53.73%, Avg Attempts=1.63 (Total Tests: 67)
Singleton: Pass Rate=50.00%, Avg Attempts=1.42 (Total Tests: 36)
Snowy Monaro Regional: Pass Rate=70.59%, Avg Attempts=1.56 (Total Tests: 34)
Snowy Valleys: Pass Rate=62.50%, Avg Attempts=1.50 (Total Tests: 24)
Strathfield: Pass Rate=49.14%, Avg Attempts=2.11 (Total Tests: 116)
Sutherland Shire: Pass Rate=50.00%, Avg Attempts=1.87 (Total Tests: 98)
Sydney: Pass Rate=46.88%, Avg Attempts=1.99 (Total Tests: 128)
Tamworth Regional: Pass Rate=54.17%, Avg Attempts=1.88 (Total Tests: 72)
Temora: Pass Rate=36.84%, Avg Attempts=1.63 (Total Tests: 19)
Tenterfield: Pass Rate=66.67%, Avg Attempts=1.83 (Total Tests: 12)
The Hills Shire: Pass Rate=51.88%, Avg Attempts=1.99 (Total Tests: 133)
Tweed: Pass Rate=63.04%, Avg Attempts=1.78 (Total Tests: 46)
Unincorporated NSW: Pass Rate=57.69%, Avg Attempts=1.62 (Total Tests: 26)
Upper Hunter Shire: Pass Rate=61.90%, Avg Attempts=1.52 (Total Tests: 21)
Upper Lachlan Shire: Pass Rate=83.33%, Avg Attempts=1.67 (Total Tests: 6)
Uralla: Pass Rate=63.64%, Avg Attempts=1.36 (Total Tests: 11)
Wagga Wagga: Pass Rate=47.44%, Avg Attempts=1.78 (Total Tests: 78)
Walcha: Pass Rate=33.33%, Avg Attempts=1.00 (Total Tests: 3)
Walgett: Pass Rate=55.56%, Avg Attempts=1.52 (Total Tests: 27)
Warren: Pass Rate=50.00%, Avg Attempts=1.88 (Total Tests: 8)
Warrumbungle Shire: Pass Rate=75.00%, Avg Attempts=1.62 (Total Tests: 8)
Waverley: Pass Rate=47.22%, Avg Attempts=1.82 (Total Tests: 72)
Weddin: Pass Rate=44.44%, Avg Attempts=1.89 (Total Tests: 27)
Wentworth: Pass Rate=62.50%, Avg Attempts=1.75 (Total Tests: 16)
Willoughby: Pass Rate=42.37%, Avg Attempts=1.96 (Total Tests: 118)
Wingecarribee: Pass Rate=57.41%, Avg Attempts=1.61 (Total Tests: 54)
Wollondilly: Pass Rate=47.50%, Avg Attempts=1.75 (Total Tests: 40)
Wollongong: Pass Rate=50.77%, Avg Attempts=2.08 (Total Tests: 130)
Woollahra: Pass Rate=54.10%, Avg Attempts=1.89 (Total Tests: 61)
Yass Valley: Pass Rate=54.55%, Avg Attempts=1.73 (Total Tests: 22)

--- Analysis by Age Group ---
16-17: Pass Rate=57.55%, (Total Tests: 1046)
18-20: Pass Rate=54.37%, (Total Tests: 892)
21-24: Pass Rate=53.69%, (Total Tests: 704)
25-29: Pass Rate=52.87%, (Total Tests: 870)
30-34: Pass Rate=51.19%, (Total Tests: 842)
35-39: Pass Rate=51.66%, (Total Tests: 755)
40-44: Pass Rate=46.59%, (Total Tests: 646)
45-49: Pass Rate=45.50%, (Total Tests: 400)
50-54: Pass Rate=42.00%, (Total Tests: 300)
55-59: Pass Rate=33.33%, (Total Tests: 192)
60-64: Pass Rate=36.23%, (Total Tests: 138)
65-69: Pass Rate=37.21%, (Total Tests: 86)
70-74: Pass Rate=16.67%, (Total Tests: 42)
75-79: Pass Rate=25.00%, (Total Tests: 8)
80-84: Pass Rate=100.00%, (Total Tests: 1)

--- Analysis by Gender ---
Female: Pass Rate=49.92%, (Total Tests: 3201)
Male: Pass Rate=51.41%, (Total Tests: 3721)

-----------------------------
```
## Data Source Note
https://opendata.transport.nsw.gov.au/data/dataset/transport-nsw-driver-licence-test-statistics/resource/417488f7-b266-455c-b921-c212082203a6?inner_span=True
This tool is designed for analysing publicly available or privately obtained datasets from Transport for NSW regarding driver licence tests. Ensure you comply with any terms of use associated with the data source. The script processes data locally and focuses on aggregate statistics.
