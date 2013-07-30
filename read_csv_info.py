"""
Reads the CSV file and return relevant information about the data.
"""

#-----------------------------------------------------------------#
import csv

#-----------------------------------------------------------------#
"""
Reads the header information about the CSV file and returns the 
Date Range and Column Names.
"""

def read_header(filename):

    csv_file_object = csv.reader(open('fare_data/'+filename, 'rb'))
    csv_file_object.next()                      # Skip junk rows
    date_range = csv_file_object.next()[1]
    column_names = csv_file_object.next()

    return csv_file_object, date_range, column_names

#-----------------------------------------------------------------#
if __name__ == '__main__':
    read_header(filename)

#-----------------------------------------------------------------#