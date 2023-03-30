from engine import Engine
from file_reader import *
import plot
from sklearn import preprocessing
import numpy as np

class AppLogic:

    def run(self):
        plt = plot.Plot()
        reader = file_reader()
        data = np.array(reader.read('data'))
        data = preprocessing.StandardScaler().fit_transform(data)
        engine = Engine()

        kmeans = engine.get_kmeans(data, 15)
        plt.create_plot(data, kmeans.labels_, "KMeans", 1)

        affin_prop = engine.get_affinity_propagation(data)
        plt.create_plot(data, affin_prop.labels_, "Affinity", 2)

        agglomerat = engine.get_agglomerative_clustering(data)
        plt.create_plot(data, agglomerat.labels_, "Agglomerative", 3)

        dbscan = engine.get_db_scan(data)
        plt.create_plot(data, dbscan.labels_, "DBscan", 4)

        mean_shift = engine.get_mean_shift(data)
        plt.create_plot(data, mean_shift.labels_, "Mean Shift", 5)

        plt.show_plot()


