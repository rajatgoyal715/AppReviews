import bs4 as bs
import urllib.request

input = input("\nEnter the name of the app you want reviews of : ");
#input = 'Whatsapp'

play = 'https://play.google.com/store/search?q=' + input + "&c=apps"

source = urllib.request.urlopen(play).read()
soup1 = bs.BeautifulSoup(source, 'html5lib')

url = 'https://play.google.com' + soup1.find('a', class_='card-click-target').get('href')
print("\n" + url)

app_source = urllib.request.urlopen(url).read()
soup2 = bs.BeautifulSoup(app_source, 'html5lib')

title = soup2.find('div', class_='id-app-title').text
print('\n' + title + '\n')

count = 1

for div in soup2.find_all('div', class_='review-body with-review-wrapper'):
	
	review = div.text.encode('ascii', 'ignore').decode('ascii')
	review = review.replace("Full Review", " ")
	print(str(count) + '.' + review)
	
	print('\n' + '-'*100 + '\n')
	
	count = count + 1