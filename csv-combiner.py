# Caleb Hoff
# Created: 03 May 2022
# Programming Challenge: CSV Combiner

import sys
import re
import csv

if __name__ == "__main__":
    # Check for Missing Arguments
    if len(sys.argv) < 2:
        print("Missing Command-Line Arguments\n" +
        "Usage: python3 csv-combiner.py <File: CSV #1> ... <File: CSV #n>")
        sys.exit("Exiting...")

    # Initialize Writer to stdout
    writer = csv.writer(sys.stdout, dialect='unix')

    # Stream Read All CSVs & Iteratively Write to stdout
    is_first = True
    for csv_filename in sys.argv[1:]:                       # Iterate Through CSVs
        csv_base = re.sub(r'^.*[/\\]', '', csv_filename)    # Get File Basename
        with open(csv_filename, 'r') as f:                  # Open CSV File
            for i, row in enumerate(csv.reader(iter(f.readline, ''))):  # Stream
                if i != 0 and not is_first:                 # Skip Header Row
                    writer.writerow(row + [csv_base])
                elif is_first:                              # Write Header Row
                    writer.writerow(row + ['filename'])
                    is_first = False