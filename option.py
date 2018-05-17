#! usr/bin/env python2
import webbrowser
import time

menu='''
Press 1 for google search
Press 2 to get the URLs
Press 3 for googe  images
'''
print menu
ch=raw_input("Enter your option")

if(ch=='1'):
	get_data=raw_input('Enter anything')
	final_data=get_data.strip().split()
	print final_data
	for i in final_data:
		webbrowser.open_new_tab("https://www.google.com/search?q="+i)
if(ch=='3'):
        get_data=raw_input('Enter anything')
        final_data=get_data.strip().split()
        print final_data
        for i in final_data:
                webbrowser.open_new_tab("https://www.images.google.com/search?q="+i)
