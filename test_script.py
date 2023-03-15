#Elie Hanna
import requests
import sys
import re

arg_list = sys.argv #list that holds arguments
url = arg_list[1] #string that holds 1st argumeny, the url

r = requests.get(url) 
html = r.text #holds the html of the url

urls = re.findall(r'href=[\'"]?([^\'" >]+)', html) #matches strings that start with 'href=' and puts them all in a list, these strings are the urls