import streamlit as st
from urllib.parse import urlparse
from sonar_api import ask_sonar, get_page_title, get_follow_up_questions
import concurrent.futures
import json
import os

# Inject custom CSS for background and text color
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.image("banner.png", use_container_width=True, caption="", output_format="PNG")

st.title("Research Sphere ")
st.caption("Empowering your curiosity through trusted research and interactive exploration!")

# Sidebar with instructions and about
with st.sidebar:
    st.header("About Research Sphere")
    st.write("""
    Research Sphere helps you explore any topic in depth using the power of Perplexity's Sonar API.
    - **Real-time research & citations**
    - **Follow-up questions to spark curiosity**
    - **Interactive accordion-style exploration with mini-answers**
    - **Auto-suggestions for previously explored questions**

    Explore, learn, and stay curious!
    """)
    st.markdown("---")
    st.write("Created by Naga Renuka, powered by Sonar API.")

# Load saved questions from a JSON file
if os.path.exists("previous_questions.json"):
    with open("previous_questions.json", "r") as f:
        previous_questions = json.load(f)
else:
    previous_questions = []

# Input box for question
question = st.text_input("Enter your research topic or question:")

# Filter suggestions as user types
suggestions = [q for q in previous_questions if question.lower() in q.lower()]

# Show suggestions if matches found
if suggestions and question:
    selected_suggestion = st.selectbox("Did you mean one of these?", suggestions, key="suggested_q")
    if selected_suggestion:
        question = selected_suggestion

# Explore button logic
if st.button("Explore!"):
    if question and question not in previous_questions:
        # Save the question for future suggestions
        previous_questions.append(question)
        with open("previous_questions.json", "w") as f:
            json.dump(previous_questions, f)

    with st.spinner("Digging deep! This might take a few seconds..."):

        # Parallel execution of API calls
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_main = executor.submit(ask_sonar, question)
            future_followups = executor.submit(get_follow_up_questions, question)

            data = future_main.result()
            follow_ups = future_followups.result()

        if data:
            try:
                answer = data["choices"][0]["message"]["content"]
            except (KeyError, TypeError, IndexError):
                answer = "Sorry, no insights available."

            citations = data.get("citations", [])

            st.subheader("Sonar’s Insights:")
            st.write(answer)

            if citations:
                st.subheader("Citations (APA-style!):")
                for i, link in enumerate(citations, start=1):
                    domain = urlparse(link).netloc
                    title = get_page_title(link)
                    st.markdown(f"[{i}] {title}. Retrieved from: {link} ({domain})")
            else:
                st.write("No citations available.")

            # Display follow-up questions with explanations in expanders
            if follow_ups:
                st.subheader("More to Explore:")
                for i, (q, explanation) in enumerate(follow_ups, start=1):
                    with st.expander(f"{i}. {q}"):
                        st.write(explanation)
            else:
                st.write("No follow-up questions available.")
        else:
            st.write("No response from Sonar API.")
