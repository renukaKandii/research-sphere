import requests
from bs4 import BeautifulSoup
import streamlit as st

def ask_sonar(question):
    api_key = st.secrets["SONAR_API_KEY"]
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "sonar",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a helpful, in-depth research assistant. For every question, "
                    "provide a thorough, well-structured answer including relevant scientific explanations, "
                    "practical examples, and bullet points if helpful. Organize your response with subheadings."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ]
    }

    response = None
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        response.raise_for_status()
        data = response.json()
        print("Sonar API Response:", data)
        return data
    except Exception as e:
        print(f"Error calling Sonar API: {e}")
        if response is not None:
            print("Response text:", response.text)
        else:
            print("No response object (API call might have failed to start).")
        return None

def get_follow_up_questions(base_question):
    api_key = st.secrets["SONAR_API_KEY"]
    follow_up_prompt = (
        f"List 5 follow-up questions someone might ask based on the question '{base_question}', "
        "and provide a brief 2-3 line explanation or answer for each. Format like:\n"
        "1. Question\n"
        "\n"
        "2. Question\n"
        "\n"
        "..."
    )

    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "sonar",
        "messages": [
            {"role": "system", "content": "You are a helpful research assistant."},
            {"role": "user", "content": follow_up_prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        response.raise_for_status()
        data = response.json()
        content = data["choices"][0]["message"]["content"]

        # Parse into pairs: question + explanation
        lines = [line.strip() for line in content.split("\n") if line.strip()]
        questions_with_answers = []
        i = 0
        while i < len(lines):
            if lines[i][0].isdigit() and (lines[i][1] == '.' or lines[i][1] == ')'):
                question = lines[i][2:].strip()
                explanation = lines[i+1].strip() if (i+1) < len(lines) else ""
                questions_with_answers.append((question, explanation))
                i += 2
            else:
                i += 1
        return questions_with_answers
    except Exception as e:
        print(f"Error fetching follow-ups: {e}")
        return []

def get_page_title(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")
        return soup.title.string.strip() if soup.title else "No Title"
    except Exception as e:
        print(f"Error fetching title for {url}: {e}")
        return "No Title"
