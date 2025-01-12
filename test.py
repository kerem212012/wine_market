import pandas as pd
from pprint import pprint
from collections import defaultdict


excel_data_df = pd.read_excel('wine3.xlsx',na_filter="")
drinks = excel_data_df.to_dict(orient="records")



groups = defaultdict(list)

for drink in drinks:
    groups[drink['Категория']].append(drink)
pprint(groups)
