# ScriptingProject2
<h1>Ethical Hacking Project</h1>
<h2>By Elie Hanna</h2>
![image](istockphoto-1297795284-170667a.jpg)

<h2>Project</h2>
I wrote a Python script that takes a URL as its first argument and performs some operations on it. The script uses the requests library to retrieve the HTML content of the URL and then uses regular expressions to extract various information from it. Specifically, the script extracts all of the URLs contained in the HTML and writes them to a file called files_output.bat. Additionally, the script reads two input files called dirs_dictionary.bat and subdomains_dictionary.bat that contain lists of directories and subdomains to try, respectively. For each directory and subdomain, the script constructs a full URL by appending it to the original URL and then sends a GET request to that URL. If the request succeeds (i.e., returns a status code between 200 and 299), the script writes the URL to either directories_output.bat or subdomains_output.bat, depending on whether it was a directory or subdomain that was tried.

<h2>BONUS</h2>
In the bonus part, I added some code that performs a login attempt on a website. The code sends a GET request to the login page to get the cookies, extracts the post URL and CSRF token from the login page using regular expressions, and then tries a list of passwords to see if any of them are correct. If a correct password is found, the script prints a message saying that the login was successful and which password was used. Otherwise, it prints a message saying that the login failed with the current password.
