import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

#loop over all points
    #compute distance between p and every other points
# sort distance and return those k points that are nearest to point p
points = np.array([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])
outcomes = np.array([0,0,0,0,1,1,1,1,1])

p = np.array([2.5, 2])
def distance(p1,p2):
    """Finds the distance between p1 and p2"""
    return np.sqrt(sum(np.power(p2-p1, 2)))

def find_nearest_neighours(p, points, k=5):
    """Find the k nearest neighbors of point p and return their indices"""
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]

def majority_votes_short(votes):
    """
    Return most common element in votes.
    """
    mode, count = ss.mstats.mode(votes)
    return mode

def knn_predict(p,points, outcomes, k=5):
    # find k nearest neighbours
    ind = find_nearest_neighours(p, points, k)
    #predict the class of based on majority vote
    return majority_votes_short(outcomes[ind])

"""
#print(points)
#print(p)
plt.plot(points[:,0], points[:,1],"ro")
plt.plot (p[0], p[1],"bo")
plt.axis([0.5, 3.5, 0.5, 3.5])
plt.show()

ind = find_nearest_neighours(p, points, 3); print(points[ind])
"""

def generate_synth_data(n=50):
    """Create two sets of points from bivariate normal distributions."""
    points = np.concatenate((ss.norm(0,1).rvs((n,2)), ss.norm(1,1).rvs((n,2))), axis=0)
    outcomes = np.concatenate((np.repeat(0, n), np.repeat(1, n)))
    return (points, outcomes)
#predict = knn_predict(np.array([2.5, 2.7]), points, outcomes, k=2)
#print(predict)
n=20
generate_synth_data()
plt.figure()
plt.plot(points[:n,0], points[:n,1], "ro")
plt.plot(points[n:,0], points[n:,1], "bo")
plt.savefig("bivardata.pdf")
