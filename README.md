# 🌸 Bella Lux Beauty Studio – AI Agent

Sophia este asistenta virtuală AI a cabinetului cosmetic **Bella Lux Beauty Studio**. Răspunde în română și engleză, oferă informații despre servicii și prețuri, și preia programări direct din chat.

🔗 **Live demo:** https://bella-lux-agent-1.onrender.com

---

## ✨ Features

- 💬 Chat AI în timp real (română & engleză)
- 📅 Calendar interactiv pentru programări
- 💅 Informații despre servicii și prețuri
- 📍 Hartă cu locația salonului
- ⭐ Review request automat după programare
- 📱 Responsive — funcționează pe mobil și desktop

## 🛠 Tech Stack

- **Backend:** Python + Flask
- **AI:** Groq API (Llama 3.3 70B)
- **Frontend:** HTML / CSS / JavaScript
- **Hosting:** Render.com

## 🚀 Rulare locală

```bash
git clone https://github.com/crisgea71/bella-lux-agent.git
cd bella-lux-agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # adaugă GROQ_API_KEY
python3 app.py
```

## 🔐 Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Cheia API de la console.groq.com |

---

*Built with AI assistance (Claude AI) using Groq API* 🌸