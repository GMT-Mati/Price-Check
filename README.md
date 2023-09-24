```markdown
# Price Monitoring Script

This Python script monitors the price of a product on a selected internet store and sends an email notification if the price drops below a specified threshold.

## Requirements

- Python 3
- `requests` library
- `BeautifulSoup` library
- SMTP email account (Gmail in this example)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/price-monitor.git
   ```

2. Install the required Python libraries:

   ```bash
   pip install requests beautifulsoup4
   ```

## Configuration

1. Open the `price_monitor.py` file and update the following variables:

   - `product_url`: URL of the product page you want to monitor.
   - `target_price`: Price threshold below which you want to be notified.
   - `sender_email`: Your email address for sending notifications.
   - `sender_password`: Your email account password.
   - `receiver_email`: Recipient's email address.

2. Make sure your Python script is executable:

   ```bash
   chmod +x price_monitor.py
   ```

## Usage

To run the script manually, execute the following command:

```bash
./price_monitor.py
```

## Running Automatically on Startup (Linux)

To run the script automatically when your computer starts, follow these steps:

1. Create a systemd service unit file:

   ```bash
   sudo nano /etc/systemd/system/price_monitor.service
   ```

2. Add the following content to the `price_monitor.service` file:

   ```ini
   [Unit]
   Description=Price Monitor Service

   [Service]
   ExecStart=/usr/bin/python3 /path/to/your/price_monitor.py
   Restart=always
   User=your_username
   WorkingDirectory=/path/to/your/script/directory

   [Install]
   WantedBy=multi-user.target
   ```

   Replace `/path/to/your/price_monitor.py` with the actual path to your Python script and `your_username` with your Linux username.

3. Save the file and exit the text editor.

4. Reload the systemd manager configuration:

   ```bash
   sudo systemctl daemon-reload
   ```

5. Enable the service to start on boot:

   ```bash
   sudo systemctl enable price_monitor.service
   ```

6. Start the service:

   ```bash
   sudo systemctl start price_monitor.service
   ```

You can check the status of your service with:

```bash
sudo systemctl status price_monitor.service
```

If you need to stop or restart the service, you can use the `systemctl` commands as well.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
