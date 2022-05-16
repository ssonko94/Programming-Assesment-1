from csv_creator import csvCreator
from csv_content_file_reader import csv_content_file_reader


def output(file_name: str = 'example.csv', data: list = ['honey', 'milk', 'cheese']) -> None:
    """
        @param file_name: name of the file to be created
        @param data: list of data to be written to the file
        Creates a csv file from a list of strings.
    """
    try:
        csvCreator(file_name, data)
        print('Success!')
        file_content = csv_content_file_reader(file_name)
        for row in file_content:
            print(row)
    except Exception as e:
        print(e)
        print('Error!')


output('cars.csv', ['Rolls Royce', 'Volkswagen', 'Aston Martin',
       'Audi', 'BMW', 'Mercedes-Benz', 'Porsche', 'Bentley', 'Lamborghini', 'Bugatti', 'Ferrari'])
