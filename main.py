# from bs4 import BeautifulSoup
# import requests
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth

# # Scraping Billboard 100
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
# billboard_url = "https://www.billboard.com/charts/hot-100/" + date
# response = requests.get(url=billboard_url, headers=header)

# soup = BeautifulSoup(response.text, 'html.parser')
# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]

# # Spotify Authentication
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="https://www.spotify.myapp.com",
#         client_id="40fb8955655b4c228bdcb89a02491a5d",
#         client_secret="ac445c2ccb28421588d94d5e34eff614",
#         show_dialog=True,
#         cache_path="token.txt"
#     )
# )
# user_id = sp.current_user()["id"]
# print(user_id)

# # Searching Spotify for songs by title
# song_uris = []
# year = date.split("-")[0]
# for song in song_names:
#     result = sp.search(q=f"track:{song} year:{year}", type="track")
#     print(result)
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped.")

# # Creating a new private playlist in Spotify
# playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

# # Adding songs found into the new playlist
# sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

# from bs4 import BeautifulSoup
# import requests
# import smtplib

# header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}


# response=requests.get(url="https://appbrewery.github.io/instant_pot/",headers=header)

# soup=BeautifulSoup(response.content,"html.parser")
# ask=soup.find(name="span",class_="a-price-fraction").getText()
# a=ask.split(">")[0]
# b=float(a)
# print(b)

# product_title=soup.find(id="productTitle").getText().strip()
# print(product_title)

# price=100
# url="https://appbrewery.github.io/instant_pot/"
# if b==price:
#     message=f"your product{product_title} , is on a sale price of{b},get it soon"

#     with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
#         connection.starttls
#         results=connection.login("dhruvpujari1@gmail.com",password="dhruvpujari")
#         connection.sendmail(
#             from_addr="dhruvpujari1@gmail.com",
#             to_addrs="dhruvpujari1@gmail.com",
#             msg=f"subject:Amazon price alert\n\n{message}\n{url}".encode("utf-8")
#         )
    

#for other product price tracer
# from bs4 import BeautifulSoup
# import requests


# ur="https://www.amazon.in/NIKE-FB2207-Revolution-7-BLACK-WHITE-FB2207-001-10UK/dp/B0C8TJ8G78/ref=sr_1_1?crid=220LB2NV232QT&dib=eyJ2IjoiMSJ9.H6Jl-XO3cuv_6MbrG-2aIfI_xaPa87qWuaowdwmV7WDrwojbg5Od-5oMNqLmuH1I1hrAVgW9hOhVqjHPPOKSFcLCsNvAJ3JJrFcDM-UREcg8LcdCMUPB5_-mgTBn0pp-FcKY6EQ4gkYMOzbRC9NznsJ3bLwtbM0YrMm_2zRW3xldklUWdpmsmyF2Le1QsW-jzZpHoeWITPeNEml12CsbvLnZYrxLg6Cmr0GK4MbnymdVLay7RFAzWv9z1zJ2ZlvIuiqVCT5LbrsoV9Okap6P5M2zkmFeB28W6gLYJko6rpQ.4Q-k0yr3HIWh_KmDCzBmqy52EShnGXL3Lmcr2M-2fIo&dib_tag=se&keywords=nike+shoes+for+man&nsdOptOutParam=true&qid=1735890212&sprefix=nike%2Caps%2C217&sr=8-1"

# header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}


# response=requests.get(ur,headers=header)

# soup=BeautifulSoup(response.text,"html.parser")
# ak=soup.find(name="span",class_="a-price-whole").getText()
# price=ak.split(">")[0]
# # c=float(d)
# shop=10000

# title=soup.find(id="productTitle").getText()
# print(title)

# good=True
# while good:
#     if price < shop:
#         print(f"your product{title}\n,is now on sale!!!{price}!!!\n,click here to buy{ur}")
 



# from selenium import webdriver
# from selenium.webdriver.common.by import By

# chrome_options=webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach",True)

# driver=webdriver.Chrome(options=chrome_options)
# driver.get("https://www.python.org/")

# # price=driver.find_element(By.CLASS_NAME,value="a-price-whole")

# # price_cent=driver.find_element(By.CLASS_NAME,value="a-price-fraction")


# # print(f"the price{price.text}{price_cent.text}")
# # # driver.close()
# # driver.quit()

# event=driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")

# event_names=driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

# events={}

# for n in range(len(event_names)):
#     events[n]={
#         "time":event[n].text,
#         "name":event_names[n].text,
#     }
# print(events)


# from selenium import webdriver
# from selenium.webdriver.common.by import By

# chrome_options=webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach",True)

# driver=webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# entry=driver.find_element(By.CSS_SELECTOR,value="#articlecount a ")
# # for number in entry:
# print(entry.text)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

# chrome_options=webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach",True)

# driver=webdriver.Chrome(chrome_options)
# driver.get("https://www.linkedin.com/jobs/?focusToMoreMenuTrigger=true&showJobAlertsModal=false")


# name=driver.find_element(By.NAME,value="session_key")
# name.send_keys("dhruvpujari1@gmail.com")

# password=driver.find_element(By.NAME, value="session_password")
# password.send_keys("dhruv252003")

# click=driver.find_element(By.XPATH,value='//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
# click.click()

# # search=driver.find_element(By.ID,value="jobs-search-box-keyword-id-ember27")
# # search.send_keys("python developer")

# enter=driver.find_element(By.XPATH,value="/html/body/div[5]/header/div/div/div/div[2]/div[2]/div/div/input[1]")
# enter.send_keys("python developer")
# enter.send_keys(Keys.ENTER)

