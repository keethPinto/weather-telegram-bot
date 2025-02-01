# 🌤️ Weather Telegram Bot 📩

This Python bot fetches **daily weather updates** for Melbourne and sends **morning & evening reports** to Telegram.

## 📌 Features
✅ Fetches **daily 8 AM & 6 PM** weather reports  
✅ Sends messages to a **Telegram chat**  
✅ 🔒 **Secure API keys** using `.env`  
✅ 🏠 **Runs on Raspberry Pi 4** with Ubuntu Server  
✅ Automates with a **Cron Job**  

---

## 🚀 **Step-by-Step Installation**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/keethPinto/weather-telegram-bot.git
cd weather-telegram-bot
```

### **2️⃣ Create a Virtual Environment**
```sh
python3 -m venv myenv
source myenv/bin/activate  # Activate the virtual environment
```

### **3️⃣ Install Required Python Packages**
```sh
pip install -r requirements.txt
```

🔹 **Required Packages** (already in `requirements.txt`):
```
requests
python-telegram-bot
python-dotenv
```

---

## 🔐 **4️⃣ Setup API Keys (Securely)**
### **Create a `.env` File**
Run:
```sh
nano .env
```
**Paste this inside**:
```
WEATHER_API_KEY=your_openweather_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```
🔹 **Replace `your_openweather_api_key`, `your_telegram_bot_token`, and `your_chat_id`** with actual values.  
🔹 **Do NOT share your `.env` file or push it to GitHub!**  

---

## ▶️ **5️⃣ Run the Bot**
Test if everything works by running:
```sh
python weather_telegram.py
```
✅ You should receive a **Telegram message** with the weather forecast.

---

## ⏳ **6️⃣ Automate with a Cron Job (Linux)**
To schedule the bot **twice daily at 8 AM & 6 PM**, run:
```sh
crontab -e
```
🔹 **Add these lines** at the bottom:
```
0 8 * * * /home/paios/myenv/bin/python /home/paios/weather_app/weather_telegram.py
0 18 * * * /home/paios/myenv/bin/python /home/paios/weather_app/weather_telegram.py
```
🔹 **Save & exit** (`CTRL+X`, then `Y`, then `Enter`).  
🔹 This ensures **automatic weather updates** every day! 🚀  

---

## 🛠️ **7️⃣ Troubleshooting**
### **Check If the Bot Is Running**
```sh
ps aux | grep python
```
### **Check Cron Logs**
```sh
cat /var/log/syslog | grep CRON
```
### **Manually Run the Script for Debugging**
```sh
python weather_telegram.py
```

---

## 📜 License
Feel free to **use, modify, and contribute** to this project. 🚀  
