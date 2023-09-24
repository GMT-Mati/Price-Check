import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Define the URL of the product page you want to monitor
product_url = "https://example.com/product"

# Set the price threshold below which you want to be notified
target_price = 100.00  # Change this to your desired price

# Email configuration (Gmail in this example)
sender_email = "youremail@gmail.com"
sender_password = "yourpassword"
receiver_email = "recipient@example.com"

# Function to send an email notification
def send_email(price, product_url):
    subject = "Price Alert"
    body = f"The price of the product is now ${price:.2f}.\n\nCheck it out here: {product_url}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, receiver_email, message)
        print("Email notification sent!")
        server.quit()
    except Exception as e:
        print("Error sending email:", str(e))

# Main function to check the price and send notifications
def monitor_price():
    while True:
        try:
            # Send a GET request to the product URL
            response = requests.get(product_url)

            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract the price from the page (you may need to inspect the webpage HTML)
            # Replace this with the appropriate code to extract the price
            current_price = float(soup.find("span", {"class": "product-price"}).text.replace("$", ""))

            # Check if the current price is lower than the target price
            if current_price < target_price:
                send_email(current_price, product_url)

            # Sleep for an hour (you can adjust the interval)
            time.sleep(3600)
        except Exception as e:
            print("Error:", str(e))

if __name__ == "__main__":
    monitor_price()
