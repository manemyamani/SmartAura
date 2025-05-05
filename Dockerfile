FROM python:3.10-slim

# Install system dependencies for OpenCV and dlib
RUN apt-get update && apt-get install -y \
    build-essential cmake libgtk2.0-dev pkg-config \
    libavcodec-dev libavformat-dev libswscale-dev \
    libboost-all-dev \
    && apt-get clean

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy your project files
COPY . /app
WORKDIR /app

# Expose port and run app
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
