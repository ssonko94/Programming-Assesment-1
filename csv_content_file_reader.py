import csv


def csv_content_file_reader(file_name: str) -> list:
    '''
        @param file_name: name of the file to be read
        @return: list of strings from the file
        Reads a csv file and returns a list of strings.
    '''
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='\n')
        return [row for row in reader]
