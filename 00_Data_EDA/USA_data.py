from Webscraping import parse_results_page, get_hrefs, relevant_links, remove_line_breaks
import pandas as pd
from bs4 import BeautifulSoup
import requests

url_part_1 = 'https://www.whitehouse.gov/remarks/page/'
url_part_2 = '/?issue_filter=healthcare'
usa_url_list = []
for i in range(1,9):
    usa_url_list.append(url_part_1 + str(i) + url_part_2)

usa_parsed_pages = parse_results_page(usa_url_list)

usa_hrefs = get_hrefs(usa_parsed_pages)

usa_links = relevant_links(usa_hrefs, 'remarks-president-trump')

def extract_data_usa(url_list):
    """
    Arguments: list of parsed pages
    Output: USA-specific data dictionary with date, header and content"""
    data_dictionary = {}
    for url in url_list:
        response = requests.get(url)
        page=response.text
        soup= BeautifulSoup(page, 'lxml')
        header = soup.select('h1.page-header__title')[0].text.strip()
        date = soup.select('time')[0].text.strip()
        content = soup.find("div", {"class":"page-content"}).text
        data_dictionary[url] = {'Header': header, 'Date': date, 'Content':content}
    return data_dictionary
data_dictionary_usa = extract_data_usa(usa_links)

us_df = pd.DataFrame.from_dict(data_dictionary_usa)

us_df = remove_line_breaks(us_df)

us_df.to_csv('usa_data.csv')




