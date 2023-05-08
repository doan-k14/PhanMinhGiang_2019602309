from gensim.models import KeyedVectors
# from sklearn.decomposition import PCA
import numpy as np

model = KeyedVectors.load('word_embedding.model')
vec_dict={}
def word2vec(word, model):
    vec = model.wv[word]
    return (vec)

# def sent2vec(sentence, model):
#     sentence = sentence.lower().split()
#     vec = [model.wv[word] for word in sentence if word in model]
#     return np.mean(vec, axis=0)


# def vec2sent(vector, model):
#     sim_words = model.similar_by_vector(vector, topn=6)
#     words = [word[0] for word in sim_words]
#     return ' '.join(words)


sent = 'chó'
vec = word2vec(sent, model)
sent2 = model.wv.similar_by_vector(vec, topn=1)
# print(vec)
print(sent2)

# sent2 = vec2sent(vec, model)
# print (sent2)
# word = 'chó'
# vec = word2vec(word, model)
# word2 = model.similar_by_vector(vec)
# print(word2)