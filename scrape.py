# #Enter Email and Password at line 20,23

# from selenium import webdriver
# from bs4 import BeautifulSoup as bs
# import time
# import pandas as pd
# import re as re
# import urllib
# import urllib.request
# from selenium.webdriver.common.keys import Keys
# import csv


# browser = webdriver.Chrome('chromedriver')

# #Open login page
# def scraper(target_url):
#     browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

#     #Enter login info:
#     elementID = browser.find_element_by_id('username')
#     elementID.send_keys("")

#     elementID = browser.find_element_by_id('password')
#     elementID.send_keys("")
#     #Note: replace the keys "username" and "password" with your LinkedIn login info
#     elementID.submit()


#     #Go to webpage
#     browser.get(target_url)


#     SCROLL_PAUSE_TIME = 1.5

#     # Get scroll height
#     last_height = browser.execute_script("return document.body.scrollHeight")
#     i=1
#     while True:
#         # Scroll down to bottom
#         browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#         # Wait to load page
#         time.sleep(SCROLL_PAUSE_TIME)
#         if i==3:
#             break
#         i+=1

    
#     company_page = browser.page_source 
#     linkedin_soup = bs(company_page.encode("utf-8"), "html.parser")
#     linkedin_soup.prettify()

#     containers = linkedin_soup.findAll("div",{"class":"occludable-update ember-view"})

#     post_dates = []
#     post_texts = []
#     media_links = []
#     media_type = []


#     for container in containers:

#         try:
#             posted_date = container.find("span",{"class":"visually-hidden"})
#             text_box = container.find("div",{"class":"feed-shared-update-v2__description-wrapper ember-view"})
#             text = text_box.find("span",{"dir":"ltr"})
#             # new_likes = container.findAll("li", {"class":"social-details-social-counts__reactions social-details-social-counts__item"})
#             # new_comments = container.findAll("li", {"class": "social-details-social-counts__comments social-details-social-counts__item"})


#             post_dates.append(posted_date.text.strip())
#             post_texts.append(text.text.strip())



#             try:
                # video_box = container.findAll("div",{"class": "feed-shared-update-v2__content feed-shared-linkedin-video ember-view"})
                # video_link = video_box[0].find("video", {"class":"vjs-tech"})
                # media_links.append(video_link['src'])
#                 media_type.append("Video")
#             except:
#                 try:
#                     image_box = container.findAll("div",{"class": "feed-shared-image__container"})
#                     image_link = image_box[0].find("img", {"class":"ivm-view-attr__img--centered feed-shared-image__image feed-shared-image__image--constrained lazy-image ember-view"})
#                     media_links.append(image_link['src'])
#                     media_type.append("Image")
#                 except:
#                     try:
#                         #mutiple shared images
#                         image_box = container.findAll("div",{"class": "feed-shared-image__container"})
#                         image_link = image_box[0].find("img", {"class":"ivm-view-attr__img--centered feed-shared-image__image lazy-image ember-view"})
#                         media_links.append(image_link['src'])
#                         media_type.append("Multiple Images")
#                     except:
#                         try:
#                             article_box = container.findAll("div",{"class": "feed-shared-article__description-container"})
#                             article_link = article_box[0].find('a', href=True)
#                             media_links.append(article_link['href'])
#                             media_type.append("Article")
#                         except:
#                             try:
#                                 video_box = container.findAll("div",{"class": "feed-shared-external-video__meta"})          
#                                 video_link = video_box[0].find('a', href=True)
#                                 media_links.append(video_link['href'])
#                                 media_type.append("Youtube Video")   
#                             except:
#                                 pass
#         except:
#             pass
    
#     data = {
#         "Date Posted": post_dates,
#         "Media Type": media_type,
#         "Post Text": post_texts,
#         "Media Links": media_links
#     }

#     df = pd.DataFrame(data)

#     df.to_csv("data\{}_posts.csv".format('Scraped'), encoding='utf-8', index=False)

#     writer = pd.ExcelWriter("data\{}_posts.xlsx".format("Scraped"), engine='xlsxwriter')
#     df.to_excel(writer, index =False)
#     writer.save()

#     flag="none"

    # if media_type[0]=='Image':
    #     urllib.request.urlretrieve(media_links[0],'data\img.jpg')
    #     flag = 'Image'

    # elif media_type[0] == "Video":
    #     urllib.request.urlretrieve(media_links[0], 'data\video.mp4')
    #     flag="Video"

    # elif media_type[0] == "Images":
    #     urllib.request.urlretrieve(media_links[0], "data\img.jpg")
    #     flag="Image"
    

