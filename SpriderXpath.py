from lxml import etree
from Sprider import Sprider
from ExcelCreate import ExcelCreate
import time

class SpriderXpath(Sprider):
	def __init__(self):
		super().__init__()
	
	def parse_list(self, text):
		try:
			html = etree.HTML(text)
			contents = html.xpath('//div[@class="sojob-item-main clearfix"]')
			for content in contents:
				title = content.xpath('./div[@class="job-info"]/h3/a/text()')
				salary = content.xpath('./div[@class="job-info"]/p/span/text()')
				addr = content.xpath('./div[@class="job-info"]/p/a/text()')
				edu = content.xpath('./div[@class="job-info"]/p/span[2]/text()')
				work = content.xpath('./div[@class="job-info"]/p/span[3]/text()')
				href = content.xpath('./div[@class="job-info"]/h3/a/@href')
				company = content.xpath('./div[@class="company-info nohover"]/p/a/text()')
				field = content.xpath('./div[@class="company-info nohover"]/p[2]/span/a/text()')
				
				self.job_info.append(title[0].strip())
				self.job_info.append(salary[0])
				self.job_info.append(addr[0])
				self.job_info.append(edu[0])
				self.job_info.append(work[0])
				self.job_info.append(company[0])
				self.job_info.append(field[0])
				self.job_info.append(href[0])
				
				self.request_detail(href[0])
				time.sleep(1)
		except Exception as e:
			print("error:%s"%e)
			
	def parse_href_detail_list(self, text):
		try:
			try:
				html = etree.HTML(text)
				detail = html.xpath('//div[@class="content content-word"]')
				detail = detail[0].xpath('string(.)').strip().split('\n')[0]
			except Exception as e:
				print("error:%s"%e)
				detail = "no data"
			self.job_info.append(detail)
			#print(detail)
			self.count = self.count + 1
			print("写入数据中，第%d条数据"%self.count)
			ExcelCreate.write_excel(self.excel_book, self.excel_sheet, self.count, self.job_info, "job_xpath.xls")
			self.job_info = []
		except Exception as e:
			print("error:%s"%e)
		
#if __name__ == "__main__":
#	x = SpriderXpath()
#	x.crawler_data()



	





