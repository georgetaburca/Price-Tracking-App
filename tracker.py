import requests

from bs4 import BeautifulSoup

import smtplib

URL = "https://www.amazon.com/Lenovo-Chromebook-Convertible-11-6-Inch-81HY0000US/dp/B07GM2J11Q?ref_=Oct_DLandingS_D_97c4e409_60&smid=ATVPDKIKX0DER"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = soup1.prettify()
    title = soup2.find(id="productTitle").get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price < 2.700):
        send_mail()
    print(converted_price)
    print(title.strip())

    
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('youremail@gmail.com', 'mjutimzlroarivxo')
    subject = 'Price decreased'
    body = 'Your camera is now on sale! Get it now: https://www.amazon.com/Lenovo-Chromebook-Convertible-11-6-Inch-81HY0000US/dp/B07GM2J11Q?ref_=Oct_DLandingS_D_97c4e409_60&smid=ATVPDKIKX0DER'

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'yourname@gmail.com',
        'yourname@yahoo.com',
        msg
    )
    print('HELLO, EMAIL HAS BEEN SENT!')
    server.quit()

check_price()    