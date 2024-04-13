import pandas as pd
from collections import ChainMap
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

#Get Sentiment Anaysis Score
def learn_state(sentence):
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(sentence)
    return sentiment_score

def df_tolist():
    b = df['1'].values.tolist()
    c = df['1.1'].values.tolist()
    d = df['Nice service and nice food'].values.tolist()
    return b,c,d    

#Decide if the review if positive, negative or neutral
def state_decision(review):
    sentiment_score = learn_state(review)
    positive_score = round((sentiment_score['pos'] * 10), 2)
    negative_score = round((sentiment_score['neg'] * 10), 2)
    if positive_score > negative_score:
        return 1
    elif positive_score < negative_score:
        return 0
    elif positive_score < negative_score:
        return -1

def update_rows(row_index):
    review = d[row_index]
    column_a = state_decision(review) 
    dict = {'A':column_a, 'B':b[row_index], 'C':c[row_index], 'Nice service and nice food':d[row_index], }
    rows_list.append(dict)

def iterate_over_csv():
    for row_index in range(0,len(b)):
        update_rows(row_index)

# reading the csv file
df = pd.read_csv("chunk33.csv")

#Download nltk for sentiment analysis
nltk.downloader.download('vader_lexicon')

b,c,d = df_tolist()

rows_list = []
iterate_over_csv()

#list to df
new_df = pd.DataFrame(rows_list)               
new_df.to_csv("chunk33_FikretMert_Gultekin.csv", index=False)
#print(new_df)



false = [16,25,26,29,34,43,70,76,82,86,88,90,98]
for row_index in false:
    specificReview = d[row_index]
    sentiment_score_specific = learn_state(specificReview)
    print(sentiment_score_specific)
    print(": Review "+specificReview)

