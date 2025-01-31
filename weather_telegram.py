import os
import requests
import asyncio
from telegram import Bot
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv  # Load API keys securely

# Load API keys from .env file
load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # Your Telegram user ID

CITY = "Melbourne"
WEATHER_URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={WEATHER_API_KEY}&units=metric"

def get_weather(target_hour):
    """Fetch the closest available weather forecast for the target hour (8 AM or 6 PM)."""
    try:
        response = requests.get(WEATHER_URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        closest_forecast = None
        closest_time_diff = float("inf")

        for forecast in data["list"]:
            forecast_time = datetime.fromtimestamp(forecast["dt"], timezone.utc) + timedelta(hours=11)  # Convert to Melbourne time
            time_diff = abs(forecast_time.hour - target_hour)

            # Choose the closest time (max 2-hour difference)
            if time_diff <= 2 and time_diff < closest_time_diff:
                closest_forecast = forecast
                closest_time_diff = time_diff

        if closest_forecast:
            forecast_time = datetime.fromtimestamp(closest_forecast["dt"], timezone.utc) + timedelta(hours=11)
            weather_desc = closest_forecast["weather"][0]["description"].capitalize()
            temp = closest_forecast["main"]["temp"]
            humidity = closest_forecast["main"]["humidity"]
            wind_speed = closest_forecast["wind"]["speed"]

            return (
                f"🌤️ **Melbourne Weather Report**\n"
                f"📅 {forecast_time.strftime('%A, %d %B %Y %I:%M %p')}\n"
                f"🌡️ Temperature: {temp}°C\n"
                f"💧 Humidity: {humidity}%\n"
                f"🌬️ Wind Speed: {wind_speed} m/s\n"
                f"🌥️ Condition: {weather_desc}"
            )

        return f"⚠️ No weather data available near {target_hour}:00."

    except requests.exceptions.RequestException as e:
        return f"🚨 Weather API error: {e}"

async def send_telegram_message(target_hour):
    """Fetch weather and send an alert via Telegram bot."""
    weather_message = get_weather(target_hour)
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    
    try:
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=weather_message, parse_mode="Markdown")
        print(f"✅ Telegram message sent ({target_hour}:00): {weather_message}")
    except Exception as e:
        print(f"❌ Error sending Telegram message: {e}")

# Run async functions correctly
async def main():
    await send_telegram_message(8)   # Morning report
    await send_telegram_message(18)  # Evening report

if __name__ == "__main__":
    asyncio.run(main())
