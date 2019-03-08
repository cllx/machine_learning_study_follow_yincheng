import numpy as np
from sklearn.datasets import load_iris

data=load_iris()
features = data['data']
labels = data['target_names'][data['target']]

plength = features[:,2]
is_setosa = (labels == 'setosa')
print("Maxinum of setosa: {0}." .format(plength[is_setosa].max()))
print("Minimum of others: {0}." .format(plength[~is_setosa].min()))