# def poster(post_texts,flag,):
#     browser.get('https://www.linkedin.com/feed/')

#     time.sleep(3)

#     browser.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/div/div/div/main/div[1]/div/div[1]/button').click()

#     time.sleep(3)

#     post_texts_final=post_texts + " "
#     browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/p').send_keys(post_texts_final)

#     time.sleep(5)

#     if flag == 'Image':
#         #click image button on post
#         browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/span[1]/button').click()
#         time.sleep(5)
#         #give image
#         browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/input').send_keys('E:\Internship\img.jpg')
#         time.sleep(5)
#         #cick done
#         browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[2]/div/button[2]').click()
#     elif flag== 'Video':
#         #click image button on post
#         browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/span[2]/button').click()
#         time.sleep(5)
#         #give video
#         browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[1]/div/input').send_keys('E:\Internship/video.mp4')
#         time.sleep(15)
#         #click done
#         browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[2]/div/button[2]').click()  
#     else:
#         pass
#     browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[3]/button').click()
#     print("The Post was made !!")

# time.sleep(3)
# target_url = 'https://www.linkedin.com/in/ajjames/detail/recent-activity/shares/'
# scraper(target_url)
# browser.close()


# # import pandas as pd
# import csv
# arr=[]
# with open('Input\CONFIG_FACEBOOK_SCRAPE_SOURCE.csv', 'r') as File:  
#     read = csv.reader(File)
#     for row in read:
#         arr.append(row)
# for i in range(1,len(arr)):
#     target_url = arr[i][1]
#     media_type = arr[i][2]


 
# # with open('Input\CONFIG_FACEBOOK_SCRAPE_SOURCE.csv', newline='') as File:  
# #     reader = csv.reader(File)
# #     for row in reader:
# #         print(row)







from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import re as re
import urllib
import urllib.request
import csv
from datetime import datetime

browser = webdriver.Chrome('chromedriver')

#Open login page
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

#Enter login info:
elementID = browser.find_element_by_id('username')
elementID.send_keys("")

elementID = browser.find_element_by_id('password')
elementID.send_keys("")
#Note: replace the keys "username" and "password" with your LinkedIn login info
elementID.submit()


#Go to webpage
def scraper(target_url):
    browser.get(target_url)

    SCROLL_PAUSE_TIME = 1.5

    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")
    i=1
    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        i+=1
        if i==3:
            break


    company_page = browser.page_source 


    linkedin_soup = bs(company_page.encode("utf-8"), "html.parser")
    linkedin_soup.prettify()

    containers = linkedin_soup.findAll("div",{"class":"occludable-update ember-view"})

    linkedin_id =[]
    current_time =[]
    post_texts = []
    media_links = []
    media_type = []
    owners_profile=[]


    for container in containers:
        linkedin_id.append('None')
        current_time.append(str(datetime.now())[:19])
        owners_profile.append(target_url)
        try:
            text_box = container.find("div",{"class":"feed-shared-update-v2__description-wrapper ember-view"})
            text = text_box.find("span",{"dir":"ltr"})
            post_texts.append(text.text.strip())
            


            try:
                video_box = container.findAll("div",{"class": "feed-shared-update-v2__content feed-shared-linkedin-video ember-view"})
                video_link = video_box[0].find("video", {"class":"vjs-tech"})
                media_links.append(video_link['src'])
                media_type.append("VIDEO")
            except:
                try:
                    image_box = container.findAll("div",{"class": "feed-shared-image__container"})
                    image_link = image_box[0].find("img", {"class":"ivm-view-attr__img--centered feed-shared-image__image feed-shared-image__image--constrained lazy-image ember-view"})
                    media_links.append(image_link['src'])
                    media_type.append("IMAGE")
                except:
                    try:
                        #mutiple shared images
                        image_box = container.findAll("div",{"class": "feed-shared-image__container"})
                        image_link = image_box[0].find("img", {"class":"ivm-view-attr__img--centered feed-shared-image__image lazy-image ember-view"})
                        media_links.append(image_link['src'])
                        media_type.append("IMAGE")
                    except:
                        try:
                            article_box = container.findAll("div",{"class": "feed-shared-article__description-container"})
                            article_link = article_box[0].find('a', href=True)
                            media_links.append(article_link['href'])
                            media_type.append("Article")
                        except:
                            try:
                                video_box = container.findAll("div",{"class": "feed-shared-external-video__meta"})          
                                video_link = video_box[0].find('a', href=True)
                                media_links.append(video_link['href'])
                                media_type.append("Youtube Video")   
                            except:
                                try:
                                    poll_box = container.findAll("div",{"class": "feed-shared-update-v2__content overflow-hidden feed-shared-poll ember-view"})
                                    media_links.append("None")
                                    media_type.append("None")
                                except:
                                    media_links.append("NONE")
                                    media_type.append("Post Text")
        except:
            pass
    arr=[]
    arr.append(linkedin_id[:15])
    arr.append(current_time[:15])
    arr.append(owners_profile[:15])
    arr.append(media_type[:15])
    arr.append(post_texts[:15])
    arr.append(media_links[:15])
    return arr

