import requests
import couchdb
from bs4 import BeautifulSoup
from flipkart import getSoup
from utils import stripHtml

#get the html source of the given url 
def get_html_source(url):
	r = requests.get(url)
	return r.text


# for each_merge_item in merge_item:
# 	# each_merge_item = merge_item[0]
# 	# each_merge_item

# 	each_merge_item.find('td',attrs = {'class':'item_date'})
# 	each_merge_item.find('td',attrs = {'class':'item_date'}).renderContents()



# print a['author_name']
# print a['date']

	# each_merge_item.find('a',attrs={'href':'/review/r150730a.htm'})
	each_merge_item.h4.a['href']

	#print all the information - Date, Authorname, Content
	print a


def getReviewData(each_merge_item):
	a = {}
	a['date'] = stripHtml(each_merge_item.find('td',attrs = {'class':'item_date'}).renderContents())
	# a['author_name'] = stripHtml(each_merge_item.find('a',attrs = {'class':'author_link'}).renderContents())
	a['content'] = stripHtml(each_merge_item.find('p').renderContents())

	#For some pages author name not found : Exception Cases : Try and except block : 
	try:
		a['author_name'] = stripHtml(each_merge_item.find('a',attrs = {'class':'author_link'}).renderContents())
	except:
		a['author_name'] = 'Author name not found'
	print a
	
#Result contains the list of dictionaries 
def getReviewsForSinglePage(soup):
	result = []
	reviews = soup.findAll('tr',attrs = {'class':'item even'})
	print len(reviews)
	for review in reviews:
		try:
			t = getReviewData(each_merge_item)
			result.append(t)
		except:
			pass
	return result


def get_content_from_single_page(soup):
	"""
	Get the soup object of the given url to identify the metadata of the speech
	"""
	#get the soup object of the given url 
	# url="https://www.bis.org/list/cbspeeches/index.htm?m=2|10"
	#soup = getSoup(url)
	item_date_even = soup.findAll('tr',attrs = {'class':'item even'})
	item_date_odd = soup.findAll('tr',attrs = {'class':'item odd'})
	merge_item = item_date_even + item_date_odd

	for each_merge_item in merge_item: 
	 	getReviewData(each_merge_item)

#main function
if __name__ == "__main__":
	url = 'https://www.bis.org/list/cbspeeches/page_1.htm'
	while True:
		print "\n" *4
		print "*" * 80
		soup = getSoup(url)
		get_content_from_single_page(soup)
		try:
				# each_merge_item.find('a',attrs={'href':'/review/r150730a.htm'})
			next_page = 'https://www.bis.org'+soup.find('a',attrs = {'class':'next'})['href']
			# print next_page
			url = next_page
		except:
			print "fetched all pages"
			break



# print merge_item
# print merge_item[0]

# #main function 
# if __name__ == "__main__":	
# 	url = "https://www.bis.org/list/cbspeeches/index.htm?m=2|10"
# 	while True:		
# 		try:
# 			soup = getSoup(url)
# 			my_results = getReviewsForSinglePage(soup)	
# 			save(my_results)
# 			#next_page = soup.find('a',attrs = {'class':'nav_bar_next_prev'})
# 			next_page = soup.find('big',text=u'\u203a').findParent('a')
# 			url = 'https://www.bis.org/list/cbspeeches/index.htm?m=2|10' + next_page['href']
# 			print "Next page is %s"%url
# 		except:
# 			# print traceback.print_exc()
# 			print 'Fetched all pages'
# 			print 'stopped'
# 			break
