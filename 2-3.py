import Pmf
from operator import itemgetter

def Mode(hist):
    " Return the most frquency value from Hist Object"
    return reduce(lambda sum, x: sum if sum[1] > x[1] else x, iter(hist.Items()))

def AllModes(hist):
    " Return all values with sorted order by desc"
    getcount = itemgetter(1)
    return sorted(hist.Items(), key=getcount, reverse = True)

hist = Pmf.MakeHistFromList([1,2, 2, 3, 3, 3, 5])
print Mode(hist)
print AllModes(hist)

