import pandas as PD

def get_Sheet(filepath,sheetName):
    sheetNameFrame = PD.read_Excel(filepath,sheetName)
    return sheetNameFrame

def get_row_count(filePath, sheetName):
    sheet = get_Sheet(filePath, sheetName)
    rowCount = sheet.shape[0]
    return  rowCount

def get_cell_value(filePath, sheetName, rowNum, colNum):
    sheet = get_Sheet(filePath, sheetName)
    value = sheet.loc[rowNum][colNum]
    return value

def write_to_excel(filePath, sheetName, rowNum, colNum, valueToEnter):
    sheet = get_Sheet(filePath, sheetName)
    sheet.loc[rowNum][colNum] = valueToEnter
    wr = PD.ExcelWriter(filePath)
    sheet.to_excel(wr, sheetName)
    wr.save()
