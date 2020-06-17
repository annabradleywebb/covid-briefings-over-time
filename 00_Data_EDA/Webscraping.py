from bs4 import BeautifulSoup
import requests

def parse_results_page(url_list):
    """
    Arguments: list of urls to parse
    Output: parsed pages"""
    pages = []
    for url in url_list:
        requests.get(url)
        pages.append((requests.get(url)).text)
    return pages

def get_hrefs(parsed_pages):
    """
    Arguments: list of parsed pages
    Output: a list of the href attributes from the pages"""
    hrefs = []
    for page in parsed_pages:
        soup = BeautifulSoup(page, "lxml")
        for link in soup.findAll('a'):
            hrefs.append(link.get('href'))
    return hrefs

def relevant_links(list_links, criteria):
    """
    Arguments: a list of the links found on the base page and criteria for finding the relevant links
    Output: a list of the relevant links
    """
    links = []
    for link in list_links:
        if criteria in link:
            if link not in links:
                links.append(link)
    return links

def remove_line_breaks(df):
    df = df.replace(r'\n',' ', regex=True)
    df = df.replace(r'\t',' ', regex=True)
    df = df.replace(r'.\xa0', ' ', regex=True)
    df = df.transpose()
    return df


