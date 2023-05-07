from gensim.models import KeyedVectors
# from sklearn.decomposition import PCA
import numpy as np

model = KeyedVectors.load('./embedding.model')

def word2vec(word, model):
    vec = model[word]
    return (vec)

def sent2vec(sentence, model):
    sentence = sentence.lower().split()
    vec = [model[word] for word in sentence if word in model]
    return np.mean(vec, axis=0)

def vec2sent(vector, model):
    sim_words = model.similar_by_vector(vector, topn=6)
    words = [word[0] for word in sim_words]
    return ' '.join(words)


sent = 'Chú chó thích ăn cơm với cá'
vec = sent2vec(sent, model)
print(vec)

sent2 = vec2sent(vec, model)
print (sent2)
# word = 'chó'
# vec = word2vec(word, model)
# word2 = model.similar_by_vector(vec)
# print(word2)