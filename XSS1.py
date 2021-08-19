import mechanize
import re
import shelve

br = mechanize.Browser()
br.set_handle_robots( False )
url = raw_input("Enter URL ")
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_referer(True) 
br.set_handle_robots(False)
br.open(url) 

s = shelve.open("mohit.xss",writeback=True)
for form in br.forms():
    print(form)

att = input("Enter the attack field ")
non = input("Enter the normal field ")
br.select_form(nr=0)

p =0 
flag = 'y'

while flag =="y":
    br.open(url)
	br.select_form(nr=0)
	br.form[non] = 'aaaaaaa'
	br.form[att] = s['xss'][p]
	print(s['xss'][p])
	br.submit()
	ch = input("Do you continue press y ")
	p = p+1
	flag = ch.lower()
