# -*- coding: utf-8 -*-
import survey
table = survey.Pregnancies()
table.ReadRecords()

outcomes = [r for r in table.records if r.outcome == 1]

first_outcomes = [r for r in outcomes if r.birthord == 1]

after_second_outcomes = [r for r in outcomes if r.birthord != '' and r.birthord != 1]

# http://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=PREG&section=A&subSec=8016&srtLabel=611933
print u'第１子', len(first_outcomes)
print u'第2子', len(after_second_outcomes)
