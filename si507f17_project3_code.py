from bs4 import BeautifulSoup
import unittest
import requests

#########
## Instr note: the outline comments will stay as suggestions, otherwise it's too difficult.
## Of course, it could be structured in an easier/neater way, and if a student decides to commit to that, that is OK.

## NOTE OF ADVICE:
## When you go to make your GitHub milestones, think pretty seriously about all the different parts and their requirements, and what you need to understand.
##Make sure you've asked your questions about Part 2 as much as you need to before Fall Break!


######### PART 0 #########

# Write your code for Part 0 here.

try:
  catData = open("gallery.html",'r').read()
except:
  catData = requests.get("http://newmantaylor.com/gallery.html").text
  f = open("gallery.html",'w')
  f.write(catData)
  f.close()

def catSoup():
	catSoup = BeautifulSoup(catData, 'html.parser')
	catImgList = catSoup.find_all("img")
	j=0
	for i in catImgList:
		j+=1
		print (j)
		print(i.get('alt',"no alt text"))

######### PART 1 #########

# Get the main page data...

# Try to get and cache main page data if not yet cached
# Result of a following try/except block should be that
# there exists a file nps_gov_data.html,
# and the html text saved in it is stored in a variable
# that the rest of the program can access.

# We've provided comments to guide you through the complex try/except,
#but if you prefer to build up the code to do this scraping and caching yourself, that is OK.


# Get individual states' data...

# Result of a following try/except block should be that
# there exist 3 files -- arkansas_data.html, california_data.html, michigan_data.html
# and the HTML-formatted text stored in each one is available
# in a variable or data structure
# that the rest of the program can access.

# TRY:
# To open and read all 3 of the files

# But if you can't, EXCEPT:

# Create a BeautifulSoup instance of main page data
# Access the unordered list with the states' dropdown

# Get a list of all the li (list elements) from the unordered list, using the BeautifulSoup find_all method

# Use a list comprehension or accumulation to get all of the 'href'
#attributes of the 'a' tag objects in each li, instead of the full li objects

# Filter the list of relative URLs you just got to include only the 3 you want:
#AR's, CA's, MI's, using the accumulator pattern & conditional statements


# Create 3 URLs to access data from by appending those 3 href values to the
#main part of the NPS url. Save each URL in a variable.


## To figure out what URLs you want to get data from (as if you weren't told initially)...
# As seen if you debug on the actual site. e.g. Maine parks URL is
#"http://www.nps.gov/state/me/index.htm", Michigan's is "http://www.nps.gov/state/mi/index.htm"
#-- so if you compare that to the values in those href attributes you just got... how can you build the full URLs?


# Finally, get the HTML data from each of these URLs, and save it in the variables you used in the try clause
# (Make sure they're the same variables you used in the try clause!
#Otherwise, all this code will run every time you run the program!)


# And then, write each set of data to a file so this won't have to run again.


# try:
#	 npsData = open("nps_gov_data.html",'r').read()
# except:
#	 npsData = requests.get("https://www.nps.gov/index.htm").text
#	 f = open("nps_gov_data.html",'w')
#	 f.write(npsData)
#	 f.close()

# indexData = BeautifulSoup(npsData, 'html.parser')
# states = indexData.select('.dropdown-menu li')
# # print(states[3].a['href'])

# for x in states:
#	 name = x.a.contents[0]
#	 if(name == 'Michigan'):
#		 miUrl = x.a['href']
#		 print(miUrl)
#	 if(name == 'California'):
#		 caUrl = x.a['href']
#		 print(caUrl)
#	 if(name == 'Arkansas'):
#		 akUrl = x.a['href']
#		 print(akUrl)


try:
	npsData = open("nps_gov_data.html",'r').read()
except:
	npsData = requests.get("https://www.nps.gov/index.htm").text
	f = open("nps_gov_data.html",'w')
	f.write(npsData)
	f.close()

indexData = BeautifulSoup(npsData, 'html.parser')
states = indexData.select('.dropdown-menu li')
# print(states[3].a['href'])

for x in states:
	 name = x.a.contents[0]
	 if(name == 'Michigan'):
		 miUrl = 'https://www.nps.gov' + x.a['href']
		 print(miUrl)
	 if(name == 'California'):
		 caUrl = 'https://www.nps.gov' + x.a['href']
		 print(caUrl)
	 if(name == 'Arkansas'):
		 akUrl = 'https://www.nps.gov' + x.a['href']
		 print(akUrl)

try:
	arkData = open("arkansas_data.html",'r').read()
except:
	arkData = requests.get(akUrl).text
	f = open("arkansas_data.html",'w')
	f.write(arkData)
	f.close()
try:
	calData = open("california_data.html",'r').read()
except:
	calData = requests.get(caUrl).text
	f = open("california_data.html",'w')
	f.write(calData)
	f.close()

try:
	michData = open("michigan_data.html",'r').read()
except:
	michData = requests.get(miUrl).text
	f = open("michigan_data.html",'w')
	f.write(michData)
	f.close()



npsSoup = BeautifulSoup (npsData, 'html.parser')
npsLinkList = npsSoup.find_all("a")

j=0
l = []
for link in npsLinkList:
	j+=1
	#print (j)
	#print(link.get('href',"no href link"))
	l.append(link.get('href',"no href link"))
	#98 links with href
	#print (l[0])






######### PART 2 #########

## Before truly embarking on Part 2, we recommend you do a few things:

