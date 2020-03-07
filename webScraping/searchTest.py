

import requests, sys, webbrowser, bs4

print('Searching...')
res = requests.get('https://nootropicsdepot.com/search.php?search_query=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

linkElems = soup.select('.card-title a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open(linkElems[i].get('href'))
