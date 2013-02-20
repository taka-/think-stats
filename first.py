# -*- coding: utf-8 -*-
import survey
table = survey.Pregnancies()
table.ReadRecords()
print u'妊娠レコードの総数', len(table.records)


print len([r for r in table.records if r.outcome == 1])
