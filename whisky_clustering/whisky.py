import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster.bicluster import SpectralCoclustering

"""
# index keyword argument to change name of the index
x = pd.Series([6, 3, 8, 6], index=["q","w","e","r"])

print(x)
print(x[["w","r"]])

print(x.index)

sorted(x.index)
print(x.reindex(sorted(x.index)))

y = pd.Series([7, 3, 5, 2], index=["e","q","r","t"])

print(x+y)

age = {"Tim":29, "Jim":31, "Pam":27, "Sam":35}
x = pd.Series(age)

#print(x)

data = {'name': ['Tim', 'Jim', 'Pam', 'Sam'],
        'age' : [29, 31, 27, 35],
        'ZIP' : ['02115', '02130', '67700', '00100']}

x = pd.DataFrame(data, columns = ["name", "age","ZIP"])

#print(x)

#print(x["name"])
#print(x.name)
"""

whisky = pd.read_csv('whiskies.txt')
whisky["Region"] = pd.read_csv('regions.txt')
#print(whisky.head)
#print(whisky.tail)

#print(whisky.iloc[5:10, 0:5])
#print(whisky.columns)

flavours = whisky.iloc[:, 2:14]
#print(flavours)

corr_flavour = pd.DataFrame.corr(flavours)
#print(corr_flavour)

#flavours correlations
plt.figure(figsize=(10,10))
plt.pcolor(corr_flavour)
plt.colorbar()
plt.savefig("corr_flavour.pdf")

#Distillery correlations
corr_whisky = pd.DataFrame.corr(flavours.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.axis("tight")
plt.colorbar()
plt.savefig("corr_whisky.pdf")

#Spectral Coclustering - Finding clusters of objects by similar attributes
model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whisky)
print(model.rows_)
clustersum = np.sum(model.rows_, axis=1)
print(clustersum)
clustersumcol = np.sum(model.rows_, axis=0)
print(clustersumcol)
print(model.row_labels_)

whisky['Group'] = pd.Series(model.row_labels_, index=whisky.index)
whisky = whisky.iloc[np.argsort(model.row_labels_)]
whisky = whisky.reset_index(drop=True)
correlations = pd.DataFrame.corr(whisky.iloc[:, 2:14].transpose())
correlation = np.array(correlations)
#Plot
plt.figure(figsize=(14,7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title("Original")
plt.axis("tight")
plt.subplot(122)
plt.pcolor(correlations)
plt.title("Rearranged")
plt.axis("tight")
plt.colorbar()
plt.savefig("correlations.pdf")



data = pd.Series([1,2,3,4])
print(data)
data = data.iloc[[3,0,1,2]]
print(data)
data = data.reset_index(drop=True)
print(data)
print(data[0])
