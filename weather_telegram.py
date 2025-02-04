import os
import requests
import datetime
from dotenv import load_dotenv
from telegram import Bot

# Load environment variables
load_dotenv()

# OpenWeather API details
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
LATITUDE = "-37.8136"  # Melbourne latitude
LONGITUDE = "144.9631"  # Melbourne longitude
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Fetch weather forecast
def get_weather_report(hour):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={LATITUDE}&lon={LONGITUDE}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    # Find the closest forecast for the requested hour (8 AM or 6 PM)
    best_match = None
    min_difference = float("inf")

    for forecast in data["list"]:
        forecast_time = datetime.datetime.utcfromtimestamp(forecast["dt"]) + datetime.timedelta(hours=11)  # Convert to Melbourne time
        forecast_hour = forecast_time.hour

        # Find the closest available time (since OpenWeather provides 3-hour intervals)
        difference = abs(forecast_hour - hour)
        if difference < min_difference:
            min_difference = difference
            best_match = forecast

    if best_match:
        weather_report = (
            f"🌤️ **Melbourne Weather Report**\n"
            f"📅 {forecast_time.strftime('%A, %d %B %Y %I:%M %p')}\n"
            f"🌡️ Temperature: {best_match['main']['temp']}°C\n"
            f"💧 Humidity: {best_match['main']['humidity']}%\n"
            f"🌬️ Wind Speed: {best_match['wind']['speed']} m/s\n"
            f"🌥️ Condition: {best_match['weather'][0]['description'].capitalize()}\n"
        )
        return weather_report
    else:
        return "⚠️ Weather data is not available."

# Fetch weather alerts
def get_weather_alerts():
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={LATITUDE}&lon={LONGITUDE}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if "alerts" in data:
        alerts = data["alerts"]
        alert_messages = "\n".join([f"⚠️ {alert['event']}: {alert['description']}" for alert in alerts])
        return alert_messages
    return None

# Send Telegram message
def send_telegram_message(message):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, parse_mode="Markdown")

# Main function
def main():
    now = datetime.datetime.now()
    hour = now.hour

    if hour == 8 or hour == 18:
        weather_report = get_weather_report(hour)
        weather_alerts = get_weather_alerts()

        final_message = weather_report
        if weather_alerts:
            final_message += f"\n\n🚨 *Weather Alerts:*\n{weather_alerts}"

        send_telegram_message(final_message)

if __name__ == "__main__":
    main()