def mediaFilter():
    arr=[]
    with open('Input\CONFIG_FACEBOOK_SCRAPE_SOURCE.csv', 'r') as File:  
        read = csv.reader(File)
        for row in read:
            arr.append(row)
    final_media_id=[]
    final_media_time=[]
    final_owner=[]
    final_media_type =[]
    final_media_post=[]
    final_media_url=[]
    for i in range(1,len(arr)):
        target_url = arr[i][1]
        media_type = arr[i][2]
        #get scraping done
        med = scraper(target_url)
        time.sleep(10)
        media_id = med[0]
        media_time = med[1]
        owner = med[2]
        media = med[3] #media type
        text = med[4]
        media_url = med[5] #media url
        if media_type.upper()=="ALL":
            final_media_id=media_id
            final_media_time=media_time
            final_owner=owner
            final_media_type=media
            final_media_post = text
            final_media_url=media_url
        else:
            for j in range(len(media)):
                if media[j]==media_type.upper():
                    final_media_id.append(media_id[j])
                    final_media_time.append(media_time[j])
                    final_owner.append(owner[j])
                    final_media_type.append(media[j])
                    final_media_post.append(text[j])
                    final_media_url.append(media_url[j])
    m = []
    m.append(final_media_id)
    m.append(final_media_time)
    m.append(final_owner)
    m.append(final_media_type)
    m.append(final_media_post)
    m.append(final_media_url)
    return m

#data massaging 
def textJamming(post):
    final_post=[]
    massag=[]

    with open('Input\CONFIG_FACEBOOK_DATAMASSAGING.CSV', 'r') as File:  
        readr = csv.reader(File)
        for row in readr:
            massag.append(row)

    for j in range(len(post)):
        x=post[j]
        for i in range(1,len(massag)):
            if massag[i][0].upper()=="REPLACE":
                cut = massag[i][1]
                paste = massag[i][2]
                x=x.replace(cut,paste)
            elif massag[i][0].upper() == "ADD" and massag[i][1].upper()=='FIRST':
                place = "FIRST"
                message = massag[i][2]
                x=message + x
            elif massag[i][0].upper() == "ADD" and massag[i][1].upper()=='LAST':
                place = "LAST"
                message = massag[i][2]
                x = x + message
            elif massag[i][0].upper() == "DELETE" :
                cut = massag[i][1]
                x.replace(cut,"")
        final_post.append(x)
    return final_post

# text_after_jamming = textJamming(final_media_post)
def make_csv():
    filtered_media = mediaFilter()
    final_id =filtered_media[0]
    final_time=filtered_media[1]
    final_owner = filtered_media[2]
    final_media_type = filtered_media[3]
    final_media_post=textJamming(filtered_media[4])
    final_media_url = filtered_media[5]

    ddata = {
            "Post Id" : final_id,
            # "Time when Scraped" : final_time,
            "Owners Profile" : final_owner,
            "Media Type": final_media_type,
            "Post Text": final_media_post,
            "Media Links": final_media_url,
            "Status" : "None"
        }

    df = pd.DataFrame(ddata)

    df.to_csv("Output\OUTPUT_LINKEDIN_SCRAPEDPOSTS.csv",mode='a', encoding='utf-8', index=False , header=False)

    df = pd.read_csv('Output\OUTPUT_LINKEDIN_SCRAPEDPOSTS.csv')
    df.drop_duplicates(subset=None,inplace=True)
    df.to_csv('Output\OUTPUT_LINKEDIN_SCRAPEDPOSTS.csv', index=False)

#final function to execute scrapping
make_csv()
def poster(post_texts,flag,):
    #Open login page
    browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

    #Enter login info:
    elementID = browser.find_element_by_id('username')
    elementID.send_keys("")

    elementID = browser.find_element_by_id('password')
    elementID.send_keys("")
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