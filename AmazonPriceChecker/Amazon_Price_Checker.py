import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/EVGA-GeForce-Gaming-Graphics-11G-P4-2487-KR/dp/B07KVKRLG2/ref=sr_1_2?keywords=gtx+2080ti&qid=1571762672&s=electronics&sr=1-2'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup.prettify(), "html.parser")

    title = soup2.find(id="productTitle").get_text()

    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1] + price[3:6])

    if(converted_price<1300.0):
        send_mail()

    print(title.strip())
    print(converted_price)

def send_mail():
    server =smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    server.login('danleash911@gmail.com', 'trtvlaxthqkeuoye')
    subject = 'Item on sale! Item price fell to desired ammount.'
    body = 'Check the Amazon link https://www.amazon.com/EVGA-GeForce-Gaming-Graphics-11G-P4-2487-KR/dp/B07KVKRLG2/ref=sr_1_2?keywords=gtx+2080ti&qid=1571762672&s=electronics&sr=1-2'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'danleash911@gmail.com',
        'dan.leash0596@gmail.com',
        msg
        )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()



check_price()


