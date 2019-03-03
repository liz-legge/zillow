from lxml import html
import requests
import unicodecsv as csv
import argparse
import datetime
import random
import time
import unicodedata
import json
import base64
import math

user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
    # IE
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
]

proxies_list = [
  'https://1.10.187.158.243:60495',
  'https://36.89.235.50:34670',
  'https://119.82.245.250:45563',
  'https://1.20.97.122:59094',
  'https://85.192.59.22:57493',
  'https://118.174.220.49:42425',
  'https://103.205.26.84:41805',
  'https://36.37.89.99:32323',
  'https://179.124.242.34:41886',
  'https://103.94.0.178:53439',
  'https://93.125.120.1:42099',
  'https://186.250.53.189:45407',
  'https://83.211.86.245:32634',
  'https://91.142.174.224:49260',
  'https://103.42.89.69:53281',
  'https://114.134.186.59:53552',
  'https://37.17.48.12:34180',
  'https://1.179.147.5:39330',
  'https://186.211.110.78:59876',
  'https://187.95.107.230:42257',
    
  


]

lat_lon_ocean = {
  32.851774:-117.26198,
  32.849539:-117.26405,
  32.849138:-117.266255,
  32.84931:-117.268733,
  32.850456:-117.27046,
  32.850514:-117.272484,
  32.851564:-117.273734,
  32.850496:-117.274563,
  32.849918:-117.274904,
  32.849621:-117.275739,
  32.849362:-117.276137,
  32.848666:-117.276253,
  32.848304:-117.276793,
  32.847888:-117.277243,
  32.847651:-117.277737,
  32.847802:-117.278502,
  32.847311:-117.278933,
  32.846868:-117.278881,
  32.846269:-117.278978,
  32.845972:-117.27917,
  32.845729:-117.27883,
  32.845119:-117.278965,
  32.844493:-117.279215,
  32.844093:-117.279929,
  32.843651:-117.28086,
  32.8431:-117.281323,
  32.842366:-117.281548,
  32.841659:-117.281766,
  32.841119:-117.281921,
  32.840412:-117.282203,
  32.839613:-117.282203,
  32.839451:-117.282133,
  32.838819:-117.281869,
  32.838042:-117.281786,
  32.837437:-117.281766,
  32.836838:-117.281753,
  32.836125:-117.281664,
  32.835655:-117.281618,
  32.835034:-117.28161,
  32.834344:-117.281896,
  32.833794:-117.282126,
  32.833112:-117.282256,
  32.832485:-117.282237,
  32.831726:-117.281656,
  32.831191:-117.281435,
}



