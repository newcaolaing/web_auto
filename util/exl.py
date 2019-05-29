import xlrd
from config.setting import excel_path

class Excel_Opertion(object):
    """excel表数据相关操作"""

    def __init__(self,ex_path=None,index=None):
        if ex_path == None:
            self.excel_path = excel_path  # 默认excel文件路径
        else:
            self.excel_path = ex_path
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index] # sheets第一页数据

    # 获取excel数据，按照每行一个list，添加到一个大的list里面
    def get_data(self):
        result = []
        rows = self.get_lines()
        head=self.table.row_values(0)
        if rows !=None:
            for i in range(1,rows):
                row = self.table.row_values(i)
                # 过滤不执行的用例
                if row[-1] == 'F':continue
                result.append(dict(zip(head,row)))
            return result
        return None

    def api_get_data(self):
        result = []
        rows = self.get_lines()
        head=self.table.row_values(0)
        if rows !=None:
            for i in range(1,rows):
                row = self.table.row_values(i)
                # 将用例名称一一对应
                result.append(dict.fromkeys((row[0],),dict(zip(head[1:],row[1:]))))
            return result
        return None

    # 获取excel行数
    def get_lines(self):
        rows = self.table.nrows  # 获取行数
        if rows > 1:
            return rows
        return None


if __name__ == '__main__':
    a=Excel_Opertion()
    print(a.get_data())