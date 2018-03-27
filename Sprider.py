import requests
import time
from ExcelCreate import ExcelCreate

class Sprider(object):
	
	def __init__(self):
		
		self.excel_title = ["招聘标题", "待遇", "地区", "学历要求", "经验", "公司名称", "公司行业", "连接", "职位描述"]
		self.sheet_name = "job"
		return_excel = ExcelCreate.create_excel(self.sheet_name, self.excel_title)
		self.excel_book = return_excel[0]
		self.excel_sheet = return_excel[1]
		self.job_info = []
		self.count = 0
		
	def crawler_data(self):
		for page in range(5):
			
			print("第%d页\n"%(page+1))
			url = "https://www.liepin.com/zhaopin/?pubTime=&ckid=90d24f8653e40ae3&fromSearchBtn=2&compkind=&isAnalysis=&init=-1&searchType=1&dqs=&industryType=&jobKind=&sortFlag=15&degradeFlag=0&industries=&salary=&compscale=&clean_condition=&key=python&headckid=90d24f8653e40ae3&d_pageSize=40&siTag=I-7rQ0e90mv8a37po7dV3Q~fA9rXquZc5IkJpXC-Ycixw&d_headId=bfd5a04b198eb369c0b4b2c7ea83be85&d_ckId=bfd5a04b198eb369c0b4b2c7ea83be85&d_sfrom=search_prime&d_curPage=1&curPage=%s"%(str(page))
		
			self.request_list(url)
			time.sleep(2)
		print("数据写入完成，请查看！\n")

	def request_list(self, page_url):
		try:
			headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
			response = requests.get(page_url, headers = headers)
			#print(response.status_code)
			if response.status_code != 200:
					return
			self.parse_list(response.text)
			
		except Exception as e:
			print("\nerror:\n",e)
	
	def parse_list(self, text):
	
		pass
	
	def request_detail(self, job_href):
		
		try:
			headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
			response = requests.get(job_href, headers = headers)

			if response.status_code != 200:
				return
				
			self.parse_href_detail_list(response.text)
			
		except Exception as e:
			print("\nerror:\n",e)
			
	def parse_href_detail_list(self, text):
		pass
		

#if __name__ == "__main__":
#	bs = Sprider()
#	bs.crawler_data()
