# 🌸 Bella Lux Beauty Studio – AI Agent

Sophia is the virtual AI assistant for **Bella Lux Beauty Studio** cosmetic salon. She responds in Romanian and English, provides information about services and prices, and accepts bookings directly from the chat.

🔗 **Live demo:** https://bella-lux-agent-1.onrender.com

---

## ✨ Features

- 💬 Real-time AI chat (Romanian & English)
- 📅 Interactive calendar for bookings
- 💅 Services and pricing information
- 📍 Map with salon location
- ⭐ Automatic review request after booking
- 📱 Responsive — works on mobile and desktop

## 🛠 Tech Stack

- **Backend:** Python + Flask
- **AI Model:** Groq API (Llama 3.3 70B)
- **Frontend:** HTML / CSS / JavaScript
- **Hosting:** Render.com (free tier)

## 🚀 Run Locally

```bash
git clone https://github.com/crisgea71/bella-lux-agent.git
cd bella-lux-agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # add your GROQ_API_KEY
python3 app.py
```

Open your browser at `http://localhost:5001`

## 🔐 Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your API key from console.groq.com |

## 📸 Screenshots

> *(Add screenshots after deployment)*

---

*Built with AI assistance (Claude AI) using Groq API* 🌸