#!/user/bin/env python
#_*_ coding:utf-8 _*_
import xlrd
import xlwt
#向表格中写入数据
#创建一个workbook对象，相当于创建一个excel文件
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
'''
Workbook类初始化时有encoding和style_compression参数
encoding设置字符编码，一般设置为utf-8，就可以在excel中输出中文
style_compression表示是否压缩，不常用
'''
#创建一个sheet对象，一个sheet对象对应excel中的一张表格
sheet = book.add_sheet('test_1',cell_overwrite_ok=True)
#test_1表示表的名字，cell_overwrite_ok表示是否可以覆盖单元格
sheet.write(0,0,'EnglishName')
sheet.write(1,0,'Marco')
txt1 = '中文名字'
sheet.write(0,1,txt1.decode('utf-8'))
txt2 = '马可'
sheet.write(1,1,txt2.decode('utf-8'))
#将表格保存到指定位置
book.save(r'F:\hyj\pytho\inte\test_1.xls')

#读取表格内容
xlsfile = r'F:\hyj\pytho\inte\test_1.xls'
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

