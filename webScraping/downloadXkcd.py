## Downloads every single XKCD comic

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    if (imgElem := soup.select('#comic img')) == []:
        print('Could not find image.')
    else:
        try:
            imgUrl = 'http' + imgElem[0].get('src')
            print('Downloading image %s...' % (imgUrl))
            res = requests.get(imgUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue
        imageFile = open(os.path.join('xkcd', os.path.basename(imgUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
    
print('Done')