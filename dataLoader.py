from bs4 import BeautifulSoup
import requests
import datetime
import re
import csv
# from tkinter import *
# from tkinter import messagebox

csv_file = open('purchaseData.csv','w', newline='')
csv_writer = csv.writer(csv_file, delimiter=',')
csv_writer.writerow(['link','price', 'address','numRooms','dateListed'])

for pageNo in range(50):
	source = requests.get('https://www.zoopla.co.uk/for-sale/property/london/?identifier=london&q=London&radius=0&pn='+str(pageNo)).text
	print('now processeing purchase data page',pageNo+1)
	soup = BeautifulSoup(source, 'lxml')



	for wrapper in soup.find_all('div', class_="listing-results-wrapper"):
		# print(wrapper.prettify())

		link1 = wrapper.find('a',class_='photo-hover')['href']
		link = 'https://www.zoopla.co.uk'+link1
		 

		monthlyPrice5 = wrapper.find('a',class_="listing-results-price text-price").text
		monthlyPrice4 = monthlyPrice5.replace('\n','')
		monthlyPrice3 = monthlyPrice4.replace(',','')
		monthlyPrice2 = monthlyPrice3.replace('£','')
		monthlyPrice1 = monthlyPrice2.split(' ')
		for i in monthlyPrice1:
			try:
				int(i)
				break
			except:
				if i =='POA':
					i = 'NaaN'
					break
				else:
					continue

		monthlyPrice = i
		 
		address1 = wrapper.find('a',class_="listing-results-address").text
		address = address1.replace(',','')

		try:
			roomNum = wrapper.find('span',class_="num-icon num-beds").text
		except Exception:
			roomNum = 0	
		 

		listedDate8 = wrapper.find('p',class_="top-half listing-results-marketed").text
		listedDate7 = listedDate8.split('on')[1]
		listedDate6 = listedDate7.split('\n')[1]
		try:
			listedDate5 = listedDate6.split(' ')[0]
			listedDate4 = listedDate5[1::-1]
			listedDate3 = listedDate4[::-1]
			listedDate2 = listedDate6[5:]
			listedDate1 = (listedDate3 + ' ' + listedDate2)
			listedDate0 = datetime.datetime.strptime(listedDate1, "%j %b %Y" )
		except: 
			listedDate5 = listedDate6.split(' ')[1]	
			listedDate4 = listedDate5[1::-1]
			listedDate3 = listedDate4[::-2]
			listedDate2 = listedDate6[5:]
			listedDate1 = (listedDate3 + ' ' + listedDate2)
			listedDate0 = datetime.datetime.strptime(listedDate1, "%j %b %Y")
		listedDate = listedDate0.date()


		csv_writer.writerow([link, monthlyPrice, address, roomNum, listedDate])
		
csv_file.close()

csv_file = open('rentalData.csv','w', newline='')
csv_writer = csv.writer(csv_file, delimiter=',')
csv_writer.writerow(['link','pricePerMonth', 'address','numRooms','dateListed'])

for pageNo in range(50):
	source = requests.get('https://www.zoopla.co.uk/to-rent/property/london/?identifier=london&q=london&search_source=refine&radius=1&price_frequency=per_month&pn='+str(pageNo)).text
	print('now processeing rental data page',pageNo+1)
	soup = BeautifulSoup(source, 'lxml')

	for wrapper in soup.find_all('div', class_="listing-results-wrapper"):
		# print(wrapper.prettify())

		link1 = wrapper.find('a',class_='photo-hover')['href']
		link = 'https://www.zoopla.co.uk'+link1
		 
		
		monthlyPrice5 = wrapper.find('a',class_="listing-results-price text-price").text
		monthlyPrice4 = monthlyPrice5.replace('\n','')
		monthlyPrice3 = monthlyPrice4.replace(',','')
		monthlyPrice2 = monthlyPrice3.replace('£','')
		monthlyPrice1 = monthlyPrice2.split(' ')
		for i in monthlyPrice1:
			try:
				int(i)
				break
			except:
				if i =='POA':
					i = 'NaaN'
					break
				else:
					continue

		monthlyPrice = i		 

		address1 = wrapper.find('a',class_="listing-results-address").text
		address = address1.replace(',','')
	
		try:
			roomNum = wrapper.find('span',class_="num-icon num-beds").text
		except Exception:
			roomNum = 0	
		 

		listedDate8 = wrapper.find('p',class_="top-half listing-results-marketed").text
		listedDate7 = listedDate8.split('on')[1]
		listedDate6 = listedDate7.split('\n')[1]
		try:
			listedDate5 = listedDate6.split(' ')[0]
			listedDate4 = listedDate5[1::-1]
			listedDate3 = listedDate4[::-1]
			listedDate2 = listedDate6[5:]
			listedDate1 = (listedDate3 + ' ' + listedDate2)
			listedDate0 = datetime.datetime.strptime(listedDate1, "%j %b %Y" )
		except: 
			listedDate5 = listedDate6.split(' ')[1]	
			listedDate4 = listedDate5[1::-1]
			listedDate3 = listedDate4[::-2]
			listedDate2 = listedDate6[5:]
			listedDate1 = (listedDate3 + ' ' + listedDate2)
			listedDate0 = datetime.datetime.strptime(listedDate1, "%j %b %Y" )
			listedDate = listedDate0.date()
		

		csv_writer.writerow([link, monthlyPrice1, address, roomNum, listedDate])
		
csv_file.close()

print("your scraping process has completed")

# window = Tk()
# window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
# window.withdraw()

# messagebox.showinfo('Suprise', 'Data has been updated')

# window.deiconify()
# window.destroy()
# window.quit()