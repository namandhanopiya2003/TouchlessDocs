# TouchlessDocs: Gesture-Operated Document Viewer for Field Workers

## 🧠 ABOUT THIS PROJECT ==>

- TouchlessDocs is a Python-based, AI-powered document viewer that lets field professionals (engineers, doctors, mechanics, etc.) **interact with PDF documents using hand gestures and voice commands** — no need to touch their devices! 

- This application uses:
**Rule-based gesture recognition** (no training required)
**Voice command intent classification using NLP**
**Real-time PDF rendering and annotation**
**User interaction logging for future predictive analytics**

- Ideal for hands-free access to manuals, blueprints, or medical reports in dusty, wet, or sterile environments.

---

## ⚙ TECHNOLOGIES USED ==>

- **Python**
- **OpenCV**                                  (video streaming & image annotation)
- **MediaPipe**                               (hand landmark detection)
- **PyMuPDF (fitz)**                          (PDF rendering & manipulation)
- **SpeechRecognition**                       (speech-to-text)
- **NLTK / Simple NLP rules**                 (command intent classification)
- **Matplotlib / Pandas**                     (analytics, optional)
- **Pickle / CSV**                            (logging data)

---

## 📁 PROJECT FOLDER STRUCTURE ==>

TouchlessDocs/<br>
│<br>
├── app/                      # Core application<br>
│   ├── __init__.py<br>
│   ├── main.py               # Entry point<br>
│   ├── gesture_control.py    # Rule-based gesture detection<br>
│   ├── voice_commands.py     # Voice-to-text + NLP intent recognition<br>
│   ├── pdf_viewer.py         # PDF viewing and interaction<br>
│   ├── annotator.py          # Drawing/annotation tool<br>
│   └── session_logger.py     # User interaction logging and analytics<br>
│<br>
├── utils/                    # Utility modules<br>
│   ├── __init__.py<br>
│   ├── mediapipe_utils.py    # MediaPipe initialization and helpers<br>
│   ├── nlp_utils.py          # Intent classification<br>
│   └── gesture_rules.py      # Reusable rule functions<br>
│<br>
├── data/                     # Logs, voice samples, interaction data<br>
│   ├── logs/<br>
│   └── analytics/<br>
│<br>
├── models/                   # Optional future AI models (e.g. ChatGPT, user modeling)<br>
│   └── README.md             # Explain how to add/plug in AI models here<br>
│<br>
├── assets/                   # Icons, images, example PDFs<br>
│<br>
├── requirements.txt<br>
├── README.md<br>
└── run.py                    # Launch the app

---

## 📝 WHAT EACH FILE DOES ==>

- **`app/gestures.py`**  
  Implements gesture detection rules using MediaPipe landmarks. Detects gestures like "next", "previous", and "pinch".

- **`app/pdf_viewer.py`**  
  Handles PDF rendering, page navigation, and annotation using PyMuPDF.

- **`app/voice_control.py`**  
  Uses SpeechRecognition to listen for voice input and classify it using rule-based NLP.

- **`app/nlp_utils.py`**  
  Contains logic for matching spoken phrases to commands like `"next_page"` or `"save_comment"`.

- **`app/analytics.py`**  
  Logs gesture/voice actions to CSV and computes basic usage stats.

- **`app/main.py`**  
  Initializes the camera, gesture detection, voice command handling, and PDF rendering.

- **`run.py`**  
  The main launcher script for running the application.

---

## 🚀 HOW TO RUN ==>

# Step 1: Open CMD and move to the project directory
cd "D:\TouchlessDocs"
D:

# Step 2: Create and activate a virtual environment
python -m venv venv
venv\\Scripts\\activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Make sure there's a PDF in the assets/ folder
Rename PDF to example.pdf or update the path in main.py

# Step 5: Run the app
python run.py

# Step 6: Controls inside the app
- Show hand gesture for next/previous page.
- Press v to speak a command like "next page", "save", "zoom in", etc.
- Press q to quit.

---

✨ SAMPLE OUTPUT ==>

📄 Document: example.pdf<br>
🎥 Webcam: Activated<br>
🖐️ Detected Gesture: "Next Page"<br>
🗣️ Voice Command: "Save comment" → save<br>
💾 Screenshot saved to screenshots/gesture_2025_06_13_111212.jpg<br>
📊 Analytics: 3 gestures, 2 voice commands logged in session.

---

📬 CONTACT ==>
For queries, feature suggestions, or collaboration, feel free to connect!

---


