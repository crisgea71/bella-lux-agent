# Bella Lux AI Agent – Beauty Salon Booking Assistant

An AI-powered assistant that helps beauty salons answer client questions, explain services, collect bookings, and request reviews — in Romanian and English.

🔗 **Live Demo:** https://bella-lux-agent-1.onrender.com

> ⚡ First load may take around 30 seconds because the demo is hosted on Render free tier and may wake up on demand.

---

## Why This Exists

Beauty salons often lose time every day answering the same repetitive questions across phone, WhatsApp, Instagram, and direct messages:

- “What services do you offer?”
- “How much does a manicure cost?”
- “Can I book for Saturday?”
- “Where is the salon located?”
- “Do you speak Romanian or English?”

**Sophia**, the salon’s AI assistant, handles these conversations automatically — 24/7.

The goal of this project is to show how a small local business can use an AI assistant to save time, respond faster, and create a smoother booking experience for clients.

---

## What Sophia Can Do

- Answer questions about salon services and prices
- Help clients choose the right service
- Take booking requests with an interactive calendar
- Switch between Romanian and English
- Show the salon location on a map
- Ask clients for a Google review after booking
- Provide a simple message-limit system for demo/testing purposes

---

## Who This Is For

This demo is designed for:

- beauty salons
- nail studios
- lash and brow studios
- hair salons
- skincare studios
- small local service businesses
- appointment-based businesses that receive repetitive client questions

---

## Business Value

Sophia helps a salon reduce repetitive manual communication and respond to clients faster.

| Task | Before | After |
|------|--------|-------|
| Answering repetitive questions | 60–90 min/day | Handled by AI |
| Booking requests | Manual replies | Assisted flow |
| After-hours messages | Often missed | 24/7 response |
| Review requests | Manual follow-up | Automatic prompt |
| Language support | Depends on staff | Romanian + English |

A small salon could save several hours per week by automating common client conversations.

---

## Main Features

### AI Client Assistant

Sophia responds naturally to client questions about services, prices, appointments, and salon information.

### Booking Support

Clients can request appointments through a simple booking flow using an interactive calendar.

### Romanian & English Support

The assistant can communicate in both Romanian and English, making it useful for local and international clients.

### Review Request Flow

After a booking interaction, the assistant can ask the client to leave a Google review.

### Demo Message Limit

The app includes a basic message-limit system, useful for testing a “free trial” or demo experience.

---

## Tech Stack

- **Backend:** Python, Flask
- **AI Model:** Groq API / Llama 3.3 70B
- **Frontend:** HTML, CSS, JavaScript
- **Hosting:** Render
- **Environment Variables:** Python dotenv

---

## Project Structure

```bash
bella-lux-agent/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── README.md
*Built with Claude AI + Groq API*
