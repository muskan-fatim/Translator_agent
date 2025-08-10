
# 🌐✨ Targeted Translator Agent

> **Your personal smart translator** — Just tell it *"Convert in Urdu: How are you?"* and boom 💥 — it speaks your desired language instantly!

---

## 🚀 Features

✅ **Natural Language Understanding** — Understands your *target language* from your message.  
✅ **Precise Translation** — Only translates the sentence you want, nothing extra.  
✅ **Super Simple Input** — Just follow the format:  
```

Convert in <target-language>: <sentence>

```
✅ **Clean Output** — No headings, no fluff, just the translated line.  
✅ **Fun & Interactive UI** — Powered by **Chainlit** for a chat-like experience.

---

## 🎯 Example

**User Input:**
```

Convert in Urdu: How are you?

```

**Bot Output:**
```

آپ کیسے ہیں؟

````

💡 *Yes, it’s that easy!*

---

## 🛠 Tech Stack

| Tech | Usage |
|------|-------|
| 🐍 **Python** | Core programming |
| 🤖 **Custom Agent** | Smart translation logic |
| 💬 **Chainlit** | Interactive chat UI |
| ⚙ **Runner + Config** | Orchestrates agent execution |

---

## 📦 Installation & Setup

1️⃣ **Clone the Repo**
```bash
git clone https://github.com/your-username/translator-agent.git
cd translator-agent
````

2️⃣ **Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

3️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

4️⃣ **Configure API Keys & Settings**

* Open `config.py` and add your keys/configurations.

5️⃣ **Run the App**

```bash
chainlit run app.py
```

---

## 💻 How It Works

1. **User Sends Message** → `"Convert in Urdu: How are you?"`
2. **Agent Reads Target Language** → `Urdu`
3. **Agent Translates** only the sentence part after the colon (`How are you?`).
4. **Chainlit Displays** → `آپ کیسے ہیں؟`

---



## 🧠 Pro Tips

* 📝 Always use the format:

  ```
  Convert in <language>: <your sentence>
  ```
* 🌍 Works with **Urdu, English, Roman Urdu** (and more if you add support).
* 🎨 You can customize the bot’s welcome message in the `@cl.on_chat_start` function.

---



### 💖 Support

If you like this project, **give it a star ⭐ on GitHub** and share it with your friends!

---

> Made with ❤️ and ☕ by **[shagufta Zakir](https://github.com/Umar-30)**

```

