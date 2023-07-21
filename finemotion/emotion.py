#!/usr/bin/env python
"""
@author: shawnemccarthy
"""

import json
import os
import re
import string
import subprocess
import sys
import unicodedata
import contractions
import nltk
import spacy
from nltk.sentiment.vader import SentimentIntensityAnalyzer

try:
    nlp = spacy.load('en_core_web_sm', disable=['parser','ner'])
except IOError:
    print("The 'en_core_web_sm' model is not installed. Downloading now..")
    print("You will need to restart your venv")
    return_code = subprocess.call([sys.executable, 
                                   "-m", 
                                   "spacy", 
                                   "download", 
                                   "en_core_web_sm"])
    print(f'The command returned: {return_code}')
    nlp = spacy.load('en_core_web_sm', disable=['parser','ner'])

nltk.download('vader_lexicon')

def removing_shortcuts(text):
    full_words = []
    shortcuts = {
                'u': 'you', 
                'y': 'why', 
                'r': 'are', 
                'doin': 'doing', 
                'hw': 'how', 
                'k': 'okay', 
                'm': 'am',
                'b4': 'before',
                'idc': "i do not care", 
                'ty': 'thank you', 
                'wlcm': 'welcome', 
                'bc': 'because', 
                '<3': 'love',
                'xoxo': 'love',
                'ttyl': 'talk to you later', 
                'gr8': 'great', 
                'bday': 'birthday', 
                'awsm': 'awesome', 
                'gud': 'good',
                'h8': 'hate',
                'lv': 'love', 
                'dm': 'direct message', 
                'rt': 'retweet', 
                'wtf': 'hate', 
                'idgaf': 'hate',
                'irl': 'in real life', 
                'yolo': 'you only live once', 
                "don't": "do not", 
                'g8': 'great',
                "won't": "will not", 
                'tbh': 'to be honest', 
                'caj': 'casual', 
                'Ikr': 'I know, right?',
                'omw': 'on my way',
                'ofc': 'of course',  
                'Irl': 'In real life', 
                'tbf': 'To be fair',
                'obvs': 'obviously', 
                'v': 'very', 
                'atm': 'at the moment',
                'col': 'crying out loud', 
                'gbu': 'god bless you', 
                'gby': 'god bless you', 
                'gotcha': 'I got you',
                'hehe': 'laughing', 
                'haha': 'laughing', 
                'hf': 'have fun',
                'hry': 'hurry', 
                'ikr': 'i know right', 
                'lmao': 'laughing my ass off', 
                'lol': 'laughing out loud',
                'n1': 'nice one', 
                'na': 'not available', 
                'qt': 'cutie', 
                'qtpi': 'cutie pie', 
                'rip': 'rest in peace',
                'sry': 'sorry', 
                'tc': 'take care',
                'thnks': 'thanks', 
                'thx': 'thanks', 
                'thnk': 'thanks', 
                'txt': 'text',
                'ugh': 'disgusted', 
                'w8': 'wait', 
                "not sad": "happy"}

    for token in text.split():
        if token in shortcuts.keys():
            token = shortcuts[token]
        full_words.append(token)
    text = " ".join(full_words)
    return text

def remove_stopwords(text):       
    filtered_sentence =[] 
    doc=nlp(text)
    for token in doc:
        if token.is_stop is False: 
          filtered_sentence.append(token.text)   
    return " ".join(filtered_sentence)

def lemmatize(text):
   doc = nlp(text)
   lemmatized_text = []
   for token in doc:
     lemmatized_text.append(token.lemma_)
   return ' '.join(lemmatized_text)

