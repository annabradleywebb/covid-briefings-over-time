## Italian and US Covid-19 Briefings: Natural Language Processing

This project used Natural Language Processing to explore the topic makeup of official Covid-19 briefings in the US and Italy in April and May 2020.

This repo contains:

### 0. Data gathering and EDA

1. Using BeautifulSoup Python package, I scraped transcripts of official briefings from WhiteHouse.gov and Governo.it (**Webscraping.py**)
2. I stored the scraped text data in dictionary format (**Italy_data.py** and **USA_data.py**) in a MongoDB database
3. I pulled the data from MongoDB back into Python (**data_cleaning_notebook.ipynb**) and cleaned and performed text preprocessing (lemmatization, part-of-speech tagging) on the text data to prepare for topic modeling (**data_cleaning.py**)

### 1. Modeling

1. Using an NMF model, I performed topic modeling on the US and Italian text data (nouns only) and generated a doc-topic matrix that showed the change in topics over time (**topic_modeling.py** and **Topic_modelingnotebook.ipynb**)

### 2. Results and Visualization

My results, interpretation and visualizations can be found in my deck (**02_Presentation.pdf**) 