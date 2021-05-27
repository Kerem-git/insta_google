from bs4.element import Declaration
from cryptography.fernet import Fernet
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
    
    message = ""
    a = "b'gAAAAABgruMNiLbqXsYwsvrx0hldY86qNj06OZL9fJxg2j59qxfWjZ04SC6BoQHHRrJbXFyaPtzZCxtFEJSteljdxGMA5LBDCeNo-qNNZ-a7jx32TpXKZRK1qM1NhNc34QYYGlvSoGLu'"
    key = Fernet.generate_key()
    
    fernet = Fernet(key)

    encMessage = fernet.encrypt(message.encode())

    print("encrypted string: ", encMessage)
    sleep(1000)
    decMessage = fernet.decrypt(encMessage).decode()
    if "Perşembe" in day:
        print("decrypted string: ", decMessage)
        sys.stdout.write("\033[F")
        sleep(43000)
        sys.stdout.write("\033[K")
