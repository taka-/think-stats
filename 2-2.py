# -*- coding: utf-8 -*-
import survey
import thinkstats
import math

table = survey.Pregnancies()
table.ReadRecords()

first_hours = [r.prglength * 7.0 * 24 for r in table.records if (r.outcome == 1 and r.birthord == 1)]
after_second_hours = [r.prglength * 7.0 * 24 for r in table.records if (r.outcome == 1 and r.birthord != '' and r.birthord != 1)]

print u'第１子分散' , math.sqrt(thinkstats.Var(first_hours))
print u'第2子以降分散' , math.sqrt(thinkstats.Var(after_second_hours))

print u'おまけ'
print u'第１子平均 && 分散偏差' , thinkstats.MeanVar(first_hours)
print u'第2子以降平均 && 分散' , thinkstats.MeanVar(after_second_hours)
