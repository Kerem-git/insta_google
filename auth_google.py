from bs4.element import Declaration
from time import sleep
import requests
from bs4 import BeautifulSoup
import sys
import smtplib

print("bot has been started.")
email = "mahmutcarlsen@gmail.com"
password = "Kerem2894" 
mails= ["keremtowork@gmail.com","keremtowork@gmail.com"]

for i in range(999999999999999):
    url= "https://www.timeanddate.com/worldclock/turkey/adana"
    date = requests.get(url)
    soup = BeautifulSoup(date.content,"html5lib")
    day = soup.find("span",{"id":"ctdat"}).text
    print(day)
    print("I'm still working")
    key = "BQ5A K56L 4IFT ACEZ QODW EF5X TB2N MBOU"
    sleep(30000)
    if "Thursday" in day:
        with smtplib.SMTP("smtp.gmail.com",587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(email, password)
            subject = "Auth Kodun."
            body = key
            msg = f"Subject: {subject}\n\n{body}"
            smtp.sendmail(email,mails[0],msg)

