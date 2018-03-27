from Sprider import Sprider
from SpriderXpath import SpriderXpath
from SpriderBs4 import SpriderBs4
from ExcelCreate import ExcelCreate

def selectway():
	print("Operation instructions:")
	print("\t\t\t1.Xpath")
	print("\t\t\t2.BeautifulBs4")
	
	num = int(input("Please choose a way:"))

	try:
		if num == 1:
			x = SpriderXpath()
			x.crawler_data()
		elif num == 2:
			result = SpriderBs4()
			result.crawler_data()
		else:
			print("error, Please input right number, and run again!")
	except Exception as e:
		print("error:%s"%e)
		
if __name__ == "__main__":
	selectway()
