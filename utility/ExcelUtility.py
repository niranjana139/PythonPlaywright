import openpyxl

class ExcelUtility:

    def __init__(self, file_path):
        self.file_path = file_path
        self.workbook = openpyxl.load_workbook(self.file_path)

    def get_sheet(self, sheet_name):
        return self.workbook[sheet_name]

    def get_string_data(self, row, column, sheet_name):
        sheet = self.get_sheet(sheet_name)
        cell_value = sheet.cell(row=row, column=column).value
        return str(cell_value) if cell_value is not None else ""

