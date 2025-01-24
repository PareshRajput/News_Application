import requests
from django.shortcuts import render

def index(request):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': 'India',  # Search query (everything endpoint does not support country filtering)
        'apiKey': 'e18c2688af7b4ebfab8bec4c7038fb8a',
        'pageSize': 20  # Limit the number of results
    }
    response = requests.get(url, params=params)
    
    # Check if the response is valid
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles', [])
    else:
        articles = []  # Fallback to an empty list if the API fails
    
    return render(request, 'news/index.html', {'articles': articles})
