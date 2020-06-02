#Library to get datetime in python
from datetime import datetime as dt
import time



#Path of host files in windows directroies
host_path = r"C:\Windows\System32\drivers\etc\hosts"

#Path where redirect when open sites
redirect_path = "127.0.0.1"


#Lists of websites

website_links = ['www.facebook.com','facebook.com','www.bing.com','bing.com','www.twitter.com','twitter.com','www.udemy.com','udemy.com']

#Infinte Loop 


while True:
#Condition to check if the time is between 8PM to 4AM
    if dt(dt.now().year,dt.now().month,dt.now().day,6) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23):
       with open('hosts',"r+") as file:
           content = file.read()
           for i in website_links:
               print('Working Hours')
               if i not in content:
                   file.write(f"{redirect_path} {i} \n")
               else:
                    pass
    else:
        with open('hosts' , "a") as file:
            content = file.readlines()
            #to return point to the top
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_links):
                    file.write(f"{line}")
                    #To delete lines after this
            file.truncate()
    print('Fun Hours')
    time.sleep(2)
