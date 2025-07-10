# **Indian Railway Information System**

**Your Gateway to Real-time Railway Information with an Integrated AI System**

---

## 📌 Overview

Welcome to **Indian Railway Info Portal**, an all-in-one platform to get real-time Indian Railways data, smart AI travel assistance, station info, trip planning, and the latest railway news — all in a single place!

Built with 🧠 **LangChain**, **Groq API**, and **Streamlit**, this project combines reliable railway APIs with conversational AI to make your journey planning smart and effortless.

---

## ✨ Features

### 🔹 Rail Services

* 📍 **Station Info** — Provide information about station.
* 🚉 **Train Schedule** — Get accurate train timings for any route.
* 🚂 **All Trains from Station** — See which trains depart/arrive from a station.
* 💰 **Train Fares** — Check fare details for different classes.
* 🎫 **Seat Availability** — Check real-time seat availability.
* 🌟 **Special Trains** — Stay updated on festival/special trains.
* 💼 **Premium Trains** — Get details of premium and luxury trains.
* 🏎️ **Rajdhani & Superfast Trains** — Fast and convenient options with schedules.
* 🔢 **Station Name to Code / Train Number to Name** — Handy code/number lookups.

---

### 🤖 AI Services

* 🔍 **SmartTrain Finder** — Find trains for your trip using natural language (with via route suggestions).
* 🚂 **SmartTrain Assistant** — Ask anything about a specific train: history, route, punctuality, facilities.
* 🏢 **SmartStation Assistant** — Get deep insights about any station: history, facilities, nearby attractions.
* 🗺️ **Travel Planner Assistant** — Plan your entire trip: best time to visit, stay, things to do, how to reach.
* 🧩 **RailSaarthi: Smart FAQ Assistant** — Get answers to any general railway-related queries.

---

### 📰 Railway News

Stay informed with the **latest Indian Railway news**, complete with images!

---

## ⚙️ Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
  * LangChain Runnables: RunnableParallel, RunnableBranch
* **Groq API** (LLM for chat agents)
* **Pinecone** (for future RAG / Vector DB)
* **RAG Architecture**
---

## 🗃️ Project Structure

```
Indian_Railway_Information_System/
├── ai_services/
│   ├── RailSaarthi/
│   ├── smart_station_assistant/
│   ├── smart_train_assistant/
│   |── smart_train_finder/
|   ├── travel_planner_assistant/
├── scripts/
│   ├── feedback/
│   ├── news/
│   ├── station_code/
│   └── train_no_to_name/
├── src/
│   ├── schedule/
│   ├── seats/
│   ├── station_details/
│   ├── station_trains/
│   └── train_fares/
|   ├── trains/
|   │   ├── premium_trains/
|   │   ├── rajdhani_trains/
|   │   ├── special_trains/
|   │   └── super_fast_trains/
├── ui/
│   ├── __init__.py
│   ├── ai_service_ui.py
│   └── train_service_ui.py
├── utils/
│   ├── __init__.py
│   ├── custom_exception.py
│   ├── load_json.py
│   ├── load_yaml.py
│   ├── prompt_templates.py
│   └── session_helper.py
├── .env
├── .gitignore
├── app.py
├── config.yaml
├── indian_railway_faqs.json
├── README.md
└── requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file at the root with:

```
PINECONE_API_KEY=YOUR_PINECONE_API_KEY
GROQ_API_KEY=YOUR_GROQ_API_KEY
NEWS_API_KEY=YOUR_NEWS_API_KEY
API_KEY=YOUR_RAIL_API_KEY
```

---

## 🚀 Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/atharvmohanjadhav/Indian-Railway-Information-System.git
cd Indian-Railway-Information-System
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Create `.env`** and add your API keys.

4. **Run the app**

```bash
streamlit run app.py
```

---

## ⚡ Usage

* Use the UI to select a **Rail Service** or **AI Service**.
* Enter your **Groq API key** once; it stays active for your session.
* Interact with the smart assistants in a chat-like UI.
* Translate SmartTrain Finder responses into Hindi or Marathi with one click.
* Check **latest railway news** with images.
* Reset your API key anytime.

---

## 📬 Contact

> **Atharv Mohan Jadhav**

> 📧 [email](mailto:atharvjadhav2910@gmail.com)
> 🌐 [GitHub](https://github.com/atharvmohanjadhav)

---

