from Webscraping import parse_results_page, get_hrefs, relevant_links, remove_line_breaks
import pandas as pd
from bs4 import BeautifulSoup
import requests

italy_url_list = ['http://www.governo.it/it/interventi?dataInizio=2020-03-01+00%3A00%3A00&dataFine=2020-04-30+23%3A59%3A59', 'http://www.governo.it/it/interventi?dataInizio=2020-03-01%2000%3A00%3A00&dataFine=2020-04-30%2023%3A59%3A59&page=1']
italy_parsed_pages = parse_results_page(italy_url_list)
italy_hrefs = get_hrefs(italy_parsed_pages)
partial_italy_links = relevant_links(italy_hrefs, 'articolo')

italy_links = []
for link in partial_italy_links:
    if 'http://www.governo.it' in link:
        italy_links.append(link)
    else:
        link = 'http://www.governo.it' + link
        italy_links.append(link)

def extract_data_italy(url_list):
    """
    Arguments: list of parsed pages
    Output: Italy-specific data dictionary with date, header and content"""
    data_dictionary = {}
    for url in url_list:
        response = requests.get(url)
        page=response.text
        soup= BeautifulSoup(page, 'lxml')
        header = soup.select('h2.title_large')[0].text.strip()
        date = soup.find("p", {"class":"h6"}).text
        content = soup.find("div", {'class':"body_intervista"}).text
        data_dictionary[url] = {'Header': header, 'Date': date, 'Content':content}
    return data_dictionary
data_dictionary_italy = extract_data_italy(italy_links)

italy_df = pd.DataFrame.from_dict(data_dictionary_italy)

italy_df = remove_line_breaks(italy_df)

italy_df.to_csv('italy_data.csv')
