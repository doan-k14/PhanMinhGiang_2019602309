import re
import string

from pyvi import ViTokenizer
import pandas as pd

corpus_file = "/home/giangpm/thesis/Data/wikicorpus.txt"
stopwords_file = "./stopwords.csv"
stopwords = pd.read_csv(stopwords_file, header=None)[0].tolist()

def preprocess_text(text):
    text = re.sub(r'<.*?>', '', text)
    words = ViTokenizer.tokenize(text).split()
    words = [word for word in words if word not in stopwords]
    return " ".join(words)

def segment_sentences(text):
    sentences = re.split(r'(?<=[\.\?\!])\s+', text)
    sentences = [sentence.strip() for sentence in sentences]
    return sentences

def segment_words(sentence):
    words = ViTokenizer.tokenize(sentence).split()
    words = [word for word in words if word not in stopwords]
    return words

with open(corpus_file, "r", encoding="utf-8") as f:
    with open("./datatrain.txt", "w", encoding="utf-8") as f_datatrain:
        count =0
        for line in f:
            count += 1
            line = preprocess_text(line)
            sentences = segment_sentences(line)
            for sentence in sentences:
                words = segment_words(sentence)
                f_datatrain.write(" ".join(words) + "\n")
            if (count % 10000 == 0):
                print("Writing"+str(count))
