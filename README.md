# Day-4-Random-Quote-Generator

Project overview

Features

Setup instructions

Usage guidelines

File structure

Dependencies

Troubleshooting tips

Future improvements

# Multilingual AI Quote & Story Generator

A Streamlit-based web app allowing users to generate quotes and stories in multiple languages using AI.  
Includes user authentication, multilingual support, AI-generated character names, user activity tracking with Excel logging, and downloadable quote portfolios in TXT and DOCX formats.

---

## 🚀 Features

- **Multilingual support:** Choose from 50+ languages including Tamil, Hindi, English, Mandarin, Arabic, and more.
- **Diverse quote types:** Select from 25+ quote categories such as Motivational, Love, Wisdom, Spiritual, and Cultural quotes.
- **AI-generated content:** Generate unique quotes and multi-paragraph stories, optionally with AI-generated character names.
- **User login:** Simple session-based login with name and Gmail address validation.
- **User activity logging:** Tracks user interactions (name, email, language, topic, generated content, timestamp) in an Excel file (`users_data.xlsx`).
- **Download options:** Export currently generated quotes and stories as TXT or DOCX files personalized with the user's name.
- **Recent quotes:** View your recent quotes filtered by selected language.
- **Clean UI:** Responsive interface with clear prompts and user feedback.

---

## 📁 Project Structure

your_project/
│
├── app.py # Entry point with user login workflow
├── data/ # Data storage for portfolios and Excel logs
│ ├── portfolios/ # JSON files storing user quotes & stories
│ └── users_data.xlsx # Excel file logging user activity
├── modules/
│ ├── ai.py # AI prompt building and API communication
│ ├── quotes.py # Portfolio management & export functions
│ ├── languages.py # Language list and codes
│ └── user_tracking.py # Excel logging for user activity
└── pages/
└── 2_Quote_Creator.py # Streamlit quote & story generation page


---

## ⚙️ Setup Instructions

1. **Clone the repository:**

git clone https://your-repo-url.git
cd your-repo


2. **Create and activate a virtual environment (recommended):**

python -m venv venv

Windows
venv\Scripts\activate

macOS/Linux
source venv/bin/activate

3. **Install dependencies:**


pip install -r requirements.txt

text

Required packages include:
- `streamlit`
- `requests`
- `python-dotenv`
- `openpyxl`
- `python-docx`

4. **Configure environment variables:**

**Create a `.env` file in the root directory with your Groq API key:**
GROQ_API_KEY=your_api_key_here

text


5. **Run the app:**

**streamlit run app.py**

## 📝 Usage Guide

- **Login:** Enter your name and a Gmail address to start.
- **Select language and quote type:** Choose from extensive lists.
- **Optional topic:** Enter keywords to tailor the quote/story.
- **Generate:** Click “Generate Quote and Story” to receive AI content.
- **View:** Your generated quote and story will appear below.
- **Download:** Choose to download your current quote/story as TXT or DOCX.
- **Recent Quotes:** Scroll to see your recent quotes in the currently selected language.

---

## 📚 Key Modules Description

### `modules/ai.py`

Handles AI prompt building and communication with the Groq AI API for quote and story generation.

### `modules/quotes.py`

Manages user quote portfolios saved as JSON files, and exports selected quotes as TXT or DOCX files.

### `modules/user_tracking.py`

Logs each user’s activity (including inputs and generated outputs) into an Excel spreadsheet for auditing and analytics.

### `modules/languages.py`

Provides the list of supported languages with human-readable names and language codes.

---

## ⚠️ Troubleshooting Tips

- **No data in Excel logs:**  
Make sure the `log_user_activity` function is correctly called after quote/story generation. Verify write permissions in the `data/` folder.

- **Streamlit rerun errors:**  
For Streamlit versions below 1.25 use `st.experimental_rerun()`. For versions 1.25 and above use `st.rerun()`.  
Use the rerun helper function if you want compatibility with multiple Streamlit versions.

- **Blank or incorrect language dropdown:**  
Ensure you have correctly updated `modules/languages.py` with the full language list and restarted Streamlit.

- **Download buttons not showing or working:**  
Make sure the current quote and story are generated (not empty) before clicking download.

---

## 🎯 Future Improvements

- Add user authentication with persistent user accounts.
- Enable export to PDF with embedded Unicode fonts for better multilingual support.
- Add history viewing and management for users.
- Support additional AI providers for redundancy and cost management.
- Add UI improvements with enhanced styling and responsiveness.

---

## 🙏 Credits

- Built using [Streamlit](https://streamlit.io/)
- AI powered by [Groq API](https://groq.com/)
- Text processing with [python-docx](https://python-docx.readthedocs.io/) and [openpyxl](https://openpyxl.readthedocs.io/)

---

Feel free to open issues or contribute!
