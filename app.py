import os
from flask import Flask, request, jsonify, send_from_directory
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

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
După ce confirmi programarea, adaugă întotdeauna: "⭐ Dacă ești mulțumită de serviciile noastre, ne-ar face plăcere să lași un review pe Google: https://g.page/r/bella-lux-review" """

conversations = {}

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        session_id = data.get("session_id", "default")
        user_message = data.get("message", "").strip()
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
        conversations[session_id].append({"role": "assistant", "content": reply})
        return jsonify({"reply": reply})
    except Exception as e:
        print(f"Eroare: {e}")
        return jsonify({"error": "Eroare tehnică. Încearcă din nou!"}), 500

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)