import streamlit as st

from transformers import AutoTokenizer,AutoModelForSequenceClassification
from scipy.special import softmax

st.title("Sentiment Analysis")

tweet = st.text_input('Enter a post')

tweet_words = []

for word in tweet.split(' '):
  if word.startswith('@') and len(word) > 1:
    word = '@user'
  elif word.startswith('http'):
    word = 'http'
  tweet_words.append(word)



tweet_proc = " ".join(tweet_words)

roberta = "cardiffnlp/twitter-roberta-base-sentiment"

model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ['Negative','Neutral','Positive']

encoded_tweet = tokenizer(tweet_proc,return_tensors='pt')
output = model(**encoded_tweet)

scores = output[0][0].detach().numpy()

scores = softmax(scores)

analysis = []

for i in range(len(scores)):

  l = labels[i]
  s = scores[i]

  analysis.append([l + " " + str(s)])


maximum = []

for i in analysis:
    temp = i[0].split(" ")
    maximum.append(float(temp[1]))
print(maximum)

if st.button('Predict'):
    if (maximum[0]>maximum[1])&(maximum[0]>maximum[2]):
        st.write('This post is negative')

    if (maximum[1]>maximum[0])&(maximum[1]>maximum[2]):
        st.write('This post is neutral')

    if (maximum[2]>maximum[0])&(maximum[2]>maximum[1]):
        st.write('This post is positive')






