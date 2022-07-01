import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys


class Fetcher:
    def __int__(self, url):
        self.driver = webdriver.PhantomJS()   #javascript
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.url = url

    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.driver.wait.unitl(EC.presence_of_element_located(
                (By.CLASS_NAME, "gsfi")
            ))
        except:
            print("Failed bro")

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        ans = soup.find_all(class_="_sPg")

        with open("test.html", "w+") as f:    # write them in a text file
            f.write(str(soup))

        if not ans:
            ans = soup.find_all(class_="_m3b")

        if not ans:
            ans = "I don't know. "

        self.driver.quit()
        return ans[0].get_text    # print the entire web search source




