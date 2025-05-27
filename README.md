# ResearchSphere 🚀

**ResearchSphere** is an interactive, deep-research assistant built with the Perplexity Sonar API. It enables users to explore any topic in depth with **well-structured, research-driven insights**, **trusted citations**, and **engaging follow-up questions**—all through a polished, user-friendly interface.

---

## 🌟 Features

- **In-depth insights:**  
  Every answer is thorough, structured with subheadings, bullet points, and practical explanations.

- **Trusted citations (APA-style):**  
  Each insight is backed by reputable sources for credibility and transparency.

- **Follow-up questions:**  
  Interactive expanders with mini-answers for deeper exploration—like having a conversation with a research assistant!

- **Auto-suggestions for questions:**  
  As you type, previously explored questions pop up to spark curiosity and streamline your exploration.

- **Sleek UI:**  
  Beautifully designed with a full-width header banner and custom CSS for a professional look.

---

## ⚙️ How It Works

1. **Type your question** in the search bar.  
2. **Explore structured, research-backed answers** with citations.  
3. **Dive deeper** with carefully crafted follow-up questions.  
4. **Revisit past questions** via auto-suggestions.

---

## 🛠️ Technologies

- **Frontend:** [Streamlit](https://streamlit.io/)  
- **Backend:** Python  
- **API:** [Perplexity Sonar API](https://docs.perplexity.ai/docs/sonar-api) for real-time, research-powered insights.  
- **Parallel API calls:** Boosted performance using Python’s `concurrent.futures`.  
- **Auto-suggestions:** Stored in a local JSON file (`previous_questions.json`) to personalize future research.

---

## 💡 How We Used Perplexity’s Sonar API

- **`ask_sonar`**: Generates a **deep, structured answer** to any user question.  
- **`get_follow_up_questions`**: Returns **5 carefully crafted follow-up questions** with brief explanations, encouraging deeper exploration.  
- **Real-time trusted citations** ensure transparency and accuracy for every insight.

---

## 🎥 Demo Video

👉 [YouTube/Vimeo link here – add after recording]

---


---

## 🚀 Submission Category

- **Category:** Best Deep Research Project  

---

## 📝 Additional Info

- **Original work** created entirely during the hackathon period.  
- No external funding, no IP conflicts.  
- **All code, UI, and user-facing elements** were developed specifically for this project.  

---

## 🔧 How to Run Locally

```bash
git clone [YOUR_PRIVATE_REPO_URL]
cd ResearchSphere
pip install -r requirements.txt
export SONAR_API_KEY="YOUR_API_KEY"
streamlit run app.py
