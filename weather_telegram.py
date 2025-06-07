import os
import requests
<<<<<<< HEAD
import json
import logging
from dotenv import load_dotenv
from datetime import datetime
import pytz

# Configure logging
LOG_FILE = "/home/paios/weather_app/weather_log.txt"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load environment variables
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "South Morang"
COUNTRY = "AU"
TIMEZONE = "Australia/Melbourne"

# Check if any variable is missing
if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID or not OPENWEATHER_API_KEY:
    logging.error("Missing environment variables. Exiting script.")
    exit(1)

def get_weather_report(target_hour):
    """Fetch weather data for the specified hour, with ±1 hour tolerance."""
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY},{COUNTRY}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        logging.error(f"Failed to fetch weather data. Status Code: {response.status_code}")
        return None

    data = response.json()

    if "list" not in data:
        logging.error("Invalid response structure from OpenWeather API.")
        return None

    tz = pytz.timezone(TIMEZONE)

    for forecast in data["list"]:
        dt = datetime.fromtimestamp(forecast["dt"], tz)
        hour = dt.hour

        if abs(hour - target_hour) <= 1:
            temperature = forecast["main"]["temp"]
            humidity = forecast["main"]["humidity"]
            wind_speed = forecast["wind"]["speed"]
            condition = forecast["weather"][0]["description"].capitalize()

            weather_warning = ""
            if "alerts" in data:
                weather_warning = f"\n⚠️ **Weather Warning:** {data['alerts'][0]['event']}"

            report = (
                f"🌤️ **{CITY} Weather Report**\n"
                f"📅 {dt.strftime('%A, %d %B %Y %I:%M %p')}\n"
                f"🌡️ Temperature: {temperature}°C\n"
                f"💧 Humidity: {humidity}%\n"
                f"🌬️ Wind Speed: {wind_speed} m/s\n"
                f"🌥️ Condition: {condition}{weather_warning}"
            )

            logging.info("Weather report generated successfully.")
            return report

    logging.warning("No matching forecast found for target hour.")
    return None

def send_telegram_message(message):
    """Send a message to Telegram."""
    if not message:
        logging.warning("No message to send. Skipping Telegram notification.")
        return False

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        logging.info("Weather report sent successfully to Telegram.")
        return True
    else:
        logging.error(f"Failed to send message to Telegram. Status Code: {response.status_code}")
        return False

def main():
    """Main function to send weather updates at 08:00 AM and 06:00 PM."""
    logging.info("Weather script started.")

    now = datetime.now(pytz.timezone(TIMEZONE))
    hour = now.hour

    if hour == 8:
        target_hour = 8
    elif hour == 18:
        target_hour = 18  # Now that DST is over, 6 PM = 18:00 is accurate
    else:
        logging.warning(f"Script executed at {hour}:00, but it's not a scheduled time.")
        exit(1)

    weather_report = get_weather_report(target_hour)

    if weather_report:
        send_telegram_message(weather_report)

if __name__ == "__main__":
    main()

=======
>>>>>>> 720694830a1b1e6cd706a99e24b4ccebde2b700b
