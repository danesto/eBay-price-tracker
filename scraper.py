import requests
from bs4 import BeautifulSoup
import smtplib
from colorama import *
init()
import time

URL=input('Enter eBay URL: ')
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
to_mail=input('Enter your e-mail: ')
def check_price():
    page=requests.get(URL, headers=headers)
    soup=BeautifulSoup(page.text, 'html.parser')

    # title=soup.find(id="productTitle").get_text().strip()
    price=soup.find("h2", class_="display-price").get_text().strip()

    converted_price=float(price[1:7])
    # print(converted_price)

    desired_price=input('Under what price you want it to drop? ')

    new_price=float(desired_price)
    # print(new_price)

    if (converted_price<=new_price):
        send_mail()
    else:
        print(Fore.RED + 'Price did not drop! Checking on every 12 hours! ' + Fore.LIGHTYELLOW_EX + 'Current price is: ' + str(converted_price) + ' hljada eura')
    
    while(converted_price>new_price):
        time.sleep(21600)
        check_price()

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('dane.sto@gmail.com','fkpblyybpcnmuqin')
    to_mail

    subject='Price droped!'
    body=f'Check the link {URL}'
    msg=f'Subject {subject}\n\n{body}'

    server.sendmail(
        'dane.sto@gmail.com',
        to_mail,
        msg
    )

    print(Fore.BLUE + 'Price has fallen down, check your e-mail!')
    server.quit()

check_price()
