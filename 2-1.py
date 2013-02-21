# -*- coding: utf-8 -*-
import thinkstats
import math

values = [0.5, 0.5, 1.5, 1.5, 96]

print u'算術平均(use Mean)', thinkstats.Mean(values)
print u'分散(use Var)', thinkstats.Var(values)
print u'標準偏差', math.sqrt(thinkstats.Var(values))
print u'算術平均 & 分散(use MeanVar)', thinkstats.MeanVar(values)

