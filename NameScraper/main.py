from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import os


def get_names(final_url, parse_type):
    webpage = requests.get(final_url, headers={'User-Agent': ''})
    soup = BeautifulSoup(webpage.content, parse_type)
    names = []
    for anchor in soup.findAll('a'):
        if anchor.parent.name == 'td':
            names.append(anchor.string + "\n")
    return names


def write_to_file(filename, values):
    file = open(filename, 'w', encoding='utf-8')
    file.writelines(values)
    file.close()


def main():
    load_dotenv()

    SAVE_LOCATION = os.getenv('OUTPUT_LOCATION')
    BASE_URL = os.getenv('WEBSITE_BASE_URL')
    FIRSTNAMES_URL = os.getenv('FIRSTNAMES')
    LASTNAMES_URL = os.getenv('LASTNAMES')
    parse_type = 'html.parser'

    firstnames = get_names(BASE_URL + "/" + FIRSTNAMES_URL, parse_type)
    lastnames = get_names(BASE_URL + "/" + LASTNAMES_URL, parse_type)

    write_to_file(SAVE_LOCATION + "\\" + "FirstNames.txt", firstnames)
    write_to_file(SAVE_LOCATION + "\\" + "LastNames.txt", lastnames)


if __name__ == '__main__':
    main()
