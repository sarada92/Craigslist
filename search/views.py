import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus
from . import models


# Create your views here.

BASE_CRAIGSLIST_URL = 'https://www.flipkart.com/search?q={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'

def home(request):
    return render(request, 'base.html')

def new_search(request): 
    if request.method == 'POST':
        searchWord = request.POST.get('searchword')
        # searchWord = 'tv'
        final_url = BASE_CRAIGSLIST_URL.format(quote_plus(searchWord))
        response = requests.get(final_url)
        print(final_url)
        data = response.text
        soup = BeautifulSoup(data, features='html.parser')
        post_listing = soup.find_all('div', {'class':'_2kHMtA'})

        final_output = []

        for post in post_listing:
            title = post.find_all('div', {'class': '_4rR01T'})[0].text
            imglink = post.find_all('img', {'class': '_396cs4 _3exPp9'})[0].get('src')
            link = 'www.flipkart.com' + post.find_all('a', {'class': '_1fQZEK'})[0].get('href')
            price = post.find_all('div', {'class': '_30jeq3 _1_WHN1'})[0].text
            final_output.append({'title': title, 'img': imglink, 'price': price, 'link': link})

        content = {'search': searchWord, 'postings': final_output}

    return render(request, 'main/search.html', content)                