def removing_not(text):
    d = {
        'not sad': 'joy',
        'not bad': 'joy',
        'not boring': 'joy',
        'not wrong': 'joy',
        'not bored': 'joy',
        'not jealous': 'joy',
        'not happy': 'sadness',
        'not well': 'sadness',
        'not suitable': 'anger',
        'not right': 'anger',
        'not good': 'sadness',
        'not excited': 'anger',
        'not funny ': 'sadness',
        'not  kind': 'sadness',
        'not proud': 'anger',
        'not cool': 'anger',
        'not funny': 'anger',
        'not kind': 'anger',
        'not open': 'anger',
        'not safe': 'fear',
        'not enough': 'Empty',
        'not know': 'sadness',
        'not knowing': 'sadness',
        'not believe': 'anger',
        'not believing': 'anger',
        'not understand': 'sadness',
        'not understanding': 'sadness',
        'no doubt': 'joy',
        'not think': 'sadness',
        'not thinking': 'sadness',
        'not recognise': 'sadness',
        'not recognising': 'sadness',
        'not forget': 'anger',
        'not forgetting': 'anger',
        'not remember': 'sadness',
        'not remembering': 'sadness',
        'not imagine': 'sadness',
        'not imagining': 'sadness',
        'not mean': 'sadness',
        'not meaning': 'sadness',
        'not agree': 'anger',
        'not agreeing': 'sadness',
        'not disagree': 'joy',
        'not disagreeing': 'joy',
        'not deny': 'sadness',
        'not denying': 'sadness',
        'not promise': 'anger',
        'not promising': 'anger',
        'not satisfy': 'sadness',
        'not satisfying': 'sadness',
        'not realise': 'sadness',
        'not realising': 'sadness',
        'not appear': 'anger',
        'not appearing': 'anger',
        'not please': 'sadness',
        'not pleasing': 'sadness',
        'not impress': 'sadness',
        'not impressing': 'sadness',
        'not surprise': 'sadness',
        'not surprising': 'sadness',
        'not concern': 'sadness',
        'not concerning': 'sadness',
        'not have': 'sadness',
        'not having': 'sadness',
        'not own': 'sadness',
        'not owning': 'sadness',
        'not possess': 'sadness',
        'not possessing': 'sadness',
        'not lack': 'sadness',
        'not lacking': 'sadness',
        'not consist': 'sadness',
        'not consisting': 'sadness',
        'not involve': 'sadness',
        'not involving': 'sadness',
        'not include': 'sadness',
        'not including': 'sadness',
        'not contain': 'sadness',
        'not containing': 'sadness',
        'not love': 'sadness',
        'not like': 'anger',
        'not hate': 'joy',
        'not hating': 'joy',
        'not adore': 'sadness',
        'not adoring': 'sadness',
        'not prefer': 'sadness',
        'not preferring': 'sadness',
        'not care': 'anger',
        'not mind': 'anger',
        'not minding': 'sadness',
        'not want': 'anger',
        'not wanting': 'sadness',
        'not need': 'anger',
        'not needing': 'anger',
        'not desire': 'sadness',
        'not desiring': 'sadness',
        'not wish': 'sadness',
        'not wishing': 'sadness',
        'not hope': 'sadness',
        'not hoping': 'sadness',
        'not appreciate': 'sadness',
        'not appreciating': 'sadness',
        'not value': 'sadness',
        'not valuing': 'sadness',
        'not owe': 'sadness',
        'not owing': 'sadness',
        'not seem': 'sadness',
        'not seeming': 'sadness',
        'not fit': 'sadness',
        'not fitting': 'sadness',
        'not depend': 'sadness',
        'not depending': 'sadness',
        'not matter': 'sadness',
        'not afford': 'sadness',
        'not affording': 'sadness',
        'not aim': 'sadness',
        'not aiming': 'sadness',
        'not attempt': 'anger',
        'not attempting': 'anger',
        'not ask': 'anger',
        'not asking': 'anger',
        'not arrange': 'anger',
        'not arranging': 'anger',
        'not beg': 'anger',
        'not begging': 'anger',
        'not begin': 'anger',
        'not beginning': 'anger',
        'not caring': 'anger',
        'not choose': 'anger',
        'not choosing': 'anger',
        'not claim': 'anger',
        'not claiming': 'anger',
        'not consent': 'anger',
        'not consenting': 'anger',
        'not continue': 'anger',
        'not continuing': 'anger',
        'not dare': 'anger',
        'not daring': 'anger',
        'not decide': 'sadness',
        'not deciding': 'sadness',
        'not demand': 'anger',
        'not demanding': 'anger',
        'not deserve': 'anger',
        'not deserving': 'anger',
        'not expect': 'anger',
        'not expecting': 'anger',
        'not fail': 'joy',
        'not failing': 'joy',
        'not get': 'sadness',
        'not getting': 'sadness',
        'not hesitate': 'sadness',
        'not hesitating': 'sadness',
        'not hurry': 'joy',
        'not hurrying': 'joy',
        'not intend': 'sadness',
        'not intending': 'sadness',
        'not learn': 'anger',
        'not learning': 'anger',
        'not liking': 'anger',
        'not loving': 'sadness',
        'not manage': 'anger',
        'not managing': 'anger',
        'not neglect': 'sadness',
        'not neglecting': 'sadness',
        'not offer': 'anger',
        'not offering': 'anger',
        'not plan': 'anger',
        'not planing': 'anger',
        'not prepare': 'anger',
        'not preparing': 'anger',
        'not pretend': 'anger',
        'not pretending': 'anger',
        'not proceed': 'anger',
        'not proceeding': 'anger',
        'not propose': 'anger',
        'not proposing': 'sadness',
        'not refuse': 'sadness',
        'not refusing': 'sadness',
        'not start': 'sadness',
        'not starting': 'sadness',
        'not stop': 'joy',
        'not stopping': 'joy',
        'not struggle': 'anger',
        'not struggling': 'anger',
        'not swear': 'anger',
        'not swearing': 'anger',
        'not threaten': 'joy',
        'not threatening': 'joy',
        'not try': 'anger',
        'not trying': 'anger',
        'not volunteer': 'anger',
        'not volunteering': 'anger',
        'not wait': 'anger',
        'not waiting': 'anger',
        'not feel': 'sadness',
        'not feeling': 'sadness',
        }

    f = re.findall(r"not\s\w+", text)
    for i in f:
        try:
            text = text.replace(i, d[i])
        except KeyError as ex:
            print(f'KeyError: {ex}')

    text = text.lower()
    return text

