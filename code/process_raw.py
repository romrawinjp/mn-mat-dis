# library is in based
import os
import igl
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt

from meshplot import plot, subplot, interact

root_dir = os.getcwd()
print(root_dir)

sample_dir = "./raw_sample/tapered-cone-solid/RUBBER-9000-P1V5000"
folder_list = [i for i in os.listdir(sample_dir) if ".csv" in i]
print(folder_list)

feature = pd.read_csv(os.path.join(sample_dir, folder_list[0])).iloc[:, 1:]
print(feature.head())

xs = feature["x"]
ys = feature["y"]
zs = feature["z"]

plt.scatter(xs, ys)
plt.show()



