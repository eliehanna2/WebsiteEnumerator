#Elie Hanna
import requests
import sys
import re

arg_list = sys.argv #list that holds arguments
url = arg_list[1] #string that holds 1st argumeny, the url

r = requests.get(url) 
html = r.text #holds the html of the url

subdomains_output  = open("./output_files/subdomains_output.bat", "a") #file that holds the subdomains
directories_output  = open("./output_files/directories_output.bat", "a") #file that holds the directories
files_output  = open("./output_files/files_output.bat", "a") #file that holds the files

files = re.findall(r'href=[\'"]?([^\'" >]+)', html) #matches strings that start with 'href=' and puts them all in a list, these strings are the urls
for file in files:
     files_output.write(file) #append the file name to files_output file

with open('./input_files/dirs_dictionary.bat', 'r') as file: #read dirs_dictionary input file
        for line in file: #iterate over given directories
            full_url = url+line

            #print(full_url) #for testing

            get = requests.get(full_url)
            #if the request succeeds, it means the url is valid
            if get.status_code in range(200,299):
                print("reachable")
                directories_output.write(full_url) #append the url to directories_output file 
file.close() # Close the file

with open('./input_files/subdomains_dictionary.bat', 'r') as file2: #read subdomains_dictionary input file
    for line in file2: #iterate over given subdomains
        parts = re.match(r'(https?://)?([\w\.]+)(.*)', url)
        
        # Insert the subdomain using regex
        full_url2 = f"{parts.group(1) or 'https://'}{line}.{parts.group(2)}{parts.group(3)}"

        #print(full_url2) #for testing

        get2 = requests.get(full_url2)
        #if the request succeeds, it means the url is valid
        if get2.status_code in range(200,299):
            subdomains_output.write(full_url2) #append the url to subdomains_output file 
file2.close() # Close the file

files_output.close()
directories_output.close()
subdomains_output.close()