import re
import string

from pyvi import ViTokenizer
import pandas as pd

corpus_file = "/home/phanminhgiang/Lab/lab601/thesis/Data/wikicorpus.txt"
stopwords_file = "/home/phanminhgiang/Lab/lab601/thesis/phanminhgiang/Data/stopwords.csv"
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
    with open("datatrain.txt", "w", encoding="utf-8") as f_datatrain:
        for line in f:
            line = preprocess_text(line)
            sentences = segment_sentences(line)
            for sentence in sentences:
                words = segment_words(sentence)
                f_datatrain.write(" ".join(words) + "\n")
