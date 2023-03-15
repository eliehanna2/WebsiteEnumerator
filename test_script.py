#Elie Hanna
import requests
import sys

arg_list = sys.argv #list that holds arguments
url = arg_list[1] #string that holds 1st argumeny, the url
r = requests.get(url) 
html = r.text #holds the html of the url