# - Create BeautifulSoup objects out of all the data you have access to in variables from Part 1
# - Do some investigation on those BeautifulSoup objects. What data do you have about each state?
# How is it organized in HTML?

# HINT: remember the method .prettify() on a BeautifulSoup object --
#might be useful for your investigation! So, of course, might be .find or .find_all, etc...
# prettify | find | find_all

# HINT: Remember that the data you saved is data that includes ALL of the parks/sites/etc
#in a certain state, but you want the class to represent just ONE park/site/monument/lakeshore.

# We have provided, in sample_html_of_park.html an HTML file that represents the HTML about 1 park.
#However, your code should rely upon HTML data about Michigan, Arkansas, and California you saved
#and accessed in Part 1.

# However, to begin your investigation and begin to plan your class definition,
#you may want to open this file and create a BeautifulSoup instance of it to do investigation on.

# Remember that there are things you'll have to be careful about listed in the instructions
#-- e.g. if no type of park/site/monument is listed in input, one of your instance variables
# should have a None value...





## Define your class NationalSite here:

class NationalSite():
	pass

	def __init__(self, soupObject):
		self.location = soupObject.h4.text
		self.name = soupObject.h3.text
		self.soupObject = soupObject
		try:
			self.type = soupObject.h2.text
		except:
			self.type = None
		self.description = soupObject.p.text

	# def getAddress(self, soupObject):
	#	 href = soupObject.select('.stateListLinks ul li a')[1]['href']
	#	 addressPage = requests.get(href).text
	#	 addressPage = BeautifulSoup (addressPage, 'html.parser')
	#	 address = addressPage.select('.physical-address > *')
	#	 addressText = ''

	#	 for tag in address:
	#		 if tag.text != '':
	#			 addressText += tag.text

	#	 addressText = addressText.replace('\n',' ').strip()


	#	 print(addressText)
		
	#	 return href


	def __str__(self):
		return("{} | {}".format(self.name, self.location))

	def get_mailing_address(self):
		hrefs = self.soupObject.select('.stateListLinks ul li a')
		href = ''
		for link in hrefs:
			if 'basic information' in link.text.lower():
				href = link['href']
				break

		addressPage = requests.get(href).text
		addressPage = BeautifulSoup(addressPage, 'html.parser')
		address = addressPage.select('.physical-address > *')
		addressText = ''

		for tag in address:
			if tag.text != '':
				addressText += tag.text

		addressText = addressText.replace('\n',' ').strip()

		return addressText


	# def __repr__(self):
	#	 return("ITUNES MEDIA: {}".format(self.itunes_id))

	# def __len__(self):
	#	 return 0

	def __contains__(self, str):
		title = self.name.lower()
		str = str.lower()
		x = str in title
		return x


## Recommendation: to test the class, at various points, uncomment the following code and invoke some of the methods / check out the instance variables of the test instance saved in the variable sample_inst:

# f = open("sample_html_of_park.html",'r')
# soup_park_inst = BeautifulSoup(f.read(), 'html.parser') # an example of 1 BeautifulSoup instance to pass into your class
# sample_inst = NationalSite(soup_park_inst)
# f.close()


######### PART 3 #########

# Create lists of NationalSite objects for each state's parks.

# HINT: Get a Python list of all the HTML BeautifulSoup instances that represent each park, for each state.


california_soup = BeautifulSoup(calData, 'html.parser').select('#list_parks > li')
arkansas_soup = BeautifulSoup(arkData, 'html.parser').select('#list_parks > li')
michigan_soup = BeautifulSoup(michData, 'html.parser').select('#list_parks > li')

california_natl_sites = []
arkansas_natl_sites = []
michigan_natl_sites = []

#Code to help you test these out:

#california_soup = california_soup[2:5]

def clean_string(string):
	return string.replace(',',' ').replace('\n', ' ').strip()

californiaFile = open("california.csv","w")
californiaFile.write("Name, Location, Type, Address, Description\n")
for p in california_soup:
	site = NationalSite(p)
	california_natl_sites.append(site)
	californiaFile.write("{}, {}, {}, {}, {}\n".format(clean_string(site.name), clean_string(site.location), clean_string(site.type) if site.type != None else 'None', clean_string(site.get_mailing_address()), clean_string(site.description)))
californiaFile.close()

arkansasFile = open("arkansas.csv","w")
arkansasFile.write("Name, Location, Type, Address, Description\n")
for a in arkansas_soup:
	site = NationalSite(a)
	arkansas_natl_sites.append(site)
	arkansasFile.write("{}, {}, {}, {}, {}\n".format(clean_string(site.name), clean_string(site.location), clean_string(site.type) if site.type != None else 'None', clean_string(site.get_mailing_address()), clean_string(site.description)))
	print
arkansasFile.close()

michiganFile = open("michigan.csv","w")
michiganFile.write("Name, Location, Type, Address, Description\n")
for m in michigan_soup:
	site = NationalSite(m)
	michigan_natl_sites.append(site)
	michiganFile.write("{}, {}, {}, {}, {}\n".format(clean_string(site.name), clean_string(site.location), clean_string(site.type) if site.type != None else 'None', clean_string(site.get_mailing_address()), clean_string(site.description)))
michiganFile.close()



######### PART 4 #########

## Remember the hints / things you learned from Project 2 about writing CSV files from lists of objects!

## Note that running this step for ALL your data make take a minute or few to run -- so it's a good idea to test any methods/functions you write with just a little bit of data, so running the program will take less time!

## Also remember that IF you have None values that may occur, you might run into some problems and have to debug for where you need to put in some None value / error handling!








