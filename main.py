from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas as pd
from collections import defaultdict


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')
excel_data_df = pd.read_excel('wine3.xlsx',na_filter="")
drinks = excel_data_df.to_dict(orient="records")
groups = defaultdict(list)

for drink in drinks:
    groups[drink['Категория']].append(drink)
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

rendered_page = template.render(
    date = datetime.date.today().year - 1920,
    year = get_year_name(),
    white_wines = groups["Белые вина"],
    red_wines = groups["Красные вина"],
    drinks = groups["Напитки"]
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
