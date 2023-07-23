# Emotional Annotation Algorithm

Our emotional annotation algorithm is built upon the foundation laid by the Text2Emotion project, with a series of key enhancements aimed at optimizing its functionality for financial news analysis. We've refined the core algorithm to account for financial terms, integrated a more robust language corpus inclusive of additional words, added support for multi-word phrases, and incorporated an expanded emotional dialect covering a total of 30 emotions.

![Updated Corpus Counts](https://github.com/AI4Finance-Foundation/Fin-Emotion/raw/main/images/corpus.png)

While Text2Emotion's original algorithm worked with five primary emotions, our iteration employs the eight emotions outlined in Plutchik’s model. As a result, we needed to normalize the Text2Emotion embedded corpus. Moreover, we extended our emotional repertoire to cover an additional 22 mixed emotions and improved our utilization of sentiment to further emphasize our calculations.

## Corpus Datasets

Our refined algorithm leverages the combined power of three datasets. The first is Text2Emotion, which we have normalized to correspond with the NRC dataset. The second is the NRC Emotion Lexicon dataset itself, and the third addition is a glossary of domain-specific (financial) phrases. The integration of these resources results in a comprehensive corpus used to process financial news articles.

![Updated Data Cleaning Options](https://github.com/AI4Finance-Foundation/Fin-Emotion/raw/main/images/data_cleaning.png)

## Enhanced Algorithms

Our upgraded algorithm, "get_emotion", creates an emotion vector for news articles, with added functionality to deal with stopwords, lemmatization, contradiction expansions, and emotion vector normalization. It uses the combined corpus of Text2Emotion and NRC EmoLex, along with the financial phrase mappings.

The newly introduced algorithm, "get_mixed_emotion", can handle emotional mixing according to Plutchik's model, delivering the top emotion or a mixed emotion for a given article. The mixed emotion is calculated if the top two emotions comprise 50% of the emotional calculation, and the difference between these two is within 15%. This method allows for more nuanced and accurate emotional analysis.

![Analyzed News Articles](https://github.com/AI4Finance-Foundation/Fin-Emotion/raw/main/images/news.png)

## Usage

Here's how you can use these algorithms to detect emotions in financial texts:
![Plutchik's Emotion Mixing](https://github.com/AI4Finance-Foundation/Fin-Emotion/raw/main/images/emotion_mixing.png)


### get_emotion function

```python
!python -m spacy download en_core_web_sm
from finemotion import emotion

# your input text
input = "The stock market is extremely volatile today!"

# get the sentiment
sentiment = emotion.get_sentiment(input)

# get the emotion
emotion = emotion.get_emotion(input, sentiment)
print(f'Emotion: {emotion}')

This will output:
Emotion: {'fear': 1.0, 'anger': 0.0, 'trust': 0.0, 'surprise': 0.0, 'sadness': 0.0, 'disgust': 0.0, 'joy': 0.0, 'anticipation': 0.0}
```

### get_mixed_emotion function

```python
# your input text
input = "The stock market is extremely volatile today, causing both fear and excitement among traders."

# get the mixed emotion
mixed_emotion = emotion.get_mixed_emotion(input)
print(f'Mixed Emotion: {mixed_emotion}')
```

These functions are beneficial for understanding the emotional undertones present in financial news articles, which can ultimately impact investment decisions.  We recommend using the get_mixed_emotion only as it incorporates all the emotions.

## Contributing

Contributions are always welcome. We value the power of diverse ideas and perspectives and believe that our project can benefit from them. If you have ideas for improvements or notice any bugs, please feel free to fork the repository and create a pull request.

Before making any significant changes, we recommend that you first open an issue to discuss the proposed changes. This helps us keep track of what changes are being made and why, and allows us to provide feedback and guidance.

When you're ready to submit your changes, please ensure that your code adheres to our coding style guidelines and that any new functionality includes appropriate tests.

This library was used in the following research paper: 

McCarthy, S.; Alaghband, G. Enhancing Financial Market Analysis and Prediction with Emotion Corpora and News Co-Occurrence Network. J. Risk Financial Manag. 2023, 16, 226. https://doi.org/10.3390/jrfm16040226


## References

1. [NRC EmoLex](https://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm)
2. [Text2Emotion GitHub Repository](https://github.com/aman2656/text2emotion-library)
3. [Investopedia Financial Terms Dictionary](https://www.investopedia.com/financial-term-dictionary-4769738)