# loc=driver.find_element(By.XPATH,value='//*[@id="jobs-search-box-location-id-ember345"]')
# loc.send_keys("Pune")

# loc=driver.find_element(By.XPATH,value='//*[@id="jobs-search-box-location-id-ember28"]')
# loc.send_keys("Pune")
# mes=driver.find_element(By.CLASS_NAME,value="truncate")
# mes.click()
# chat=driver.find_element(By.XPATH,value='//*[@id="msg-form-ember1028"]/div[3]/div[1]/div/div[1]/p')
# chat.send_keys("update?")

# x=driver.find_element(By.CLASS_NAME,value="artdeco-button__icon ")
# x.click()

# ak=driver.find_element(By.ID,value="jobs-search-box-keyword-id-ember28")
# ak.send_keys("python developer")
# # buy=driver.find_element(By.ID,value="buyGrandm")

# ak=driver.find_element(By.ID,value="money")
# # buy=driver.find_element(By.ID,value="buyGrandma")
# s=100
# if ak>=s:
# buy=driver.find_element(By.ID,value="buyGrandma")
# buy.click() 
    # if ak==100:
    #     buy=driver.find_element(By.ID,value="buyGrandm")
    #     buy.click()
    # if ak==100:

    
    # ask=driver.find_element(By.CSS_SELECTOR,value="#bigCookie")
# ask.click()
# a=driver.find_element(By.NAME,value="lName")
# a.send_keys("pujari")

# b=driver.find_element(By.NAME,value="email")
# b.send_keys("dhruvpujari25@gmail.com")

# button=driver.find_element(By.CSS_SELECTOR,value="button")
# button.click()


# link=driver.find_element(By.LINK_TEXT, value="Content portals")
# # # # link.click() 
# # icon=driver.find_element(By.CLASS_NAME, value="vector-icon mw-ui-icon-search mw-ui-icon-wikimedia-search")
# # icon.click()
# keys=driver.find_element(By.NAME,value="search")

# keys.send_keys("python", Keys.ENTER)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time


# username="sugarinsane07"
# password="sugarpujari07"

# class instafollower:

#     def __init__(self):
#         chrome_option=webdriver.ChromeOptions()
#         chrome_option.add_experimental_option("detach",True)
#         self.driver=webdriver.Chrome(chrome_option)

#     def login(self):
#         self.driver.get("https://www.instagram.com/accounts/login/")
#         time.sleep(4.2)

#         decline_cookies_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
#         cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)

#         if cookie_warning:
#             cookie_warning[0].click()


#         username=self.driver.find_element(By.NAME,value="username")
#         username.click()
#         username.send_keys("sugarinsane07")

#         password=self.driver.find_element(By.NAME,value="password")
#         password.click()
#         password.send_keys("sugarpujari07") 

#         time.sleep(2.1)
#         password.send_keys(Keys.ENTER)
    
#         time.sleep(4.3)
#         # Click "Not now" and ignore Save-login info prompt
#         save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
#         if save_login_prompt:
#             save_login_prompt.click()
#         find=self.driver.find_element(By.CSS_SELECTOR,value="titlr Search")
#         find.click()

        # time.sleep(3.7)
        # Click "not now" on notifications prompt
        # notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        # if notifications_prompt:
        #     notifications_prompt.click()

    # def find_follower(self):
    #     # time.sleep(5)
    #     find=self.driver.find_element(By.CLASS_NAME,value="x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft")
    #     find.click()
        # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",find)
        
        # search=self.driver.find_element(By.XPATH,value='//*[@id="mount_0_0_qA"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
        # search.click()
        # search.send_keys("carryminati")
    


    # def follow(self):
    #     pass

# bot=instafollower()
# bot.login()
# bot.find_follower()
# bot.follow()

    
# driver.get("https://www.instagram.com/accounts/login/")
# link=https://docs.google.com/forms/d/e/1FAIpQLSdJa4tJjLgM2-mGLzdWRf2s3cRu5w9hjFuXOObDfX-EM1Vucg/viewform?usp=header

    
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)
driver=webdriver.Chrome(chrome_option)

# driver.get(url="https://docs.google.com/forms/d/e/1FAIpQLSdJa4tJjLgM2-mGLzdWRf2s3cRu5w9hjFuXOObDfX-EM1Vucg/viewform?usp=header")

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


response=requests.get(url="https://appbrewery.github.io/Zillow-Clone/",headers=header)


soup=BeautifulSoup(response.text,"html.parser")

#all price for property  data####################


all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]
# print(f"\n After having been cleaned up, the {len(all_prices)} prices now look like this: \n")
print(all_prices)

# all address data###############################


all_address_elements=soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]
# print(f"\n After having been cleaned up, the {len(all_addresses)} addresses now look like this: \n")
print(all_addresses)

#all links data#################################

all_link_elements = soup.select(".StyledPropertyCardDataWrapper a") 
all_links = [link["href"] for link in all_link_elements] 
# print(f"There are {len(all_links)} links to individual listings in total: \n")
print(all_links)

for n in range(len(all_links)):

    driver.get(url="https://docs.google.com/forms/d/e/1FAIpQLSdJa4tJjLgM2-mGLzdWRf2s3cRu5w9hjFuXOObDfX-EM1Vucg/viewform?usp=header")

    add=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add.send_keys(all_addresses[n])
    
    price=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(all_prices[n])
    
    link=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(all_links[n])

    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()

