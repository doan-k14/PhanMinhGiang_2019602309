from text_summarizing import TextSummarizing
import numpy as np
ts = TextSummarizing(5)
file_path = '../Test_file/Ngay_he.txt'
file = open(file_path, 'r')
paragraph = file.read() 
ts.para2vec_list(paragraph)
clusters = ts.clustering()
close_index_vec_list = ts.find_center_vec(clusters)
vec_for_summary = [ts.vec_list[index] for index in close_index_vec_list]
summary = ts.we.veclist2para(vec_for_summary)
print(summary)
