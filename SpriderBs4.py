from Sprider import Sprider
from bs4 import BeautifulSoup
import time
from ExcelCreate import ExcelCreate

class SpriderBs4(Sprider):
	
	def __init__(self):
		
		super().__init__()
	
	def parse_list(self, text):
		try:
			soup = BeautifulSoup(text, "lxml")
			contents = soup.find_all("div", class_="sojob-item-main")
			for content in contents:
				try:
					title = content.find("div", class_="job-info").a.text.strip()
					salary = content.find("span", class_="text-warning").text.strip()
					addr = content.find("p", class_="condition clearfix").a.text.strip()
					edu = content.find("span", class_="edu").text.strip()
					work = content.find("p", class_="condition clearfix").contents[7].text.strip()
					company = content.find("p", class_="company-name").a.text.strip()
					field = content.find("p", class_="field-financing").a.text.strip()
					href = content.find("div", class_="job-info").a.get("href")
					#print(href)
					
					self.job_info.append(title)
					self.job_info.append(salary)
					self.job_info.append(addr)
					self.job_info.append(edu)
					self.job_info.append(work)
					self.job_info.append(company)
					self.job_info.append(field)
					self.job_info.append(href)
					
					self.request_detail(href)
					time.sleep(1)
				except Exception as e:
					job_info = ['error','error','error','error','error','error','error','error']
				
		except Exception as e:
			print("error:%s"%e)
			
	def parse_href_detail_list(self, text):
		try:
			soup = BeautifulSoup(text, "lxml")
			detail = soup.find("div", class_="content-word").text.strip()
		except Exception as e:
			print("error:%s"%e)

			detail = "no data"
		self.job_info.append(detail)
		self.count = self.count + 1
		print("写入数据中，第%d条数据"%self.count)
		ExcelCreate.write_excel(self.excel_book, self.excel_sheet, self.count, self.job_info, "job_Bs4.xls")
		self.job_info = []

#if __name__ == "__main__":
#	result = SpriderBs4()
#	result.crawler_data()
