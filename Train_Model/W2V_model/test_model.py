from using_model import WordEmbedding
import numpy as np

model_vec_dict={}
we = WordEmbedding(model_vec_dict=model_vec_dict)

sents = ['Có một chú chó trong nhà tôi', 'Nhà tôi có 2 con mèo', 'Hai con mèo chơi cùng hai con chó']
vecs = [we.sent2vec(sent) for sent in sents]
sents2 = [we.vec2sent(vec) for vec in vecs]
print(sents2)

paragraph = 'Có một chú hổ trong nhà tôi. Nhà tôi có 3 con chó. Hai con chó chơi cùng hai con hổ.'
we.para2vecdict(paragraph)
vec_list = [value for key,value in model_vec_dict.items()]
print(we.veclist2para(vec_list))
