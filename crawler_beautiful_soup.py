from bs4 import BeautifulSoup
import urllib2


instagram_username = "" #for example david beckham
response = urllib2.urlopen("https://www.instagram.com/"+instagram_username+"/").read()
f=open("index.html","wb")
f.write(response) 
soup=BeautifulSoup(open("index.html"),'lxml')
count=0
for i in soup.find_all("script",limit=7):
	count+=1
	if(count==7):
		i=i.string
	



value = '{%s}' % (i.split('{', 1)[1].rsplit('}', 1)[0],)
templist=[]

found = False
for j in value.split():
	if found:
		
		templist.append(j)
		found = False
	if(j=='{"count":' or j=='{"username":'):
		found=True


q,r=templist[0].split(',')
a,b,c=q.split('"')
print "Username: ", b

q,r=templist[1].split('}')
print "Follows ",q, " people"

q,r=templist[2].split('}')
print "Followed by ",q, " people"





