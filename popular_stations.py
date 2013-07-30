"""
Combines all the fare data from all csv files and processes it using MapReduce 
model. Based on the selection made by the user, outputs the top stations for 
that particular fare type.
"""

#-----------------------------------------------------------------------------#
import MapReduce
import os

#-----------------------------------------------------------------------------#
# Creates a MapReduce object
mr = MapReduce.MapReduce()

"""
Offers a menu selection to the user and collects total fare information across 
all the fara data files downloaded from MTA's site.
"""
def main():

    # Capture list of files in the fare_data folder
    data_files = os.listdir('fare_data')
    data_files = ['fares_130713.csv']
    
    print '\nPlease enter one of the following:'
    print '"F" for full fares'
    print '"S" for senior citizen and disabled fares'
    print '"7" for 7 day unlimited fares'
    print '"30" for 30 day unlimited fares'
    print 'Or default choice is student fares\n'

    choice = raw_input()
    
    if choice in ['F', 'f']:
        col_num = 2  # Full fares are listed in column 2
        col_name = 'Full'
    elif choice in ['S', 's']:
        col_num = 3  # Senior Citizen/Disabled fares are listed in column 3
        col_name = 'Senior Citizen/Disabled'
    elif choice in ['7', 7]:
        col_num = 7  # 7 Day Unlimited fares are listed in column 7
        col_name = '7 Day Unlimited'
    elif choice in ['30', 30]:
        col_num = 8  # 30 Day Unlimited fares are listed in column 8
        col_name = '30 Day Unlimited'
    else:
        col_num = 24 # Student fares are listed in column 24
        col_name = 'Student'

    results = mr.execute(data_files, mapper, reducer, 24)
    
    print '\nHere are the top stations for ' + col_name + ' fares in descending order:\n'
    print 'Station Name - ', 'Total Tickets Used'
    for item in results:
        print item[0].strip(), '-', item[1]

#-----------------------------------------------------------------------------#
"""
Generates key-value pair for Station Name and Tickets sold for a particular 
fare type
"""
def mapper(record, col_num):
    key = record[1]
    value = int(record[col_num])
    mr.emit_intermediate(key, value)

#-----------------------------------------------------------------------------#
"""
Processes the total of all values for each Station
"""
def reducer(key, list_of_values):
    total = 0
    for value in list_of_values:
        total += value
    mr.emit((key, total))

#-----------------------------------------------------------------------------#
if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------------#