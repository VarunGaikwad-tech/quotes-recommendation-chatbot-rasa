# 💬 Quotes Recommendation Chatbot

> An intelligent conversational system built with **Rasa NLU** that delivers motivational, inspirational, love, success, and humorous quotes through natural language conversations.

---

## Overview

In today's fast-paced world, people often seek quick motivation or emotional encouragement. This chatbot solves that by delivering meaningful quotes instantly through a natural conversation — no searching required.

The system understands user intent using **Natural Language Processing (NLP)** and responds with relevant quotes across multiple categories. It also includes a **web interface** so users can interact through a browser instead of the command line.

---

## Features

- 🧠 Intent recognition using **Rasa NLU**
- 📚 Quote categories: Motivation, Inspiration, Love, Success, Funny
- 🌐 Web-based chat interface
- ⚡ Real-time REST API responses
- 🔌 Easy local setup

---

## Tech Stack

| Layer | Technology |
|---|---|
| NLP Engine | Rasa NLU |
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| API | REST |

---

## Prerequisites

Before getting started, make sure you have:

- **Python 3.9** (Rasa requires this specific version)
- **pip** (Python package manager)
- A terminal / command prompt

---

## Project Structure

```
quoteChatbot/
│
├── actions/
│   ├── actions.py
│   └── __init__.py
│
├── data/
│   ├── nlu.yml
│   ├── rules.yml
│   └── stories.yml
│
├── tests/
│   └── test_stories.yml
│
├── webapp/
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── config.yml
├── credentials.yml
├── domain.yml
├── endpoints.yml
├── requirements.txt
├── commands.txt          # Quick reference for common CLI commands
└── README.md
```

---

## Installation & Setup

### Step 1 — Create a Virtual Environment

```bash
py -3.9 -m venv venv
```

Activate the environment:

```bash
# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

---

### Step 2 — Install Dependencies

Upgrade pip first:

```bash
python -m pip install --upgrade pip
```

Install Rasa:

```bash
pip install rasa=3.6.21
```

---

### Step 3 — Train the Model

```bash
rasa train
```

---

## Running the Project

You'll need **two terminals** open simultaneously.

### Terminal 1 — Start the Rasa Server

```bash
rasa run --enable-api --cors "*"
```

### Terminal 2 — Start the Web App

```bash
cd webapp
python app.py
```

### Open the Chatbot

Navigate to:

```
http://127.0.0.1:5000
```

---

## Example Interaction

```
User: hi
Bot:  Hello! Please tell me which type of quote you want.

User: give me an inspirational quote
Bot:  "Believe you can and you're halfway there." – Theodore Roosevelt

User: yes
Bot:  Thanks for your feedback! If you want more quotes, tell me the category.
```

---

## Testing

Run automated model tests:

```bash
rasa test
```

Test interactively in the terminal:

```bash
rasa shell
```

---

## Future Improvements

- [ ] Integration with messaging platforms (WhatsApp, Telegram)
- [ ] More quote categories (mindfulness, leadership, etc.)
- [ ] Sentiment analysis for context-aware responses
- [ ] Voice interaction support

---

## Authors

**Team Project — SmartBridge EL Program**

- Vansh Malhotra
- Varun Gaikwad
- Vedika Tandulwadkar
- Vidisha Jain
