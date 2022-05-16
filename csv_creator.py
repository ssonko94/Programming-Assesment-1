import csv


def csvCreator(file_name: str = 'example_file.csv', data: list = ['']) -> None:
    ''' 
        @param file_name: name of the file to be created
        @param data: list of data to be written to the file
        Creates a csv file from a list of strings.
    '''
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(data)
