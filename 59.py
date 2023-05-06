def read_login_file():
    # 指定要操作的excel文件
    wb = openpyxl.load_workbook("login.xlsx")
    # 获取要操作的sheet
    sheet = wb["login_case"]
    # 获取工作表中的最大行数
    rows = sheet.max_row
    # 获取工作表中的最大列数
    clos = sheet.max_column



