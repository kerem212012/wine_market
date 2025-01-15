import pandas as pd
from collections import defaultdict
import datetime
import argparse


def get_drinks(xlsx_file):
    excel_data_df = pd.read_excel(xlsx_file,na_filter="")
    drinks = excel_data_df.to_dict(orient="records")
    groups = defaultdict(list)

    for drink in drinks:
        groups[drink['Категория']].append(drink)
    return groups

def get_year_name():
    year = datetime.date.today().year - 1920
    year = " ".join(str(year)).split(" ")
    if (year[-1] == "1" or year[-1] == "2" or year[-1] == "3" or year[-1] == "4")  and year[-2] == "1":
        name = "лет"
    elif year[-1] == "1":
        name = "год"
    elif year[-1] == "2" or year[-1] == "3" or year[-1] == "4":
        name = "года"
    else:
        name = "лет"
    return name
