import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(page_title="AI Sentiment Analyzer", page_icon="🤖", layout="wide")

# 2. Initialize "Memory" (Session State)
# This keeps your history alive as long as the browser tab is open
if 'history' not in st.session_state:
    st.session_state.history = []

# 3. Sidebar for History
st.sidebar.header("📜 Analysis History")
if not st.session_state.history:
    st.sidebar.info("No history yet. Start analyzing!")
else:
    for item in st.session_state.history[:10]: # Show last 10
        icon = "🟢" if item['label'] == "POSITIVE" else "🔴"
        st.sidebar.write(f"{icon} **{item['label']}**")
        st.sidebar.caption(f"'{item['text'][:30]}...' ({item['score']}%)")
        st.sidebar.divider()

# 4. Main UI Header
st.title("🤖 AI Sentiment Analyzer Pro")
st.write("Professional MLOps Dashboard | Powered by DistilBERT")

# 5. User Input Area
user_input = st.text_input("Enter text for AI analysis:", placeholder="How are you feeling today?")

# 6. Analysis Logic
if st.button("Analyze Sentiment"):
    if user_input:
        try:
            # Call the API Brain
            response = requests.post(
                "http://sentiment-api:8000/predict", 
                json={"text": user_input}
            )
            
            if response.status_code == 200:
                result = response.json()
                label = result["label"]
                score = result["score"]

                # Save to History (Top of the list)
                st.session_state.history.insert(0, {
                    "text": user_input, 
                    "label": label, 
                    "score": score
                })

                # Display Visual Metrics
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Detected Sentiment", label)
                with col2:
                    st.metric("AI Confidence", f"{score}%")

                # Progress Bar Gauge
                st.write("Confidence Level:")
                st.progress(score / 100)

                # Feedback Effects
                if label == "POSITIVE":
                    st.balloons()
                    st.success(f"Positive Sentiment Detected! ({score}%)")
                else:
                    st.error(f"Negative Sentiment Detected! ({score}%)")
            else:
                st.error("The AI Brain returned an error.")

        except Exception as e:
            st.error("Connection Error: Is the sentiment-api container running?")
    else:
        st.warning("Please enter some text first!")

# 7. Footer
st.divider()
st.caption("BCA Student Project | Mahendergarh, Haryana")
