# 4. Network
# The dataset
# The dataset is a text file where every line represents a JSON object that describes a tweet (tweet.json). It was fetched using twitter stream API, hence we're dealing with real life data (yay).
 
# 4.1 Popular Hashtag
# Write a program that prints on the screen 10 most popular #hashtags followed by the number of occurrences of the #hashtag.
# 4.2 Tokenizer
# Let's do some emotional analyses.
# In this file AFINN-111.txt you'll find an emotion dictionary for English words. Every word mentioned in the dictionary is followed by a numerical value in the range of -5 to 5. The numerical value describes the word emotional impact where -5 is the most negative and 5 is the most positive.
# Your task is to find the emotional value for every tweet. First step would be to extract every word from the tweet body. I recommend using an nltk tokenizer (similar to PSA Lab 3). Then you find out the emotional value for every word (if it has one). You finish by summing the emotion rating.
# Write a program that will store the computed result in a text file. Every line should represent the tweet id followed by the computed emotional value.
# 4.3 Top
# Write a program that prints on the screen 10 most positive tweets and 10 most negative tweets.

import json
from string import punctuation
from collections import Counter
from nltk.tokenize import word_tokenize

def writeinfile(file_path, tweets, emotions):
    with open(file_path, 'w') as file:
        for i in range(len(tweets)):
            file.write("{0} : {1:.2f}\n".format(tweets[i]['id'],emotions[i]))

def replace_punct(text, set):
    for i in range(len(text)):
        if text[i] in set:
            text = text.replace(f'{text[i]}', ' ')
    return text

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def read_emotions(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i]=lines[i].strip().split()

    dict = {' '.join(line[0:len(line)-1]): int(line[-1]) for line in lines}
    return dict



print("Problem 4.1\n10 most popular #hashtags followed by the number of occurrences of the #hashtag")
tweets=read_json("tweets.json")
hashtags=[]
spec_characters=set(punctuation)
spec_characters.remove('#')
spec_characters.add('…')
sentences=[]
for tweet in tweets:
    text=tweet['text']
    sentences.append(word_tokenize(text))
    text=replace_punct(text,spec_characters).split()

    for word in text:
        if word[0]=='#' and len(word)>1 and word[1].isalpha():
            hashtags.append(word)

count_hashtags= Counter(hashtags)
sorted_hashtags=dict(sorted(count_hashtags.items(), key=lambda item: item[1],reverse=True))
i=0
for hashtag,count in sorted_hashtags.items():
    print("{0}. {1}: {2}".format(i+1,hashtag,count))
    i+=1
    if i==10:
        break




print("\n\nProblem 4.2\nfind the emotional value for every tweet")
emotions=read_emotions("AFINN-111.txt")
emotional_value=[]

for sentence in sentences:
    sum=0
    k=0
    for word in sentence:
        if word in emotions:
            sum+=emotions[word]
            k+=1

    if k!=0:
        emotional_value.append(sum/k)
    else:
        emotional_value.append(0)

writeinfile("output.txt", tweets, emotional_value)
print("Data is stored in 'output.txt'")




print("\n\nProblem 4.3\n10 most positive tweets and 10 most negative tweets")
for i in range(len(tweets)):
    tweets[i]['emotional_value']=emotional_value[i]
sorted_tweets = sorted(tweets, key=lambda x: x['emotional_value'])

print("\nMost Positive Tweets")
i=0
for tweet in sorted_tweets[::-1]:
    print(i+1," : ", tweet['text'])
    i+=1
    if i==10:
        break

print("Most Negative Tweets")
i=0
for tweet in sorted_tweets:
    print(i+1," : ", tweet['text'])
    i+=1
    if i==10:
        break