def parse(read_rows):
	url = "https://www.zillow.com/homes/for_sale/La-Jolla-San-Diego-CA/46087_rid/pricea_sort/0_mmm/1_p/"
	headers= {
					'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
					'accept-encoding':'gzip, deflate, sdch, br',
					'accept-language':'en-GB,en;q=0.8,en-US;q=0.6,ml;q=0.4',
					'cache-control':'max-age=0',
					'upgrade-insecure-requests':'1',
					'user-agent':random.choice(user_agent_list)
	}

	proxy_url=random.choice(proxies_list)
	# proxies_list.pop(proxies_list.index(proxy_url))
	print(proxy_url)
	# response = requests.get(url,headers=headers,proxies={'https': proxy_url})
	while True:
		try:
			response = requests.get(url,headers=headers,proxies={'https': proxy_url})
			break
		except requests.exceptions.ConnectionError:
			proxy_url=random.choice(proxies_list)
	parser = html.fromstring(response.text)
	# print(parser)
	search_results = parser.xpath("//div[@id='search-results']//article")
	# if search_results == []:
	# 	print("retrying")
	# 	time.sleep(10)
	# 	parse(read_rows)
	search_results_pages = parser.xpath("//ol[@class='zsg-pagination']//text()")
	# print("search_results_pages")
	# print(search_results_pages)
	page_max = search_results_pages[-2].strip() if search_results_pages[-1] == 'Next' else search_results_pages[-1]
	print("Total pages: " + str(page_max))
	properties_list = []

	for page in range(1, int(page_max) + 1):
		sleep_intervals = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
		time.sleep(random.choice(sleep_intervals))
  # range(1, int(page_max) + 1):
		# time.sleep(10)
		print("Current page: " + str(page))
		proxy_url=random.choice(proxies_list)
		print(proxy_url)
		# proxies_list.pop(proxies_list.index(proxy_url))

		# if zipcode=="LaJolla":
		url = "https://www.zillow.com/homes/for_sale/La-Jolla-San-Diego-CA/46087_rid/pricea_sort/0_mmm/" + str(page) + "_p/"
		# elif zipcode == "SantaMonica":
		# 	url = "https://www.zillow.com/homes/for_sale/Santa-Monica-CA/26964_rid/pricea_sort/34.069084,-118.404637,33.949839,-118.589173_rect/12_zm/" + str(page) + "_p/"
		# print(url)
		headers= {
					'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
					'accept-encoding':'gzip, deflate, sdch, br',
					'accept-language':'en-GB,en;q=0.8,en-US;q=0.6,ml;q=0.4',
					'cache-control':'max-age=0',
					'upgrade-insecure-requests':'1',
					'user-agent':random.choice(user_agent_list)
		}
		while True:
			try:
				response = requests.get(url,headers=headers,proxies={'https': proxy_url})
				break
			except requests.exceptions.ConnectionError:
				print("caught it!")
				proxy_url=random.choice(proxies_list)
		parser = html.fromstring(response.text)
		search_results = parser.xpath("//div[@id='search-results']//article")
		search_results_pages = parser.xpath("//ol[@class='zsg-pagination']//text()")
		for properties in search_results:
			# time.sleep(240)
			raw_address = properties.xpath(".//span[@itemprop='address']//span[@itemprop='streetAddress']//text()")
			raw_city = properties.xpath(".//span[@itemprop='address']//span[@itemprop='addressLocality']//text()")
			raw_state= properties.xpath(".//span[@itemprop='address']//span[@itemprop='addressRegion']//text()")
			raw_image= properties.xpath(".//img/@src")
			print(raw_image)
			raw_price = properties.xpath(".//span[@class='zsg-photo-card-price']//text()")
			# raw_info = properties.xpath(".//span[@class='zsg-photo-card-info']//text()")
			raw_id = properties.xpath("./@data-zpid")
			# raw_url = properties.xpath(".//a[contains(@class,'overlay-link')]/@href")
			# raw_title = properties.xpath(".//h4//text()")
			# raw_lat= properties.xpath("./@data-latitude")
			# raw_lon= properties.xpath("./@data-longitude")
			# print(raw_address)
      # http://www.zillow.com/webservice/GetDeepSearchResults.htm?zws-id=X1-ZWz1guuolpta17_8w9nb&address=860+Turquoise+St+UNIT+328&citystatezip=San+Diego%2C+CA
			address = '+'.join(' '.join(raw_address).split()) if raw_address else None
			city = '+'.join(' '.join(raw_city).split()) if raw_city else None
			state = ''.join(raw_state).strip() if raw_state else None
			# lat = ''.join(raw_lat) if raw_lat else None
			price = ''.join(raw_price).strip() if raw_price else None
			# image = base64.b64encode(open((''.join(raw_image).strip()), 'rb').read()) if raw_image else None
			# bath = ((raw_info)[2]).split()[0] if len(raw_info) > 1 else None
			# sqft = ((raw_info)[4]).split()[0] if len(raw_info) > 1 else ((raw_info)[0]).split()[0]
			# lon = ''.join(raw_lon) if raw_lon else None
			# title = ''.join(raw_title) if raw_title else None
			property_id = ''.join(raw_id) if raw_id else None      
			# property_url = "https://www.zillow.com"+raw_url[0] if raw_url else None 
			# print(image)
			# print(city)
			if str(property_id) not in read_rows:
				zillow_api = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm?zws-id=X1-ZWz1guuolpta17_8w9nb&address=' + address + '&citystatezip=' + city + '%2C+' + state
				print(zillow_api)
				response = requests.get(zillow_api,headers=headers)
				more_info = html.fromstring(response.content)
				# print(more_info.xpath("/searchResults/response/results/result/yearBuilt"))
				for information in more_info:
					if information.xpath(".//response") != []:    
				# print(information.xpath(".//response//yearbuilt//text()"))
						raw_id = information.xpath(".//response//zpid//text()")				
						raw_url = information.xpath(".//response//homedetails//text()")
						raw_address = information.xpath(".//response//address//street//text()")
						raw_city = information.xpath(".//response//address//city//text()")
						raw_state = information.xpath(".//response//address//state//text()")
						raw_lat = information.xpath(".//response//address//latitude//text()")
						raw_lon = information.xpath(".//response//address//longitude//text()")
						raw_year_built = information.xpath(".//response//yearbuilt//text()")
						raw_use_code = information.xpath(".//response//usecode//text()")
						raw_lotSqFt = information.xpath(".//response//lotsizesqft//text()")
						raw_finishedSqFt = information.xpath(".//response//finishedsqft//text()")
						raw_bathrooms = information.xpath(".//response//bathrooms//text()")
						raw_bedrooms = information.xpath(".//response//bedrooms//text()")
						raw_lastSoldDate = information.xpath(".//response//lastsolddate//text()")
						raw_lastSoldPrice = information.xpath(".//response//lastsoldprice//text()")
						raw_zestimate = information.xpath(".//response//zestimate//amount//text()")
						raw_lastUpdated = information.xpath(".//response//zestimate//last-updated//text()")
						raw_valueChange = information.xpath(".//response//zestimate//valuechange//text()")
						# print(information.xpath(".//response//address//street//text()"))
						property_id = ''.join(raw_id) if raw_id else None   
						property_url = ''.join(raw_url) if raw_url else None 
						address = ' '.join(' '.join(raw_address).split()) if raw_address else None
						city = ' '.join(' '.join(raw_city).split()) if raw_city else None
						state = ' '.join(' '.join(raw_state).split()) if raw_state else None
						lon_before = ''.join(raw_lon) if raw_lon else None
						lat_before = ''.join(raw_lat) if raw_lat else None
						lat = lat_before.split('.')[0] + '.' + lat_before.split('.')[1]
						lon = '-' + lon_before.split('-')[1]
						yearBuilt = ''.join(raw_year_built) if raw_year_built else None
						useCode = ''.join(raw_use_code) if raw_use_code else None
						lotSqft = ''.join(raw_lotSqFt) if raw_lotSqFt else None
						sqft = ''.join(raw_finishedSqFt) if raw_finishedSqFt else None
						bath = ''.join(raw_bathrooms) if raw_bathrooms else None
						beds = ''.join(raw_bedrooms) if raw_bedrooms else None
						lastSoldDate = ''.join(raw_lastSoldDate) if raw_lastSoldDate else None
						lastSoldPrice = ''.join(raw_lastSoldPrice) if raw_lastSoldPrice else None
						zestimate = ''.join(raw_zestimate) if raw_zestimate else None
						lastUpdated = ''.join(raw_lastUpdated) if raw_lastUpdated else None
						valueChange = ''.join(raw_valueChange) if raw_valueChange else None

						googleApi = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=' + lat + ',' + lon + '&destinations=32.845448,-117.275101&units=imperial&key=AIzaSyAD0GuNF-BDlqiGGvAYP4P2551dbrOfzmY'
						# print(googleApi)
						google_Response = requests.get(googleApi,headers=headers)
						# print(google_Response.content)
						formatted = google_Response.json()
						distance_to_gym = None
						duration_to_gym = None
						# print(formatted[2])
						for key1 in formatted:
						# print(formatted[2]["elements"])
							# print(formatted[key1])
							for value1 in formatted[key1]:
								# print(value1)
								for interesting in value1:
									# print(interesting)
									if len(interesting) >= 8:
										for somethingElse in value1[interesting]:
											for whatever in somethingElse:
												for last in somethingElse[whatever]:
													if len(whatever) > 6:
														# print(whatever)
														# print(last)
														# print(somethingElse[whatever][last])
														if ((whatever == "duration") and (last == "text")):
															duration_to_gym = somethingElse[whatever][last]
														if ((whatever == "distance") and (last == "text")):
															distance_to_gym = somethingElse[whatever][last]
												# print(somethingElse[whatever][0])
												# print(somethingElse[whatever]["text"])
										# print(value1[interesting])
						print(distance_to_gym)
						print(duration_to_gym)
						distance_to_ocean = []
						for key, value in lat_lon_ocean.items():
						# lat_test = lat.split('.')[0] + '.' + lat.split('.')[1]
						# lon_test = lon.split('.')[0] + '.' + lon.split('.')[1]
						# print(key)
						# print(value)
							single_dist_to_ocean = 3959 * math.acos(math.sin(math.radians(float(lat))) * math.sin(math.radians(key)) + math.cos(math.radians(float(lat))) * math.cos(math.radians(key)) * math.cos(math.radians(value) - math.radians(float(lon))))
            # 3959 * ACOS( 
            # SIN(RADIANS([Latitude])) * 
            # SIN(RADIANS(32.851774)) + 
            # COS(RADIANS([Latitude])) * 
            # COS(RADIANS(32.851774)) * 
            # COS(RADIANS(-117.26198) - RADIANS([Longitude]))
            # )																				
							distance_to_ocean.append(single_dist_to_ocean)
						properties = {
							'Property Type': useCode,
							'Address':address,
							'City':city,
							'State':state,
							'Price':price,
							'Beds':beds,
              'Bath': bath,
              'House Sqft':sqft,
              'Lot Sqft': lotSqft,
							'Url':property_url,
							'Ocean Distance':min(distance_to_ocean),
              'Gym Distance':distance_to_gym,
              'Gym Duration':duration_to_gym,
              'Lat': lat,
              'Lon': lon,
              'Year Built': yearBuilt,
              'Last Sold Date': lastSoldDate,
              'Last Sold Price': lastSoldPrice,
              'Zestimate': zestimate,
              'Last Updated': lastUpdated,
              'Value Change Last 30 Days': valueChange,
              'Id': property_id,
              'Date Scraped': (unicode(datetime.datetime.now())).split()[0],
						}
						# if is_forsale:
						properties_list.append(properties)
	return properties_list
		# except:
		# 	print ("Failed to process the page",url)

