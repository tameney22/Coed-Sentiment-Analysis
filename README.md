# Sentiment Analysis

**Project Site:** [Link Here](https://iwrite.wludci.info/dci102/)
Performing sentiment analysis on letters using the Bing Liu lexicon. After a sentiment score and net-sentiment score are calculated, their change across time is observed using time series plots.
### Getting Started

  - Create a **data** folder to store the corpus and a metadata.csv file. The metadata will be used in [sentiment.py](https://github.com/tameney22/Coed-Sentiment-Analysis/blob/main/sentiment.py) to retrieve the relevant information for creating the three CSVs: posCloud, negCloud, and output. The metadata data model can be found in the data section on the project site.
  - The copies included in the repo are sample outputs when running the analysis.
  - Run  `$ python sentiment.py` in your terminal from the project directory.
  - Open the [visualize.ipynb](https://github.com/tameney22/Coed-Sentiment-Analysis/blob/main/visualize.ipynb) and run all code blocks. This will use the CSV outputs from the previous step and create time series plots for the scores and wordclouds using words in the corpus.
  - The visualizations should then be saved in the **images** folder in png format.

### Libraries used
This project uses the following python libraries:
* [pandas](https://pandas.pydata.org/)
* [numpy](https://numpy.org/)
* [nltk](https://www.nltk.org/)

License
----

MIT