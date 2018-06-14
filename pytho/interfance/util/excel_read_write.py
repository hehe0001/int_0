#!/user/bin/env python
#_*_ coding:utf-8 _*_
import xlwt
import xlrd
#创建excel表并写入内容
#创建一个Workbook对象，这就相当于创建了一个excel文件
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
'''
Workbook类初始化时有encoding和style_compression参数
encoding设置字符编码，使得excel可以输出中文
style_compression：表示是否压缩，不常用
'''
#创建一个sheet对象，一个sheet对象对应excel文件的一张表格
sheet =book.add_sheet('test',cell_overwrite_ok=True)
#test是表名称，cell_overwrite_ok表示是否可以覆盖单元格，一般默认值为flase
#向test表中添加上数据
sheet.write(0,0,'Englishname')#0行0列写入englishname
sheet.write(1,0,'Marcovaldo')
txt1=u"中文名字"#需要将中文内容设置为Unicode编码
sheet.write(0,1,txt1.encode('utf-8'))#
txt2=u"马可波罗"
sheet.write(1,1,txt2.encode('utf-8'))
book.save('F:\\hyj\\study\\test.xls')

#读取excel表中的内容
xlsfile=r'F:\\hyj\\study\\test.xls'#打开指定路径的xls文件
book=xlrd.open_workbook(xlsfile)#得到excel文件的book对象，实例化对象
sheet0=book.sheet_by_index(0)#通过sheet索引来获取sheet对象
print '1、',sheet0
sheet_name=book.sheet_names()[0]#获得指定索引的sheet表名字
print '2、',sheet_name
sheet1=book.sheet_by_name(sheet_name)#通过sheet名字来获取，当然如果知道sheet名字就可以直接指定
nrows=sheet0.nrows#获取总行数
print  '3、',nrows
#循环打印每行的内容
for i in range(nrows):
    print sheet1.row_values(i)
ncols=sheet0.ncols#获取总列数
print '4、',ncols
row_data=sheet0.row_values(0)#获取第一行的数据列表
print row_data
col_data=sheet0.col_values(0)#获取第一列的数据列表
print '5、',col_data
#通过坐标读取表格中的数据
cell_value1=sheet0.cell_value(0,0)
print '6、',cell_value1
cell_value2=sheet0.cell_value(0,1)
print '7、',cell_value2





