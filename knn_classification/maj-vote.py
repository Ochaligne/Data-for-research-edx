
import random

def majority_votes(votes):
    """
    Return most common element in votes.
    """
    vote_counts = {}
    for vote in votes:
        #known word
        if vote in vote_counts:
             vote_counts[vote] += 1
        #unknown word
        else:
            vote_counts[vote] = 1

    winners = []
    max_counts = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_counts:
            #print(vote, count)
            winners.append(vote)

    return random.choice(winners)


#vote_counts = majority_votes(votes)
#winner = majority_votes(votes)
#print(vote_counts)
#print(max(vote_counts))
#print(max(vote_counts.keys()))
#max_counts = max(vote_counts.values())
#print(max_counts)
#print(winner)

import scipy.stats as ss
def majority_votes_short(votes):
    """
    Return most common element in votes.
    """
    mode, count = ss.mstats.mode(votes)
    return mode

votes = [1,2,3,1,2,3,1,2,3,3,3,3,2,2,2]
mode = majority_votes_short(votes)
print(mode)
