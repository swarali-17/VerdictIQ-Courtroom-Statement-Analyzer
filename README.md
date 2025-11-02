# ⚖️ VerdictIQ - Courtroom Statement Analyzer

An NLP-based AI system that analyses witness statements and classifies them as **Valid**, **Potentially Suspicious**, or **Suspicious**, based on structural and linguistic patterns. The project features a clean and interactive Streamlit UI for legal-tech enthusiasts, built with a focus on NLP model integration and real-time verdict generation.

---

## 🚀 Features
- ✅ Real-time witness statement validation and classification  
- 🧠 NLP-powered engine using spaCy & NLTK  
- 📊 Clean Streamlit-based frontend for interactive UI to display verdict 
- 📁 Modular structure (backend notebook + frontend app)
- ⚙️ Shell script automation for environment setup & execution

---

## 🧰 Tech Stack
| Technology | Description |
|------------|-------------|
| Python 3   | Core logic & NLP processing |
| spaCy, NLTK| Linguistic analysis and classification |
| Pandas, NumPy | Data handling and manipulation |
| Streamlit | Web UI for user interaction |
| Shell scripting | Setup automation and execution |

---

## 📂 Project Structure
```
VerdictIQ/
  ├── frontend/
      └── streamlit_app.py       # Streamlit UI logic
  ├── notebook/
      └── verdict_iq.py          # NLP classification & analysis
  ├── run.sh                     # Shell script to run project
  ├── requirements.txt
  └── README.md
```

---

## ▶️ How to Run
1. Clone the repository  
   ```bash
   git clone https://github.com/swarali-17/VerdictIQ-Courtroom-Statement-Analyzer.git
   cd VerdictIQ-Courtroom-Statement-Analyzer
   ```
2. Make the run script executable  
   ```bash
   chmod +x run.sh
   ./run.sh
   ```
3. Start the Streamlit UI  
   ```bash
   streamlit run frontend/streamlit_app.py
   ```
4. Interact with the UI, upload witness statements, and observe classification results.

---

## 🎥 Demo Video  
📌 *Demo link will be added soon*  
`[Demo Coming Soon]`

---

## 🔮 Future Enhancements
- Add user authentication & role-based access  
- Expand dataset and improve classification accuracy  
- Add export of results to PDF / Excel  
- Deploy as a web service for broader access  
