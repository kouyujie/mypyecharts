# -*- coding: utf-8 -*-
import xlrd
book = xlrd.open_workbook(u"中文名.xlsx")
s = book.sheet_by_index(1)
i = 0
while i <= 15:
    #print (s.row_values(i))
    print s.cell_value(4+i,0),s.cell_value( 4+i,1 )
    i += 1