def standardize_accented_chars(text):
    return (
        unicodedata.normalize('NFKD', text)
        .encode('ascii', 'ignore')
        .decode('utf-8', 'ignore'))

def expand_contractions(text):
    expanded_words = [] 
    for word in text.split():
       expanded_words.append(contractions.fix(word)) 
    return ' '.join(expanded_words)

def remove_punctuation(text):
    return ''.join([c for c in text if c not in string.punctuation])

def cleaning(text):
    text = text.lower()
    text = re.sub(r'http\S+|www.\S+', '', text)
    text = expand_contractions(text)
    text = remove_punctuation(text)
    text = standardize_accented_chars(text)
    text = removing_not(text)
    text = removing_shortcuts(text)
    text = lemmatize(text)
    text = ' '.join([i for i in text.split() if not i.isdigit()])
    text = remove_stopwords(text)
    text = text.replace('   ', ' ')
    text = text.replace('  ', ' ')
    return text

def get_sentiment(input):
    sid = SentimentIntensityAnalyzer()
    sentiment = "neutral"
    sentiment_dict = sid.polarity_scores(input)
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        sentiment = "positive"
    elif sentiment_dict['compound'] <= - 0.05 :
        sentiment = "negative"
    else :
        sentiment = "neutral"

    if sentiment_dict['neu'] >= 0.65 :
        sentiment = "neutral"

    return sentiment

def get_emotion(input, sentiment=''):
    if sentiment == '':
        sentiment = get_sentiment(input)
    text = cleaning(input).split()
    
    emotion_values = []
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, 'data', 'all_en_merged.json')

    with open(data_path,'r') as f:
        data = json.load(f)

    emotions = {
        "fear": 0.0, 
        "anger": 0.0, 
        "trust": 0.0, 
        "surprise": 0.0, 
        "sadness": 0.0, 
        "disgust": 0.0, 
        "joy": 0.0, 
        "anticipation": 0.0}
    
    y = 0
    try:
        for idx, word in enumerate(text):
            try:
                emos = get_emos(word, idx, text, data)
                if emos:
                    for emo in emos:
                        if emo not in ['positive', 'negative']:
                            emotions[emo] += 1
                        if sentiment == 'positive':
                            if emo in ['trust', 'surprise', 'joy', 'anticipation']:
                                emotions[emo] += 0.5  
                        elif sentiment == 'negative':
                            if emo in ['fear', 'anger', 'sadness', 'disgust']:
                                emotions[emo] += 0.5
            except Exception as e:
                print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    if sum(emotions.values()) == 0:
        return emotions
    for i in emotions:
        emotion_values.append(round((emotions[i] / sum(emotions.values())), 2))
    for j in emotions:
        emotions[j] = emotion_values[y]
        y += 1
    return emotions

