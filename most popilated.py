from collections import Counter
from itertools import accumulate
import operator

def most_populated(population, single=True):
    delta = Counter(x[0] for x in population)
    delta.subtract(Counter(x[1]+1 for x in population))
    start, end = min(delta.keys()), max(delta.keys())
    years = list(accumulate(delta[year] for year in range(start, end)))
    return max(enumerate(years), key=operator.itemgetter(1))[0] + start if single else \
           [i + start for i, val in enumerate(years) if val == max(years)]
           

print(most_populated([(1920, 1939), (1911, 1944),
                      (1920, 1955), (1938, 1939)]))
                      