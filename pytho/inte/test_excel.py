#!/user/bin/env python
#_*_ coding:utf-8 _*_
import xlrd
xlsfile = r'F:\hyj\pytho\inte\data_config\test_1.xls'
book = xlrd.open_workbook(xlsfile)
sheet0 = book.sheet_by_index(0)#通过sheet索引获取sheet对象
print '1、',sheet0
sheet_name = book.sheet_names()[0]#获取指定索引的sheet的表名字
print '2、',sheet_name
sheet1 = book.sheet_by_name(sheet_name)#通过sheet名字来获取
nrows = sheet0.nrows#获取总行数
print '3、',nrows
#循环打印每一行的内容
for i in range(nrows):
    print sheet1.row_values(i)
ncols = sheet0.ncols#获取总列数
print '4、',ncols
row_data = sheet0.row_values(0)#获取第一行的数据列表
print '5、',row_data
col_data = sheet0.col_values(0)#获取第一列的数据列表
print '6、',col_data
#通过坐标读取表格的数据
cell_data1 = sheet0.cell_value(0,0)
print '7、',cell_data1
cell_data2 = sheet0.cell_value(0,1)
print '8、',cell_data2

d1 = []
d2 = []
d1 = cell_data1
d2 = cell_data2
new_dict = dict(zip(d1,d2))
print new_dict
