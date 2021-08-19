## This code check the HTTP header

import urllib

url1 = input("Enter the URL ") 
http_r = urllib.urlopen(url1)
 
if http_r.code == 200:
    print( http_r.headers)