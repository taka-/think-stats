# -*- coding: utf-8 -*-
import survey
table = survey.Pregnancies()
table.ReadRecords()

outcomes = [r for r in table.records if r.outcome == 1]

first_outcomes = [r for r in outcomes if r.birthord == 1]

after_second_outcomes = [r for r in outcomes if r.birthord != '' and r.birthord != 1]

# http://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=PREG&section=A&subSec=8016&srtLabel=611933
print u'第１子出生数', len(first_outcomes)
print u'第2子以降出生数', len(after_second_outcomes)

print u'第１子平均妊娠期間(w)', 1.0 * reduce(lambda sum,b: sum + b.prglength, first_outcomes, 0) / len(first_outcomes)
print u'第2子以降平均妊娠期間(w)', 1.0 * reduce(lambda sum,b: sum + b.prglength, after_second_outcomes, 0) / len(after_second_outcomes)

print u'第１子平均妊娠期間(h)', 7.0 * 24 * reduce(lambda sum,b: sum + b.prglength, first_outcomes, 0) / len(first_outcomes)
print u'第2子以降平均妊娠期間(h)', 7.0 * 24 * reduce(lambda sum,b: sum + b.prglength, after_second_outcomes, 0) / len(after_second_outcomes)
