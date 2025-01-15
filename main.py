from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
from functions import get_year_name,get_drinks
import argparse
from environs import Env


environ = Env()
environ.read_env()
env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

parser = argparse.ArgumentParser()
parser.add_argument("-f","--file",help="enter file path",default=environ.str("FILE_PATH"))
args = parser.parse_args()

drinks = get_drinks(args.file)


rendered_page = template.render(
    date = datetime.date.today().year - 1920,
    year = get_year_name(),
    drinks = drinks

)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
