import requests
from bs4 import BeautifulSoup
import smtplib

def send_email(items):
    # Set up your email configuration
    sender_email = "your_mail@gmail.com"
    sender_password = "password"
    recipient_email = "example_email@gmail.com"

    subject = "Price Alert"
    message = "\n".join(items)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        email_text = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, recipient_email, email_text)
        print("Email notification sent successfully!")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))
    finally:
        server.quit()

def price_check(URLs, headers):
    items_to_notify = []

    for URL, price_threshold in URLs:
        try:
            page = requests.get(URL, headers=headers)
            soup = BeautifulSoup(page.content, "html.parser")
            
            if "notino" in URL:
                price_element = soup.find(id="pd-price")
                if price_element:
                    price = price_element.get_text()
                    # Extract numerical value from the price string
                    price_value = float("".join(filter(str.isdigit, price[0:3])))
                    if price_value < price_threshold:
                        items_to_notify.append(f"Item: {URL}\nPrice: {price_value}")
                    print("Price:", price_value)
                else:
                    print("Price not found on the page.")
            
            elif "euro.com.pl" in URL:
                price_element = soup.find("span", class_="price-template__default--amount")
                if price_element:
                    price = price_element.get_text().strip()
                    # Remove currency symbols or spaces, if present
                    price_value = float("".join(filter(str.isdigit, price)))
                    if price_value < price_threshold:
                        items_to_notify.append(f"Item: {URL}\nPrice: {price_value}")
                    print("Price:", price_value)
                else:
                    print("Price not found on the page.")
        except Exception as e:
            print("An error occurred:", str(e))
    
    if items_to_notify:
        send_email(items_to_notify)

# Example usage:
# you can replace  url adress with any adress from www.notino.pl and www.euro.com.pl, also you can change price for any value you want
URLs = [
    ("https://www.notino.pl/azzaro/chrome-woda-toaletowa-dla-mczyzn/p-59969/", 300),
    ("https://www.notino.pl/guerlain/aqua-allegoria-pera-granita-woda-toaletowa-dla-kobiet/", 400),
    ("https://www.euro.com.pl/odkurzacze-automatyczne/roborock-s8-czarny-mopowanie.bhtml?cd=191780169&ad=10070947089&kd=&gclid=EAIaIQobChMI3o7gg7XAgQMV2OyyCh0vZQ5aEAQYBCABEgLcOvD_BwE&gclsrc=aw.ds", 2500),
    ("https://www.euro.com.pl/odkurzacze-automatyczne/roborock-q7-max-bialy.bhtml?&cd=191780169&ad=10070947089&kd=&gclid=Cj0KCQjwvL-oBhCxARIsAHkOiu0R-ybG2gKqgA2JwP9MWxqIoeNi60vhT709nlSer7e6CMqssst_084aAmyKEALw_wcB&gclsrc=aw.ds", 2000)
]

headers = {"User-Agent": "Your User Agent"}
price_check(URLs, headers)