if __name__=="__main__":
	argparser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

	proxies_scraped = []
	url = "https://free-proxy-list.net/"
	response = requests.get(url)
	parser = html.fromstring(response.text)
	search_results = parser.xpath("//tbody")
	for address in search_results:
		for information in address:
			raw_ip = information.xpath(".//td//text()")
			proxies_scraped.append('https://' + raw_ip[0] + ':' + raw_ip[1])
			# print(raw_ip[0])
			# print(raw_ip[1])

	with open("propertiesBuyV2.csv",'ab+')as csvfile:
		fieldnames = ['Property Type', 'Beds', 'Bath', 'House Sqft', 'Lot Sqft', 'Price', 'Address','City','State','Lat', 'Lon', 'Ocean Distance', 'Gym Distance', 'Gym Duration', 'Year Built', 'Last Updated', 'Value Change Last 30 Days', 'Last Sold Date', 'Last Sold Price', 'Zestimate', 'Date Scraped', 'Id', 'Url']
		read_rows = []
		reader = csv.DictReader(csvfile, fieldnames=fieldnames)
		for row in reader:
			read_rows.append(unicodedata.normalize('NFKD', row['Id']).encode('ascii','ignore'))

	# print ("Fetching data for %s"%(zipcode))
	scraped_data = parse(read_rows)
  # , proxies_scraped)
  #  + parse('SantaMonica',sort)
	print ("Writing data to output file")
	date=(unicode(datetime.datetime.now())).split()[0]
	# date_split=date.split()
	# date_formatted=date_split[0]
  #  + '_' + date_split[1]

	with open("propertiesBuyV2.csv",'ab+')as csvfile:
		fieldnames = ['Property Type', 'Beds', 'Bath', 'House Sqft', 'Lot Sqft', 'Price', 'Address','City','State','Lat', 'Lon', 'Ocean Distance', 'Gym Distance', 'Gym Duration', 'Year Built', 'Last Updated', 'Value Change Last 30 Days', 'Last Sold Date', 'Last Sold Price', 'Zestimate', 'Date Scraped', 'Id', 'Url']
		read_rows = []
		reader = csv.DictReader(csvfile, fieldnames=fieldnames)
		for row in reader:
			read_rows.append(unicodedata.normalize('NFKD', row['Id']).encode('ascii','ignore'))
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		if read_rows == []:
			writer.writeheader()
		# print(read_rows)
		for row in scraped_data:
			# print(row['id'])
			if str(row['Id']) not in read_rows:
				writer.writerow(row)