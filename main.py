import requests
from bs4 import BeautifulSoup
import smtplib


URL = "https://www.notino.pl/lancome/lancome-idole-woda-perfumowana-dla-kobiet/p-15966662/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                         "(XHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.53"}


class PriceCheck:

    def __init__(self):
        self.URL = URL

    @staticmethod
    def price_check():
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        price = soup.find(id="pd-price").get_text()
        converted_price = float(price[0:3])
        if converted_price < 200:
            send_mail()
        else:
            print("Email hasn't sent")

    @staticmethod
    def send_mail():
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("matt_____@gmail.com", "_____")  # your mail address and password
        subject = "Price fell down!"
        body = f"Check link! {URL}"
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(
            "matt_____@gmail.com",  # your email address
            "gmait_____@gmail.com",  # mail recipient
            msg)
        print("Email has been sent!")
        server.quit()


PriceCheck.send_mail()
