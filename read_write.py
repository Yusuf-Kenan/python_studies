import csv
import os
import pandas as pd
from zipfile import ZipFile

zipfiles=os.listdir("type your root file of your files you want to use")
#example => "desktop/python_studies/" = below "root_file" will be used

#extracting zip
for file in zipfiles:
    with ZipFile(f"root_file{file}", 'r') as f:
        f.extractall("./csv_files/")

#File to dataframe
csv_files=os.listdir("./csv_files/")
combine_csv=pd.DataFrame()
for file in csv_files:
    df=pd.read_csv(f"./csv_files/{file}", sep=";")
    combine_csv = combine_csv._append(df,ignore_index=True)

#Dataframe to csv
combine_csv.to_csv("combined_data_file.csv", index=False, sep=";")

#Read and write file
my_file="combined_data_file.csv"
field_names=["DATE","MEMBER","ACCOUNT_NO","TOTAL"]
with open(my_file, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")

    with open("member_account_"+my_file, "w" , newline="") as new_file:
        csv_writer= csv.DictWriter(new_file, fieldnames=field_names, delimiter=";")
        csv_writer.writeheader()
        for line in csv_reader:
            if(len(line["ACCOUNT"])==11 or line["MEMBER"]=="1650001509"):
                csv_writer.writerow(line)  

    #reread file. without rereaad this part will throw error
    csv_rereader = csv_file.read()
    with open("rearead"+my_file, "w",newline="") as new_file:
        csv_writer= csv.DictWriter(new_file, fieldnames=field_names, delimiter=";")
        csv_writer.writeheader()
        for line in csv_reader:
            if(len(line["ACCOUNT"])==8):
                csv_writer.writerow(line)         