#need to get multiple word phrases
def get_emos(word, idx, text, data):
    if word in data:
        return data[word]
    else:
        keys = [k for k in data.keys() if k.startswith(word)]
        if keys:
            for key in keys:
                split_key = key.split()
                len_key = len(split_key)
                if (idx+len_key <= len(text)):
                    words = text[idx:idx+len_key]
                    if set(split_key) == set(words):
                        return data[key]
    return None

def top_emotion(input):
    sentiment = get_sentiment(input)
    emotions = get_emotion(input, sentiment)
    #opposite_emotion = { "joy":"sadness", "sadness":"joy", 
    #                     "surprise":"anticipation", "anticipation":"surprise",
    #                     "trust":"disgust", "disgust":"trust",
    #                     "fear":"anger", "anger":"fear" }

    sorted_tuples = dict(sorted(emotions.items(), 
                                key=lambda item: item[1], 
                                reverse=True))
    print(sorted_tuples)

    top = next(iter(sorted_tuples.items()))

    return top

def get_mixed_emotion(input):
    sentiment = get_sentiment(input)
    emotions = get_emotion(input, sentiment)
    sorted_tuples = sorted(emotions.items(), key=lambda item: item[1], reverse=True)
    print(sorted_tuples)
    top1 = sorted_tuples[0]
    top2 = sorted_tuples[1]
    if top1[1] + top2[1] > 0.5 and top1[1] - top2[1] < 0.15:
        return mixed_emotion([top1[0], top2[0]])
    else:
        return top1[0]

def mixed_emotion(top2):
    mixed_emotion = {
        'love' : ['joy', 'trust'],
        'guilt' : ['joy', 'fear'],
        'delight': ['joy', 'surprise'],
        'submission': ['trust', 'fear'],
        'awe': ['fear', 'surprise'],
        'despair': ['fear', 'sadness'],
        'shame': ['fear', 'disgust'],
        'disappointment': ['surprise', 'sadness'],
        'unbelief': ['surprise', 'disgust'],
        'outrage': ['surprise', 'anger'],
        'remorse': ['sadness', 'disgust'],
        'envy': ['sadness','anger'],
        'pessimism': ['sadness', 'anticipation'],
        'contemt': ['disgust', 'anger'],
        'cynicism': ['disgust', 'anticipation'],
        'morbidness': ['disgust', 'joy'],
        'aggression': ['anger', 'anticipation'],
        'pride': ['anger', 'joy'],
        'dominance': ['anger', 'trust'],
        'optimism': ['anticipation', 'joy'],
        'hope': ['anticipation', 'trust'],
        'anxiety': ['anticipation', 'fear']
     }

    #return the mixed emotion
    for key in mixed_emotion:
        if set(top2) == set(mixed_emotion[key]):
            return key

    #else return the emotion
    return top2[0]

def get_emotion_list():
    emotion_list = [
        'fear',
        'anger',
        'trust',
        'surprise',
        'sadness',
        'disgust',
        'joy',
        'anticipation',
        'love',
        'guilt',
        'delight',
        'submission',
        'awe',
        'despair',
        'shame',
        'disappointment',
        'unbelief',
        'outrage',
        'remorse',
        'envy',
        'pessimism',
        'contemt',
        'cynicism',
        'morbidness',
        'aggression',
        'pride',
        'dominance',
        'optimism',
        'hope',
        'anxiety'
    ]
    return emotion_list

def get_counts():
    import csv
    nrc_merged = 0
    nrc_en = 0
    text2emo = 0
    investopedia = 0
    all_merged = 0

    with open('data/nrc_en.json','r') as f:
        data = json.load(f)
        nrc_en = len(data)
    with open('data/nrc_en_merged.json','r') as f:
        data = json.load(f)
        nrc_merged = len(data)
    with open('data/all_en_merged.json','r') as f:
        data = json.load(f)
        all_merged = len(data)
    with open('data/investopedia.json','r') as f:
        data = json.load(f)
        investopedia = len(data)
    with open('data/text2emotion.tsv','r') as f:
        tsv_file = csv.reader(f, delimiter="\t")
        text2emo = len(list(tsv_file)) - 1

    s = (f'text2emotion: {text2emo} '
         f'nrc_en: {nrc_en} '
         f'nrc_merged: {nrc_merged} '
         f'investopedia: {investopedia} '
         f'all_merged: {all_merged}')
    print(s)