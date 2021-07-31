import pandas as pd
import csv
arr=[]
# with open('Input\CONFIG_FACEBOOK_SCRAPE_SOURCE.csv', 'r') as File:  
#     read = csv.reader(File)
#     for row in read:
#         arr.append(row)
# print(arr[2][1])
# # print(arr[0])
# print(arr[1][2]=='All')
# print(arr[2][2]=="IMAGES")

# we have to pass one massage query at a time
# massag=[]
# post =[]
# with open('Input\CONFIG_FACEBOOK_DATAMASSAGING.CSV', 'r') as File:  
#     readr = csv.reader(File)
#     for row in readr:
#         massag.append(row)
# # print(massag)
# for i in range(1,len(massag)):
#     if massag[i][0]=="REPLACE":
#         cut = massag[i][1]
#         paste = massag[i][2]
#     elif massag[i][0] == "ADD" and massag[i][1]=='FIRST':
#         place = "FIRST"
#         message = massag[i][2]
#     elif massag[i][0] == "ADD" and massag[i][1]=='LAST':
#         place = "LAST"
#         message = massag[i][2]
#     elif massag[i][0] == "DELETE" :
#         cut = massag[i][1]
# post=[]
# with open('data\scraped_posts.csv', 'r',encoding="utf8") as File:  
#     read = csv.reader(File)
#     for i in read:
#         post.append(i)
# for i in range(len(post)):
#     print(post[i][1])






# final_post=[]
# post=[]
# with open('data\scraped_posts.csv', 'r',encoding="utf8") as File:  
#     read = csv.reader(File)
#     for i in read:
#         post.append(i)
# # x="ADD"
# # start="Good Morning Everyone\n"
# # end = "\nThanks Amit"
# # y="FIRSeT"
# # z="LAST"
# # x="DELETE"
# # deleted = "Text"
# massag=[]
# with open('Input\CONFIG_FACEBOOK_DATAMASSAGING.CSV', 'r') as File:  
#     readr = csv.reader(File)
#     for row in readr:
#         massag.append(row)

# for j in range(len(post)):
#     x=post[j][1]
#     # print(massag)
#     for i in range(1,len(massag)):
#         if massag[i][0]=="REPLACE":
#             cut = massag[i][1]
#             paste = massag[i][2]
#             x=x.replace(cut,paste)
#         elif massag[i][0] == "ADD" and massag[i][1]=='FIRST':
#             place = "FIRST"
#             message = massag[i][2]
#             x=message + x
#         elif massag[i][0] == "ADD" and massag[i][1]=='LAST':
#             place = "LAST"
#             message = massag[i][2]
#             x = x + message
#         elif massag[i][0] == "DELETE" :
#             cut = massag[i][1]
#             x.replace(cut,"")
#     final_post.append(x)
# print(final_post)
# def textJamming():
#     final_post=[]
#     post=[]
#     with open('data\scraped_posts.csv', 'r',encoding="utf8") as File:  
#         read = csv.reader(File)
#         for i in read:
#             post.append(i)
#     massag=[]
#     with open('Input\CONFIG_FACEBOOK_DATAMASSAGING.CSV', 'r') as File:  
#         readr = csv.reader(File)
#         for row in readr:
#             massag.append(row)

#     for j in range(len(post)):
#         x=post[j][1]
#         for i in range(1,len(massag)):
#             if massag[i][0]=="REPLACE":
#                 cut = massag[i][1]
#                 paste = massag[i][2]
#                 x=x.replace(cut,paste)
#             elif massag[i][0] == "ADD" and massag[i][1]=='FIRST':
#                 place = "FIRST"
#                 message = massag[i][2]
#                 x=message + x
#             elif massag[i][0] == "ADD" and massag[i][1]=='LAST':
#                 place = "LAST"
#                 message = massag[i][2]
#                 x = x + message
#             elif massag[i][0] == "DELETE" :
#                 cut = massag[i][1]
#                 x.replace(cut,"")
#         final_post.append(x)
#     return final_post
# x=textJamming()
# print(x)

from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import re as re
import urllib
import urllib.request
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome('chromedriver')

#Open login page
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

