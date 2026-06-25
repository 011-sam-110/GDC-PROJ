<h1 align="center">LLM Screen Assistant</h1>
<p align="center">A translucent desktop overlay that reads whatever is on your screen and answers questions about it, out loud.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/OCR-Tesseract-5391FE">
  <img src="https://img.shields.io/badge/LLM-GPT--4o--mini-412991?logo=openai&logoColor=white">
  <img src="https://img.shields.io/badge/TTS-OpenAI-412991?logo=openai&logoColor=white">
</p>

A small, always-on-top, semi-transparent Tkinter window that floats over your desktop. Type a
question and it screenshots your monitor, OCRs the text on it, and asks GPT-4o-mini using that text
as context, then shows the answer and reads it aloud. Handy for "what does this error mean?",
"summarise this page", or translating on-screen text without copy-pasting anything.

## ✨ Features
- **Reads your screen** — captures the monitor with `mss` and extracts its text with Tesseract OCR (`pytesseract`).
- **Context-aware answers** — the on-screen text is fed to GPT-4o-mini as system context, so questions are answered about what you are actually looking at (replies kept to 1–2 sentences).
- **Speaks the reply** — answers are voiced with OpenAI neural TTS (`gpt-4o-mini-tts`) and played through VLC.
- **Stays out of the way** — a translucent floating window (alpha 0.6) that sits over whatever you are doing.

## 🛠 Stack
Python · Tkinter (GUI) · mss + OpenCV (screen capture) · Tesseract / pytesseract (OCR) · OpenAI GPT-4o-mini (`openai`) · OpenAI TTS via `python-vlc` · `python-dotenv`.

## 🚀 Run
Requires Python, an OpenAI API key, and a local Tesseract install.
```bash
pip install openai mss pillow pytesseract opencv-python python-vlc colorama python-dotenv
echo "OPENAI_API_KEY=your_key_here" > .env
python main.py
```
Tesseract must be installed separately (its path is set in `src/CaptureScreen.py`). Type a question
in the box and press Enter; the answer appears in the window and is read aloud.

## 🧠 How it works
```
type a question → screenshot monitor (mss) → Tesseract OCR → on-screen text
   → GPT-4o-mini (text as system context) → answer in the window + OpenAI TTS → VLC playback
```
`main.py` is the Tkinter UI; `src/CaptureScreen.py` does capture + OCR, `src/llm.py` the GPT-4o-mini
call, and `src/tts.py` the spoken reply.

## 🗺 Roadmap
A working personal desktop tool.
- [ ] Multi-monitor capture (currently a single monitor)
- [ ] Make the Tesseract path configurable instead of hard-coded
- Known limitation: needs an OpenAI API key and a local Tesseract install; built and tuned for a Windows desktop.
