import xlwt

class ExcelCreate(object):
	
	def create_excel(sheet_name, title):
		book = xlwt.Workbook()
		sheet = book.add_sheet(sheet_name)
		for i in range(len(title)):
			sheet.write(0, i, title[i])
		return book, sheet
		
	def write_excel(book, sheet, count, data, excel_name):
		
		for num in range(len(data)):
			sheet.write(count, num, data[num])
		book.save(excel_name)
		
