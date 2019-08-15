{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 380,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from splinter.exceptions import ElementDoesNotExist\n",
    "from bs4 import BeautifulSoup\n",
    "import pymongo\n",
    "import pandas as pd\n",
    "import requests\n",
    "from selenium import webdriver\n",
    "import time\n",
    "import splinter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 382,
   "metadata": {},
   "outputs": [],
   "source": [
    "# create dict to store info\n",
    "mars_info = {}\n",
    "\n",
    "# build pathing for splinter and Soup\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "url = 'https://mars.nasa.gov/news'\n",
    "browser.visit(url)\n",
    "\n",
    "html = browser.html\n",
    "\n",
    "time.sleep(10)\n",
    "\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "# use soup to find title info\n",
    "title = soup.find('div', class_=\"content_title\").text\n",
    "\n",
    "# store the tile\n",
    "mars_info['title']=title\n",
    "\n",
    "body = soup.find('div', class_='article_teaser_body').text\n",
    "\n",
    "body\n",
    "\n",
    "# store the body\n",
    "mars_info['body']=body\n",
    "\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 383,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "url = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "\n",
    "browser.visit(url)\n",
    "\n",
    "html = browser.html\n",
    "\n",
    "image = browser.find_by_css('#page > section.multi_teaser.module > div > ul > li:nth-child(1) > a > div.image_and_description_container > img')\n",
    "\n",
    "for i in image:\n",
    "    featured_image_url = i['src']\n",
    "\n",
    "featured_image_url\n",
    "\n",
    "mars_info['featured_image_url']=featured_image_url\n",
    "\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 379,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "url = \"https://twitter.com/marswxreport?lang=en\"\n",
    "\n",
    "browser.visit(url)\n",
    "\n",
    "html = browser.html\n",
    "\n",
    "tweet = browser.find_by_css('#stream-item-tweet-1161319330275045376 > div.tweet.js-stream-tweet.js-actionable-tweet.js-profile-popup-actionable.dismissible-content.original-tweet.js-original-tweet.has-cards.has-content > div.content > div.js-tweet-text-container > p')\n",
    "\n",
    "tweet\n",
    "\n",
    "tweet.is_empty()\n",
    "\n",
    "for t in tweet:\n",
    "    mars_weather = t.text\n",
    "\n",
    "mars_weather\n",
    "\n",
    "mars_info['mars_weather']=mars_weather\n",
    "\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 384,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'InSight sol 251 (2019-08-11) low -101.0ºC (-149.7ºF) high -26.5ºC (-15.8ºF)\\nwinds from the SSE at 4.1 m/s (9.2 mph) gusting to 17.5 m/s (39.1 mph)\\npressure at 7.60 hPa'"
      ]
     },
     "execution_count": 384,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 385,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "url = 'https://space-facts.com/mars/'\n",
    "\n",
    "browser.visit(url)\n",
    "\n",
    "html = browser.html\n",
    "\n",
    "table = pd.read_html(url)\n",
    "\n",
    "mdf = table[1]\n",
    "\n",
    "mdf = mdf.rename(columns={0:\"\",1:\"value\"})\n",
    "\n",
    "mdf.to_html()\n",
    "\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 387,
   "metadata": {},
   "outputs": [],
   "source": [
    "hemisphere_image_urls = []\n",
    "\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "\n",
    "browser.visit(url)\n",
    "\n",
    "html = browser.html\n",
    "\n",
    "step1 = browser.find_by_css('#product-section > div.collapsible.results > div:nth-child(1) > div > a > h3')\n",
    "\n",
    "step1.click()\n",
    "\n",
    "step2 = browser.find_by_css('#wide-image > div > ul > li:nth-child(1) > a')\n",
    "\n",
    "step2.click()\n",
    "\n",
    "cerberus_url = browser.url\n",
    "\n",
    "cerberus = {\"image title\":\"Cerberus Hemisphere\", \"image url\": cerberus_url}\n",
    "\n",
    "\n",
    "hemisphere_image_urls.append(cerberus)\n",
    "\n",
    "browser.windows.current\n",
    "\n",
    "browser.back()\n",
    "\n",
    "step3 = browser.find_by_css('#product-section > div.collapsible.results > div:nth-child(2) > div > a > h3')\n",
    "\n",
    "step3.click()\n",
    "\n",
    "step4 = browser.find_by_css('#wide-image > div > ul > li:nth-child(1) > a')\n",
    "\n",
    "step4.click()\n",
    "\n",
    "schiaparelli_url = browser.url\n",
    "\n",
    "schiaparelli = {\"image title\":\"Schiaparelli Hemisphere\", \"image url\": schiaparelli_url}\n",
    "\n",
    "hemisphere_image_urls.append(schiaparelli)\n",
    "\n",
    "\n",
    "browser.windows.current\n",
    "\n",
    "browser.back()\n",
    "\n",
    "step5 = browser.find_by_css('#product-section > div.collapsible.results > div:nth-child(3) > div > a > h3')\n",
    "\n",
    "step5.click()\n",
    "\n",
    "step6 = browser.find_by_css('#wide-image > div > ul > li:nth-child(1) > a')\n",
    "\n",
    "step6.click()\n",
    "\n",
    "syrtis_url = browser.url\n",
    "\n",
    "syrtis = {\"image title\":\"Syrtis Hemisphere\", \"image url\": syrtis_url}\n",
    "\n",
    "hemisphere_image_urls.append(syrtis)\n",
    "\n",
    "\n",
    "browser.windows.current\n",
    "\n",
    "browser.back()\n",
    "\n",
    "step7 = browser.find_by_css('#product-section > div.collapsible.results > div:nth-child(4) > div > a > h3')\n",
    "\n",
    "step7.click()\n",
    "\n",
    "step8 = browser.find_by_css('#wide-image > div > ul > li:nth-child(1) > a')\n",
    "\n",
    "step8.click()\n",
    "\n",
    "valles_url = browser.url\n",
    "\n",
    "valles = {\"image title\":\"Valles Hemisphere\", \"image url\": valles_url}\n",
    "\n",
    "hemisphere_image_urls.append(valles)\n",
    "\n",
    "\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 389,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'title': \"Space Samples Link NASA's Apollo 11 and Mars 2020\",\n",
       " 'body': \"While separated by half a century, NASA's Apollo 11 and Mars 2020 missions share the same historic goal: returning samples to Earth.\",\n",
       " 'featured_image_url': 'https://imagecache.jpl.nasa.gov/images/640x350/apollo-mars2020-20190809-16-640x350.jpg'}"
      ]
     },
     "execution_count": 389,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mars_info['hemisphere_image-urls']=hemisphere"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 366,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 368,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