#Enter login info:
elementID = browser.find_element_by_id('username')
elementID.send_keys("enter email")

elementID = browser.find_element_by_id('password')
elementID.send_keys("enter password")
#Note: replace the keys "username" and "password" with your LinkedIn login info
elementID.submit()

# browser.get('https://www.linkedin.com/in/ajjames/detail/recent-activity/shares/')

# time.sleep(2)

# browser.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div/div/div/div/div/div/a/img').click()

# x=browser.current_url
# print(x)
# browser.get('https://www.linkedin.com/in/ajjames/detail/recent-activity/shares/')
# 
# import urllib.request
# arr=[]
# with open('data\scraped_posts.csv', 'r',encoding="utf8") as File:  
#     read = csv.reader(File)
#     for row in read:
#         arr.append(row)
# for i in range(len(arr)):
#     if arr[i][1]=="IMAGE":
#         try:
#             urllib.request.urlretrieve(arr[i][3],'data\img{}.jpg'.format(i))
#         except:
#             pass
#     elif arr[i][1]=="VIDEO":
#         # try:
#         urllib.request.urlretrieve(arr[i][3], 'data/video{}.mp4'.format(i))
#         # except:
#         #     pass
# print("Done")

# with open('data\scraped_posts.csv', 'r',encoding="utf8") as File:  
#     read = csv.reader(File)
#     for row in read:
#         arr.append(row)
# https://www.linkedin.com/in/amit-kumar-62068218b/detail/recent-activity/shares/

# df = pd.read_csv('Output\OUTPUT_LINKEDIN_SCRAPEDPOSTS.csv')
# df.drop_duplicates(subset = None,inplace=True)
# df.to_csv('Output\OUTPUT_LINKEDIN_SCRAPEDPOSTS.csv', index=False)

def poster(post_texts,flag,):
    #Open login page
    browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

    #Enter login info:
    elementID = browser.find_element_by_id('username')
    elementID.send_keys("Enter EMail")

    elementID = browser.find_element_by_id('password')
    elementID.send_keys("Enter Password")
    #Note: replace the keys "username" and "password" with your LinkedIn login info
    elementID.submit()
    browser.get('https://www.linkedin.com/feed/')

    time.sleep(3)

    browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/button').click()

    time.sleep(3)

    post_texts_final=post_texts + " "
    browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/p').send_keys(post_texts_final)

    time.sleep(5)

    if flag == 'Image':
        #click image button on post
        browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/span[1]/button').click()
        time.sleep(5)
        #give image
        browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/input').send_keys('E:\Internship\Output\data\img.mp3')
        time.sleep(5)
        #cick done
        browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[2]/div/button[2]').click()
    elif flag== 'Video':
        #click image button on post
        browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/span[2]/button').click()
        time.sleep(5)
        #give video
        browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[1]/div/input').send_keys('E:\Internship\Output\data/video.mp4')
        time.sleep(15)
        #click done
        browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[2]/div/button[2]').click()  
    else:
        pass
    browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[3]/button').click()
    browser.close()
    print("The Post was made !!")

# text="Test Post"
# flag='Image'
# poster(text,flag)
arr=[]
with open('Output\OUTPUT_LINKEDIN_SCRAPEDPOSTS.csv', 'r',encoding="utf-8") as File:  
    read = csv.reader(File)
    for row in read:
        arr.append(row)
print(arr[2][4])
print(arr[2][3])
for i in range(len(arr)):
    post_texts=arr[i][3]
    post_media= arr[i][2]
    post_media_url=arr[i][4]
    if post_media=='IMAGE':
        urllib.request.urlretrieve(post_media_url,'Output\data\img.jpg'.format(i))
        flag = 'Image'
        poster(post_texts,flag)

    elif post_media == "VIDEO":
        urllib.request.urlretrieve(post_media_url, 'Output\data/video.mp4'.format(i))
        flag="Video"
        poster(post_texts,flag)

    elif post_media == "IMAGE":
        urllib.request.urlretrieve(post_media_url, "Output\data\img.jpg".format)
        flag="Image"
        poster(post_texts,flag)
    # except:
    #     pass
print("DONE")