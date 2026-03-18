import streamlit as st
import requests

# Set page title
st.set_page_config(page_title="AI Sentiment Analyzer")

st.title("🤖 AI Sentiment Analyzer")
st.write("Type a sentence below to see if the AI thinks it is Positive or Negative.")

# User Input
user_input = st.text_input("Enter text:", placeholder="e.g., I am loving this Docker course!")

if st.button("Analyze Sentiment"):
    if user_input:
        # MAGIC ALERT: We use the service name 'sentiment-api' instead of 'localhost'
        # because Docker containers talk to each other using their service names!
        try:
            response = requests.post(
                "http://sentiment-api:8000/predict", 
                json={"text": user_input}
            )
            result = response.json()
            label = result["label"]
            
            # Display result with color
            if label == "POSITIVE":
                st.success(f"Analysis: {label} ✅")
            else:
                st.error(f"Analysis: {label} ❌")
        except Exception as e:
            st.error("Could not connect to the AI Brain. Is the API running?")
    else:
        st.warning("Please enter some text first.")
