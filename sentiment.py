# Download the bing dictionary of sentiment words
# Categorized as positive or negative
# Only done once, so comment out
# nltk.download('opinion_lexicon')

# The following is the package for the tockenizer to separate the words and punctuations
# Also done once, so comment out
# nltk.download('punkt')
import csv
import nltk
import os
from dateutil import parser
from nltk.corpus import opinion_lexicon
from nltk import word_tokenize

positiveWords = set(opinion_lexicon.positive())
negativeWords = set(opinion_lexicon.negative())

# The following are for capturing the frequencies for the wordcloud figure
positiveCloud = {}
negativeCloud = {}

def calculateSentiment(filename):
    # Open the file for reading
    file = open("data/" + filename, "r")
    text = file.read()
    file.close()

    wordList = word_tokenize(text)
    # Make all letters in each word lowercase
    wordList = [word.lower() for word in wordList]

    sentimentScore = 0
    # Just to see which words are considered
    positiveCount = 0
    negativeCount = 0
    for word in wordList:
        if word in positiveWords:
            sentimentScore += 1
            positiveCount += 1

            if positiveCloud.get(word):
                positiveCloud[word] += 1
            else:
                positiveCloud[word] = 1

        elif word in negativeWords:
            sentimentScore -= 1
            negativeCount += 1

            if negativeCloud.get(word):
                negativeCloud[word] += 1
            else:
                negativeCloud[word] = 1
    # Calculate net sentiment ratio
    netSentiment = (positiveCount - negativeCount) / len(text.split())
    
    return (sentimentScore, netSentiment)

def main():
    toOutput = []
    with open('data/metadata.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        fields = next(csv_reader)
        
        for row in csv_reader:
            (score, netSentiment) = calculateSentiment(row[4])
            date = parser.parse(row[2]).date()
            opinion = row[3]
            toOutput.append([score, netSentiment, date, opinion])

    # CSV write for sentiment and net sentiment ratio graphs
    outputFilename = "output.csv"
    with open(outputFilename, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Sentiment", "Net Sentiment Ratio", "Date", "Opinion"])
        csv_writer.writerows(toOutput)

    # CSV write for word cloud of positive words
    cloudFilename = "posCloud.csv"
    with open(cloudFilename, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Word", "Frequency"])
        
        posWords = [[word, freq] for word, freq in positiveCloud.items()]

        csv_writer.writerows(posWords)

    # CSV write for word cloud of negative words
    cloudFilename = "negCloud.csv"
    with open(cloudFilename, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Word", "Frequency"])
        
        negWords = [[word, freq] for word, freq in negativeCloud.items()]

        csv_writer.writerows(negWords)

if __name__ == "__main__":
    main()