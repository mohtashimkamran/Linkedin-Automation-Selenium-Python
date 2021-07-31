from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import re as re

# page = input("Enter the Company Linkedin URL: ")
# company_name = page[33:-1]

# try:
#     f= open("credentials.txt","r")
#     contents = f.read()
#     username = contents.replace("=",",").split(",")[1]
#     password = contents.replace("=",",").split(",")[3]
# except:
# f= open("credentials.txt","w+")
# username = input('Enter your linkedin username: ')
# password = input('Enter your linkedin password: ')
# f.write("username={}, password={}".format(username,password))
# f.close()


# In[7]:


#access Webriver
browser = webdriver.Chrome('chromedriver')

#Open login page
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

#Enter login info:
elementID = browser.find_element_by_id('username')
elementID.send_keys('')

elementID = browser.find_element_by_id('password')
elementID.send_keys('')
#Note: replace the keys "username" and "password" with your LinkedIn login info
elementID.submit()


# In[8]:


#Go to webpage
browser.get('https://www.linkedin.com/in/strati-georgopoulos/detail/recent-activity/shares/')


# In[9]:


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

    # # Calculate new scroll height and compare with last scroll height
    # new_height = browser.execute_script("return document.body.scrollHeight")
    # if new_height == last_height:
    #     break
    # last_height = new_height


company_page = browser.page_source   


# In[10]:


linkedin_soup = bs(company_page.encode("utf-8"), "html.parser")
linkedin_soup.prettify()

containers = linkedin_soup.findAll("div",{"class":"occludable-update ember-view"})
#container = containers[0].find("div","display-flex feed-shared-actor display-flex feed-shared-actor--with-control-menu ember-view")


# In[21]:


post_dates = []
post_texts = []
post_likes = []
post_comments = []
video_views = []
media_links = []
media_type = []


for container in containers:

    try:
        posted_date = container.find("span",{"class":"visually-hidden"})
        text_box = container.find("div",{"class":"feed-shared-update-v2__description-wrapper ember-view"})
        text = text_box.find("span",{"dir":"ltr"})
        new_likes = container.findAll("li", {"class":"social-details-social-counts__reactions social-details-social-counts__item"})
        new_comments = container.findAll("li", {"class": "social-details-social-counts__comments social-details-social-counts__item"})


        post_dates.append(posted_date.text.strip())
        post_texts.append(text.text.strip())



        try:
            video_box = container.findAll("div",{"class": "feed-shared-update-v2__content feed-shared-linkedin-video ember-view"})
            video_link = video_box[0].find("video", {"class":"vjs-tech"})
            media_links.append(video_link['src'])
            media_type.append("Video")
        except:
            try:
                image_box = container.findAll("div",{"class": "feed-shared-image__container"})
                image_link = image_box[0].find("img", {"class":"ivm-view-attr__img--centered feed-shared-image__image feed-shared-image__image--constrained lazy-image ember-view"})
                media_links.append(image_link['src'])
                media_type.append("Image")
            except:
                try:
                    #mutiple shared images
                    image_box = container.findAll("div",{"class": "feed-shared-image__container"})
                    image_link = image_box[0].find("img", {"class":"ivm-view-attr__img--centered feed-shared-image__image lazy-image ember-view"})
                    media_links.append(image_link['src'])
                    media_type.append("Multiple Images")
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
                                media_type.append("Other: Poll, Shared Post, etc")
                            except:
                                media_links.append("None")
                                media_type.append("Unknown")



        #Getting Video Views. (The folling three lines prevents class name overlap)
        view_container2 = set(container.findAll("li", {'class':["social-details-social-counts__item"]}))
        view_container1 = set(container.findAll("li", {'class':["social-details-social-counts__reactions","social-details-social-counts__comments social-details-social-counts__item"]}))
        result = view_container2 - view_container1

        view_container = []
        for i in result:
            view_container += i

        try:
            video_views.append(view_container[1].text.strip().replace(' Views',''))

        except:
            video_views.append('N/A')


        try:
            post_likes.append(new_likes[0].text.strip())
        except:
            post_likes.append(0)
            pass

        try:
            post_comments.append(new_comments[0].text.strip())                           
        except:                                                           
            post_comments.append(0)
            pass
    
    except:
        pass


# In[22]:


# cleaned_dates = []
# for i in post_dates:
#     d = str(i[0:3]).replace('\n\n', '').replace('•','').replace(' ', '')
#     cleaned_dates += [d]
    
comment_count = []
for i in post_comments:
    s = str(i).replace('Comment','').replace('s','').replace(' ','')
    comment_count += [s]


# In[23]:


#pd.set_option('max_colwidth', 1000)

data = {
    "Date Posted": post_dates,
    "Media Type": media_type,
    "Post Text": post_texts,
    "Post Likes": post_likes,
    "Post Comments": comment_count,
    "Video Views": video_views,
    "Media Links": media_links
}


df = pd.DataFrame(data)
df


# In[28]:


df.to_csv("{}_posts.csv".format('Hello'), encoding='utf-8', index=False)

writer = pd.ExcelWriter("{}_posts.xlsx".format("helo"), engine='xlsxwriter')
df.to_excel(writer, index =False)
writer.save()


# In[ ]:

