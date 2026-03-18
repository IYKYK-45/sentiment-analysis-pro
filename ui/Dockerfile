FROM python:3.10-slim

WORKDIR /app

# Install only what we need for the UI
RUN pip install streamlit requests

COPY . .

# Streamlit runs on port 8501 by default
EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
