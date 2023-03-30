import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class Plot:

    def __init__(self):
        self.__n_rows = 2
        self.__n_cols = 3
        self.__id = 1

    def create_plot(self, data, labels, title, part):
        plt.figure(self.__id)
        plt.subplot(self.__n_cols, self.__n_rows, part)
        cmap = mcolors.ListedColormap(mcolors.CSS4_COLORS.values())
        plt.scatter(data[:, 0], data[:, 1], c=labels, cmap=cmap, s=1)
        plt.title(title)

    def show_plot(self):
        plt.figure(self.__id)
        plt.tight_layout()
        plt.show()
