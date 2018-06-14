#!/user/bin/env python
#_*_ coding:utf-8 _*_
import xlrd
xlsfile=r'C:\Users\yibao\Desktop\\xiaofei.xlsx'#打开指定路径的xls文件
book=xlrd.open_workbook(xlsfile)#得到excel文件的book对象，实例化对象
#data=xlrd.open_workbook('C:\Users\yibao\Desktop\日常消费.xlsx')
table =book.sheets()[0]
print table
table1=book.sheet_by_index(0)
print table1
table2 = book.sheet_by_name(u'2018-2')
print table2
print table.row_values(4)
print table.col_values(1)
print table.cell(1,4)
print table.nrows
print table.ncols