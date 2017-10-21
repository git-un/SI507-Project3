import requests
from bs4 import BeautifulSoup
##importing class definition
"""
students = [("Jones, Jamal J", 98, "A+"),
            ("Ensted, Eloise E", 87, "B+"),
            ("Morton, Madeline", 99, "A+")]

outfile = open("grades.csv","w")
# output the header row
outfile.write('"Name", "score", "grade"\n')
# output each of the rows:
for student in students:
    #print (student[2])
    outfile.write('"{}", "{}", "{}"\n'.format(student[0],student[0],student[0]))
outfile.close()

for a,b,c in students:
    #print(c)
    pass


try:
  catData = open("gallery.html",'r').read()
except:
  catData = requests.get("http://newmantaylor.com/gallery.html").text
  f = open("gallery.html",'w')
  f.write(catData)
  f.close()
# ursulav_data should be a big string of HTML data

#print (ursulav_data)
catSoup = BeautifulSoup(catData, 'html.parser')
catImgList = catSoup.find_all("img")
j=0
for i in catImgList:
    j+=1
    print j
    print(i.get('alt',"no alt text"))

    #################################
    * Access and cache data, starting from `https://www.nps.gov/index.htm`.
    You will ultimately need the HTML data from all the parks from Arkansas, California, and Michigan.
    So, you should save on your computer data from the following pages, in files with the following
    names:

    	* [Main page data](https://www.nps.gov/index.htm),
         `https://www.nps.gov/index.htm`, in a file `nps_gov_data.html`

    	* [Arkansas](https://www.nps.gov/state/ar/index.htm),
         `https://www.nps.gov/state/ar/index.htm`, in a file `arkansas_data.html`

    	* [California](https://www.nps.gov/state/ca/index.htm),
         `https://www.nps.gov/state/ca/index.htm`, in a file `california_data.html`

    	* [Michigan](https://www.nps.gov/state/mi/index.htm),
         `https://www.nps.gov/state/mi/index.htm`, in a file `michigan_data.html`
"""

michData = open("sample_html_of_park.html",'r').read()



michSoup = BeautifulSoup(michData, 'html.parser')
liList = michSoup.find_all("li")
for i in liList:
    h2 = liList.find("h2")
print(h2)
