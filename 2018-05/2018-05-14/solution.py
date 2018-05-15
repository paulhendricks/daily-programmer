"""
python solution.py abcde
python solution.py dbbaCEDbdAacCEAadcB
"""
import collections
import operator
import sys


def tally(series):
    c = collections.Counter(series)
    users = set(series.lower())
    scores = {k: 0 for k in users}
    for k, v in c.items():
        if k in users:
            scores[k] += v
        elif k.lower() in users:
            scores[k.lower()] -= v

    sorted_scores = sorted(scores.items(), key=operator.itemgetter(1), reverse=True)
    output = ['{}:{}'.format(i, j) for i, j in sorted_scores]
    print(', '.join(output))
    return 0


if __name__ == '__main__':
    tally(sys.argv[1])
