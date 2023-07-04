#Create a program that allows you to search for images in gif format. 
#The program should allow you to enter a search word. Using this word, 
#search for GIFs using the Giphy API. As a result, print the links to the GIFs.


import requests
#import json

word = input('Please enter a search word: ')
response = requests.get(f'https://api.giphy.com/v1/gifs/search?api_key=ANB5AMDXev554QvgeD0GA6NKq20N3J3e&q={word}&limit=1&offset=0&rating=g&lang=en&bundle=messaging_non_clips')
d = response.json()
gif = d['data'][0]['url']
print(gif)
