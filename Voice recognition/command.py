import subprocess
import os
import requests
from bs4 import BeautifulSoup
from get_answer import Fetcher

from django.core.management.commands import shell


class commander:         # command back or response from the terminal
    def __int__(self):
        self.confirm = ["yes", "affirmative", "yeah"]
        self.cancle = ["no", "negative", "nope"]

    def discover(self, text):      # response like a artificial intelligent
        if "what" in text and "name" in text:
            if "my" in text:
                self.response("you haven't told me your name yet")
            else:
                self.response("my name is python")
        else:
            f = Fetcher("https://www.google.com/search?q=" + text)   # web search
            ans = f.lookup()
            self.respond(ans)

        if "launch" or "open" in text:    # for application
            app = text.split(" ", 1)[-1]
            self.respond("Opening " + app)
            os.system("open -a" + app + ".app")   # open the application

    def respond(self, response):
        print(response)
        subprocess.call("say " + response, shell=True)