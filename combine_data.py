"""
Combines all the files downloaded by 'download_data.py' into one 
big csv file. Then, prints out some basic stats about 5 major 
types of fares.
"""

#-----------------------------------------------------------------#
import os
import csv
from read_csv_info import read_header

#-----------------------------------------------------------------#
"""
Combines all the CSV files and creates a big master file on main 
folder.
"""
def combine_data():
    
    # Create a new combined csv master file, with a header row
    combo_file = csv.writer(open('fares_combined.csv', 'wb'))
    header = ['DATE RANGE', 'REMOTE', ' STATION', 'FF', 'SEN/DIS', ' 7-D AFAS UNL', \
                '30-D AFAS/RMF UNL', 'JOINT RR TKT', '7-D UNL', '30-D UNL', '14-D RFM UNL', \
                '1-D UNL', '14-D UNL', '7D-XBUS PASS', 'TCMC', 'LIB SPEC SEN/RF 2 TRIP', \
                'RR UNL NO TRADE', 'TCMC ANNUAL MC', 'MR EZPAY EXP', 'MR EZPAY UNL', 'PATH 2-T', \
                'AIRTRAIN FF', 'AIRTRAIN 30-D', 'AIRTRAIN 10-T', 'AIRTRAIN MTHLY', 'STUDENTS']
    combo_file.writerow(header)

    # Capture list of files in the fare_data folder
    data_files = os.listdir('fare_data')
    for files in data_files:
        csv_file_object, date_range, column_names = read_header(files)

        # Only consider recent data files which include Student fare data
        if 'STUDENTS' in column_names:
            for row in csv_file_object:
                row.insert(0, date_range)           # Insert date range as first column
                combo_file.writerow(row[:-1])

    print "All files combined, please check the 'fares_combined.csv' in current directory."

#-----------------------------------------------------------------#
"""
Prints some basic stats about 5 major types of fares. These are:
- Full fares
- Senior Citizen/Disabled fares
- 7 Day Unlimited fares
- 30 Day Unlimited fares
- Student fares
"""
def print_stats():

    csv_file_object = csv.DictReader(open('fares_combined.csv'))
    ff_total = sen_total = unl7d_total = unl30d_total = stu_total = 0
    
    for row in csv_file_object:
        ff_total += int(row['FF'])
        sen_total += int(row['SEN/DIS'])
        unl7d_total += int(row['7-D UNL'])
        unl30d_total += int(row['30-D UNL'])
        stu_total += int(row['STUDENTS'])
    
    print '\nHere are some fare type stats:'
    print 'Full Fares(FF) Total:', ff_total
    print 'Senior Citizen/Disabled Fares (SEN/DIS) Total:', sen_total
    print '7 Day Unlimited Fares (7-D UNL) Total:', unl7d_total
    print '30 Day Unlimited Fares (30-D UNL) Total:', unl30d_total
    print 'Student Fares (STUDENTS) Total:', stu_total
    print '\n'

#-----------------------------------------------------------------#
if __name__ == '__main__':
    combine_data()
    print_stats()

#-----------------------------------------------------------------#
