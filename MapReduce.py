"""
Implements the MapReduce programming model on NYC Subway Fare data
"""

#-----------------------------------------------------------------------------#
from read_csv_info import read_header

#-----------------------------------------------------------------------------#
class MapReduce:
    def __init__(self):
        self.intermediate = {}
        self.result = []

    def emit_intermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer, col_num):

        # Iterate over all the files
        for files in data:
            csv_file_object, date_range, column_names = read_header(files)

            # Only consider recent data files which include Student fare data
            if 'STUDENTS' in column_names:
                for row in csv_file_object:
                    mapper(row, col_num) # Call the mapper

        for key in self.intermediate:
            reducer(key, self.intermediate[key]) # Call the reducer

        # Sort the result by station with largest number of fares
        self.result.sort(key=lambda tup: tup[1], reverse=True)
        
        return self.result

#-----------------------------------------------------------------------------#