from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
import numpy as np
from using_model import WordEmbedding
import numpy as np

class TextSummarizing:


    def __init__(self, n_cluster):
        self.n_cluster = n_cluster
        self.model_vec_dict = {}
        self.vec_list = []
        self.we = WordEmbedding(self.model_vec_dict)


    def para2vec_list(self, paragraph)->list:
        self.we.para2vecdict(paragraph)
        self.vec_list = [value for key, value in self.model_vec_dict.items()]
    

    def clustering(self):
        vec_list = self.vec_list
        kmeans = KMeans(self.n_cluster)
        clusters = kmeans.fit(vec_list)
        return clusters
    

    def find_center_vec(self, clusters):
        vec_list = self.vec_list
        avg = []
        for label in range(self.n_cluster):
            label_group = np.where(clusters.labels_ == label)[0]
            avg.append(np.mean(label_group))
        closest, _ = pairwise_distances_argmin_min(clusters.cluster_centers_, vec_list)
        return closest




