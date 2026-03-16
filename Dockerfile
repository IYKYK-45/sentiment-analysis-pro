# Use a tiny version of Python (saves space!)
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system essentials
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy only the requirements file first
COPY requirements.txt .

# Install the LEAN version of libraries inside Docker
RUN pip install --no-cache-dir -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

# Copy the rest of your app code
COPY ./app ./app

# The command to run the API
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
