import os
import json
import gspread
from google.oauth2.service_account import Credentials
from flask import Flask, request, jsonify, send_from_directory
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Google Sheets setup
def get_sheet():
    try:
creds_path = "/etc/secrets/credentials.json" if os.path.exists("/etc/secrets/credentials.json") else "credentials.json"
creds = Credentials.from_service_account_file(creds_path, scopes=[
            creds_dict = json.loads(creds_json)
            creds = Credentials.from_service_account_info(creds_dict, scopes=[
                "https://spreadsheets.google.com/feeds",
                "https://www.googleapis.com/auth/drive"
            ])
        else:
            creds = Credentials.from_service_account_file("credentials.json", scopes=[
                "https://spreadsheets.google.com/feeds",
                "https://www.googleapis.com/auth/drive"
            ])
        gc = gspread.authorize(creds)
        sheet_id = os.environ.get("GOOGLE_SHEET_ID")
        return gc.open_by_key(sheet_id).sheet1
    except Exception as e:
        print(f"Sheet error: {e}")
        return None

def save_booking(nume, telefon, serviciu, data, ora, limba="RO"):
    try:
        sheet = get_sheet()
        if sheet:
            sheet.append_row([nume, telefon, serviciu, data, ora, limba])
            print(f"Programare salvată: {nume} {data} {ora}")
    except Exception as e:
        print(f"Eroare salvare: {e}")

SYSTEM_PROMPT = """Ești Sophia, asistenta virtuală a cabinetului cosmetic Bella Lux Beauty Studio.
Ești prietenoasă, profesională și entuziastă despre beauty.
Răspunzi ÎNTOTDEAUNA în română (sau engleză dacă clienta scrie în engleză).

PROGRAM: Luni-Vineri 09-20, Sâmbătă 09-18, Duminică 10-16
TELEFON: 0744261906

SERVICII:
- Manichiură simplă: 40 lei
- Manichiură semipermanentă: 80 lei
- Pedichiură simplă: 60 lei
- Epilat axile: 30 lei
- Epilat picioare integral: 80 lei
- Curățare facială: 120 lei
- Masaj relaxant 60min: 150 lei

Când cineva vrea programare, colectează: nume, telefon, serviciu, dată, oră.
După ce confirmi programarea, adaugă întotdeauna: "⭐ Dacă ești mulțumită de serviciile noastre, ne-ar face plăcere să lași un review pe Google: https://g.page/r/bella-lux-review"

IMPORTANT: Când confirmi o programare, include în răspuns un bloc JSON astfel:
BOOKING_DATA:{"nume":"...","telefon":"...","serviciu":"...","data":"...","ora":"..."}"""

conversations = {}

def extract_booking(text):
    try:
        if "BOOKING_DATA:" in text:
            start = text.index("BOOKING_DATA:") + len("BOOKING_DATA:")
            json_str = text[start:].split("\n")[0].strip()
            return json.loads(json_str)
    except:
        pass
    return None

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        session_id = data.get("session_id", "default")
        user_message = data.get("message", "").strip()
        limba = data.get("limba", "RO")
        if not user_message:
            return jsonify({"error": "Mesaj gol"}), 400
        if session_id not in conversations:
            conversations[session_id] = []
        conversations[session_id].append({"role": "user", "content": user_message})
        history = conversations[session_id][-20:]
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}, *history],
            temperature=0.7,
            max_tokens=1024,
        )
        reply = response.choices[0].message.content

        # Salvează programarea dacă există
        booking = extract_booking(reply)
        if booking:
            save_booking(
                booking.get("nume", ""),
                booking.get("telefon", ""),
                booking.get("serviciu", ""),
                booking.get("data", ""),
                booking.get("ora", ""),
                limba
            )
            # Elimină JSON-ul din răspunsul afișat
            reply = reply[:reply.index("BOOKING_DATA:")].strip()

        conversations[session_id].append({"role": "assistant", "content": reply})
        return jsonify({"reply": reply})
    except Exception as e:
        print(f"Eroare: {e}")
        return jsonify({"error": "Eroare tehnică. Încearcă din nou!"}), 500

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/programari")
def programari():
    try:
        sheet = get_sheet()
        if not sheet:
            return jsonify({"error": "Nu pot accesa sheet-ul"}), 500
        rows = sheet.get_all_records()
        return jsonify({"programari": rows})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)