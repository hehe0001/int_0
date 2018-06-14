#!/user/bin/env python
#_*_ coding:utf-8 _*_
import xlrd
import xlwt
from xlutils.copy import copy
class OperationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = 'F:\hyj\pytho\inte\data_config\inte.xls'
            self.sheet_id = 0
        self.data = self.get_data()
    #获取sheet的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables
    #获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows
    #获取单元格的列数：
    def get_ncols(self):
        tables = self.data
        return tables.ncols
    #获取某一个单元格的内容
    def get_cel_value(self,row,col):
        return self.data.cell_value(row,col)
    #写入数据
    def wirte_value(self,row,col,value):
        '''
        写入excel数据
        :param row:
        :param col:
        :param value:
        :return:
        '''
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)#如果不用copy函数，那么会覆盖掉原有excel中的数据
        sheet_data = write_data.get_sheet(0)#得到excel表格的数据
        sheet_data.write(row,col,value)#写入数据
        write_data.save(self.file_name)#保存写入的数据
    #根据对应的case_id找到对应的行的内容
    def get_rows_data(self,case_id):
        row_num = self.get_row_num(case_id)#获取对应的行号
        rows_data = self.get_row_values(row_num)
        return rows_data
    #根据对应的case_id找到对应的行号
    def get_row_num(self,case_id):
        num = 0
        cols_data = self.get_cols_data()#获取某一列的内容
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num = num + 1
    #根据行号找到该行的内容
    def get_row_values(self,row):
        table = self.data
        row_data = table.row_values(row)
        return row_data
    #获取某一列的内容
    def get_cols_data(self,col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols
if __name__ == '__main__':
    opers = OperationExcel()
    print opers.get_data().nrows
    print opers.get_ncols()
    print '**********'
    print opers.get_row_values(3)
    print '**********'
    print opers.get_cols_data(1)
    print '##########'
    print opers.get_rows_data('yb_3')
    print '------->'
    print opers.get_row_num('yb_3')
