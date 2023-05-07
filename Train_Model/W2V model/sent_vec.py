from gensim.models import KeyedVectors
import numpy as np

model_path = '/home/phanminhgiang/Lab/lab601/thesis/phanminhgiang/Train_Model/W2V model/word_embedding.model'
model = KeyedVectors.load(model_path)

def get_sentence_vector(sentence, model):
    sentence = sentence.lower().split()
    vec = [model[word] for word in sentence if word in model]
    return np.mean(vec, axis=0)

def get_sentence_from_vector(vector, model):
    words = model.similar_by_vector(vector, topn=1)
    return ' '.join([word[0] for word in words])

# Example usage
sentence = 'Tôi muốn mua một chiếc điện thoại mới'
vector = get_sentence_vector(sentence, model)
print(vector)

sentence_from_vector = get_sentence_from_vector(vector, model)
print(sentence_from_vector)
