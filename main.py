import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import matplotlib.pyplot as plt
text  = open('read.txt',encoding='utf-8').read()
lower_case=text.lower()
print(lower_case)
cleaned_text=lower_case.translate(str.maketrans('','',string.punctuation))
print(cleaned_text)
tokenized_words=word_tokenize(cleaned_text,"english")


final_words=[]
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

emotion_list=[]
with open('emotions.txt','r') as file:
    for line in file:
        clear_line= line.replace("\n",'').replace(",",'').replace("'",'').strip()
        word,emotion=clear_line.split(':')
        print("word :" +word+ " "+"Emotion :"+ emotion)

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w=Counter(emotion_list)
print(w)

def sentiment_analyse(sentiment_text):
    score =SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg=score['neg']
    pos=score['pos']
    if neg>pos:
        print("negative statement")
    elif pos>neg:
        print("positive sentiment")
    else:
        print("Neutral Vibe")

sentiment_analyse(cleaned_text)

fig ,ax1=plt.subplots()
plt.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()