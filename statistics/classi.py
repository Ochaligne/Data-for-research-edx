import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
np.random.seed(1)

h = 1 #
sd = 1 # standard devition
n = 50 # number of observation
#Vectors
def gen_data(n, h, sd1, sd2):
    x1 = ss.norm.rvs(-h, sd1, n)
    y1 = ss.norm.rvs(0, sd1, n)
    x2 = ss.norm.rvs(h, sd2, n)
    y2 = ss.norm.rvs(0, sd2, n)
    return (x1, y1, x2, y2)


(x1, y1, x2, y2) = gen_data(50, 1, 1, 1.5)

(x1, y1, x2, y2) = gen_data(1000, 1.5, 1, 1.5)

#(x1, y1, x2, y2) = gen_data(1000, 0, 1, 1) # all mixed up hard to classify
#(x1, y1, x2, y2) = gen_data(1000, 1, 2, 2.5) # mixed up but slightly left/right divide
#(x1, y1, x2, y2) = gen_data(1000, 10, 100, 100) # all mixed up maybe more orange in middle
#(x1, y1, x2, y2) = gen_data(1000, 20, .5, .5) # clear left right

def plot_data(x1, y1, x2, y2):
    plt.figure()
    plt.plot(x1, y1, "o", ms=2)
    plt.plot(x2, y2, "o", ms=2)
    plt.xlabel("$X_1$")
    plt.ylabel("$X_2$")
    plt.show()

#plot_data(x1, y1, x2, y2)

clf = LogisticRegression()
X = np.vstack((np.vstack((x1, y1)).T, np.vstack((x2, y2)).T)) #transposed stack because shape return 2rows*1000columns
#print(X.shape)
n = 1000
y = np.hstack((np.repeat(1,n), np.repeat(2,n)))
#print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5, random_state=1)

#print(X_train.shape)
#print(y_test.shape)

clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))
print(clf.predict_proba(np.array([-2, 0]).reshape(1, -1)))
print(clf.predict(np.array([-2, 0]).reshape(1, -1)))

def plot_probs(ax, clf, class_no):
    xx1, xx2 = np.meshgrid(np.arange(-5, 5, 0.1), np.arange(-5, 5, 0.1))
    probs = clf.predict_proba(np.stack((xx1.ravel(), xx2.ravel()), axis=1))
    Z = probs[:,class_no]
    Z = Z.reshape(xx1.shape)
    CS = ax.contourf(xx1, xx2, Z)
    cbar = plt.colorbar(CS)
    plt.xlabel("$X_1$")
    plt.ylabel("$X_2$")

plt.figure(figsize=(5,8))
ax = plt.subplot(211)
plot_probs(ax, clf, 0)
plt.title("Pred. prob for class 1")
ax = plt.subplot(212)
plot_probs(ax, clf, 1)
plt.title("Pred. prob for class 2");
plt.show()
