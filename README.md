🌤️ Weather Telegram Bot 📩
This Python bot fetches daily weather updates for South Morang (Melbourne area) and sends morning & evening reports to Telegram.

📌 Features
✅ Fetches daily 8 AM & 6 PM weather reports
✅ Sends messages to a Telegram chat
✅ 🔒 Secure API keys using .env
✅ 🏠 Runs on Raspberry Pi 4 with Ubuntu Server
✅ Automates with a Cron Job
✅ DST-safe: handles daylight saving changes (±1 hour logic)

🚀 Step-by-Step Installation
1️⃣ Clone the Repository
sh
Copy
git clone https://github.com/keethPinto/weather-telegram-bot.git
cd weather-telegram-bot
2️⃣ Create a Virtual Environment
sh
Copy
python3 -m venv myenv
source myenv/bin/activate  # Activate the virtual environment
3️⃣ Install Required Python Packages
sh
Copy
pip install -r requirements.txt
Required Packages (already in requirements.txt):

nginx
Copy
requests
python-dotenv
pytz
🔐 Setup API Keys (Securely)
Create a .env File
sh
Copy
nano .env
Paste this inside:

env
Copy
OPENWEATHER_API_KEY=your_openweather_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
✅ Replace your_openweather_api_key, your_telegram_bot_token, and your_chat_id with your actual values.
❌ Do NOT share your .env file or push it to GitHub!

▶️ Run the Bot
Test if everything works by running:

sh
Copy
python weather_telegram.py
✅ You should receive a Telegram message with the weather forecast.

⏳ Automate with a Cron Job (Linux)
To schedule the bot twice daily at 8 AM & 6 PM, run:

sh
Copy
crontab -e
Add these lines at the bottom:

cron
Copy
0 8 * * * /home/paios/myenv/bin/python /home/paios/weather_app/weather_telegram.py >> /home/paios/weather_app/weather_log.txt 2>&1
0 18 * * * /home/paios/myenv/bin/python /home/paios/weather_app/weather_telegram.py >> /home/paios/weather_app/weather_log.txt 2>&1
✅ Save & exit (CTRL+X, then Y, then Enter).
✅ This ensures automatic weather updates every day!

🛠️ Troubleshooting
Check If the Bot Is Running
sh
Copy
ps aux | grep python
Check Cron Logs
sh
Copy
cat /var/log/syslog | grep CRON
Manually Run the Script for Debugging
sh
Copy
python weather_telegram.py
Check Bot Logs
sh
Copy
cat /home/paios/weather_app/weather_log.txt
🖥️ Example Output
When the bot runs (via cron or manually), the Telegram message will look like:

yaml
Copy
🌤️ South Morang Weather Report
📅 Monday, 15 April 2025 08:00 AM
🌡️ Temperature: 19.5°C
💧 Humidity: 78%
🌬️ Wind Speed: 4.2 m/s
🌥️ Condition: Broken Clouds
If there is a weather warning:

yaml
Copy
🌤️ South Morang Weather Report
📅 Monday, 15 April 2025 06:00 PM
🌡️ Temperature: 17.8°C
💧 Humidity: 85%
🌬️ Wind Speed: 6.1 m/s
🌥️ Condition: Light Rain

🚨 Weather Warning:
⚠️ Severe Thunderstorm Warning
✅ Automatic daily reports at 8 AM and 6 PM
✅ Handles Daylight Saving changes automatically (±1 hour tolerance)
✅ Sends directly to your Telegram chat

📜 License
Feel free to use, modify, and contribute to this project. 🚀
