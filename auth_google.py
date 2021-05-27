from bs4.element import Declaration
from time import sleep
import requests
from bs4 import BeautifulSoup
import sys
print("bot has been started.")
for i in range(999999999999999):
    url= "https://www.timeanddate.com/worldclock/turkey/adana"
    date = requests.get(url)
    soup = BeautifulSoup(date.content,"html5lib")
    day = soup.find("span",{"id":"ctdat"}).text
    print(day)
    print("I'm still working")
    key = "BQ5A K56L 4IFT ACEZ QODW EF5X TB2N MBOU"
    sleep(1)
    if "Thursday" in day:
        print(key)
        sys.stdout.write("\033[F")
        sleep(3)
        sys.stdout.write("\033[K")

