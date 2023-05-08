import string
from gensim.models import Word2Vec
import numpy as np

class WordEmbedding:


    def __init__(self, model_vec_dict:dict):
        self.model = Word2Vec.load('/home/phanminhgiang/Lab/lab601/thesis/phanminhgiang/Train_Model/Models/W2V/word_embedding.model')
        self.model_vec_dict = model_vec_dict


    def sent2vec(self, sentence)->dict:
        model = self.model
        vec_dict = self.model_vec_dict
        word_list = sentence.lower().split()
        vec = [model.wv[word] for word in word_list if word in model.wv]
        vec_dict[sentence]=np.mean(vec, axis=0)
        return vec_dict[sentence]
    """
    This function receive a sentence than encode it to a vector and add it to the vector dictionary of the model
    """


    def vec2sent(self, vector)->string:
        vec_dict = self.model_vec_dict
        for key, value in vec_dict.items():
            if str(value) == str(vector):
                return key


    def para2vecdict(self, paragraph):
        """
        This function receive a paragraph contains many sentences than encode it to vectors and add it to the vector dictionary of the model
        """
        sent_list = paragraph.split(". ")
        for sent in sent_list:
            if sent.endswith('.'):
                sent = sent[:-1]
            self.sent2vec(sent)



    def veclist2para(self, vec_list)->string:
        paragraph = ''
        model_vec_dict = self.model_vec_dict
        for vec in vec_list:
            paragraph += self.vec2sent(vec) + '. '
        return paragraph