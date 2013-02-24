import Pmf

def Mode(hist):
    " Return the most frquency value from Hist Object"
    return reduce(lambda sum, x: sum if sum[1] > x[1] else x, iter(hist.Items()))

hist = Pmf.MakeHistFromList([1, 2, 2, 3, 5])
print Mode(hist)

