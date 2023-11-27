import pandas as pd

"""
    Sometimes it is not possible to make df direct from txt or csv files.
    To create a df we can read file with open module of python and get the data with loop and append it to a list. 
    Then we can create a df from the list.
"""

my_first_list=[]
with open("file_name", "r") as f:
    """
        To pars a string line we can use 2 methods. one of them is parse with arrey method
    """
    for line in f:
       col2=line[37:49].replace(" ","")
       col3=float(line[49:64].replace(" ",""))
       new_data=[col2, col3]
       my_first_list.append(new_data)

my_first_df = pd.DataFrame(my_first_list, columns=["COL1","COL2"])

my_second_list =[]
with open("file_name", "r") as f:
    """
        To pars a string line we can use 2 methods. one of them is parse with split method.
        you may want to use some math methodes. to do that make sure you data is int or float.
    """
    for line in f:
        list_line=list(line.split(","))
        if list_line[5].isdigit():
            list_line[5] = float(list_line[11])
        my_second_list.append(list_line)

"""
    before create a df we need a header. the index 0 of our list is the header.
    to creat a df start from the index 1. 
"""
header = my_second_list[0]
my_second_df = pd.DataFrame(my_second_list[1:], header=header)
