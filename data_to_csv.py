import csv
import csv_funcs

from radiodata.radiodata import RadioData

# This is the main function of the Radio-to-CSV script. 
# It writes the data given by a RadioData object into a CSV file with the given name.
def data_to_csv(data_obj: RadioData, filename: str = "buggydata.csv"):

    # Creating a new CSV if there doesn't exist one
    if not csv_funcs.exists_csv(filename):
        csv_funcs.create_csv_file(filename, data_obj.get_fieldnames())

    # Writing to the CSV
    csv_funcs.write_to_csv(filename, data_obj.get_data_dict())