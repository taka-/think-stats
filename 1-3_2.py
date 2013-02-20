# -*- coding: utf-8 -*-
import survey
table = survey.Pregnancies()
table.ReadRecords()

# http://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=PREG&section=A&subSec=8016&srtLabel=611932
# 1   LIVE BIRTH      9148
print u'生児出生', len([r for r in table.records if r.outcome == 1])
