```markdown
# Price Checker

This Python program is designed to monitor the prices of specific items on e-commerce websites and send email notifications when the prices fall below predefined thresholds. It uses web scraping techniques to extract price information from the websites and sends email alerts if the conditions are met.

## Prerequisites

Before running the program, ensure you have the following:

- Python installed on your system.
- The required Python packages installed:
  - `requests`
  - `beautifulsoup4`

You can install these packages using pip:

```bash
pip install requests beautifulsoup4
```

## Configuration

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/price-checker.git
cd price-checker
```

2. Open the `config.py` file in the project directory and configure it with your email credentials and the URLs you want to monitor, along with their respective price thresholds.

```python
# config.py

# Email Configuration
sender_email = "your_email@gmail.com"
sender_password = "your_email_password"
recipient_email = "recipient_email@gmail.com"

# User-Agent for HTTP requests (you can leave this as is)
user_agent = "Your User Agent"

# URLs to monitor with their respective price thresholds
urls = [
    ("https://www.notino.pl/azzaro/chrome-woda-toaletowa-dla-mczyzn/p-59969/", 300),
    ("https://www.notino.pl/guerlain/aqua-allegoria-pera-granita-woda-toaletowa-dla-kobiet/", 400),
    ("https://www.euro.com.pl/odkurzacze-automatyczne/roborock-s8-czarny-mopowanie.bhtml?cd=191780169&ad=10070947089&kd=&gclid=EAIaIQobChMI3o7gg7XAgQMV2OyyCh0vZQ5aEAQYBCABEgLcOvD_BwE&gclsrc=aw.ds", 2500),
    ("https://www.euro.com.pl/odkurzacze-automatyczne/roborock-q7-max-bialy.bhtml?&cd=191780169&ad=10070947089&kd=&gclid=Cj0KCQjwvL-oBhCxARIsAHkOiu0R-ybG2gKqgA2JwP9MWxqIoeNi60vhT709nlSer7e6CMqssst_084aAmyKEALw_wcB&gclsrc=aw.ds", 2000)
]
```

Ensure that you provide your email credentials and URLs with the appropriate price thresholds in the `config.py` file.

## Running the Program

You can manually run the program using the following command:

```bash
python price_checker.py
```

## Scheduling Daily Checks (Linux)

To schedule the program to run daily at a specific time on a Linux machine, you can use `cron`. Follow these steps:

1. Open your crontab configuration:

```bash
crontab -e
```

2. Add an entry to run the program daily at your desired time. For example, to run the program every day at 9:00 AM, add the following line to your crontab:

```bash
0 9 * * * /usr/bin/python3 /path/to/price_checker.py
```

Replace `/path/to/price_checker.py` with the actual path to your `price_checker.py` script.

3. Save and exit the crontab editor.

The program will now run daily at the specified time, checking the prices and sending email notifications when necessary.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
