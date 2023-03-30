from sklearn.cluster import KMeans, AffinityPropagation, MeanShift, AgglomerativeClustering, DBSCAN

class Engine:

    def get_kmeans(self, data, n_count):
        kmeans = KMeans(n_clusters=n_count, max_iter=150).fit(data)
        return kmeans

    #https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html
    def get_affinity_propagation(self, data):
        affinity_propagation = AffinityPropagation(convergence_iter=50, damping=0.97).fit(data)
        return affinity_propagation

    # https: // scikit - learn.org / stable / modules / generated / sklearn.cluster.AgglomerativeClustering.html
    def get_agglomerative_clustering(self, data):
        agglomerative = AgglomerativeClustering(n_clusters=15).fit(data)
        return agglomerative

    # https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html
    def get_db_scan(self, data):
        dbscan = DBSCAN(eps=0.16, min_samples=30).fit(data)
        return dbscan

    # https: // scikit - learn.org / stable / modules / generated / sklearn.cluster.MeanShift.html
    def get_mean_shift(self, data):
        mean_shift = MeanShift(bandwidth=0.3).fit(data)
        return mean_shift
