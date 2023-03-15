#Elie Hanna
import requests
import sys
import re

arg_list = sys.argv #list that holds arguments
link = arg_list[1] #string that holds 1st argumeny, the url

r = requests.get(url) 
html = r.text #holds the html of the url

urls = re.findall(r'href=[\'"]?([^\'" >]+)', html) #matches strings that start with 'href=' and puts them all in a list, these strings are the urls

subdomains_output  = open("./output_files/subdomains_output.bat", "a") #file that holds the correct subdomains
directories_output  = open("./output_files/directories_output.bat", "a") #file that holds the correct directories

for url in urls:
    with open('./input_files/dirs_dictionary.bat', 'r') as file: #read dirs_dictionary input file
        for line in file: #iterate over given directories
            full_url2 = url+line
            print(full_url)
            get = requests.get(full_url)
            #if the request succeeds, it means the url is valid
            if get.status_code == 200:
                print("reachable")
                directories_output.write(full_url) #append the url to directories_output file 
        file.close() # Close the file

    with open('./input_files/subdomains_dictionary.bat', 'r') as file2: #read subdomains_dictionary input file
        for line in file2: #iterate over given directories
            parts = re.match(r'(https?://)?([\w\.]+)(.*)', url)
            
            # Insert the subdomain
            full_url2 = f"{parts.group(1) or 'https://'}{subdomain}.{parts.group(2)}{parts.group(3)}"

            print(full_url2)
            get2 = requests.get(full_url2)
            #if the request succeeds, it means the url is valid
            if get2.status_code == 200:
                subdomains_output.write(full_url2) #append the url to subdomains_output file 
        file2.close() # Close the file


