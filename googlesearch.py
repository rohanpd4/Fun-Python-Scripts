import requests
from bs4 import BeautifulSoup
import webbrowser


item = input('Google search:')

r=requests.get("https://www.google.com/search?q="+"".join(item))
res=r.text
res1 = BeautifulSoup(res, 'html.parser')
links=res1.select('.r a');
webbrowser.open_new_tab("https://www.google.com/search?q="+item)
for i in links:
    #print("https://www.google.com/"+i.get('href'))
    webbrowser.open_new_tab("https://www.google.com/"+i.get('href'))