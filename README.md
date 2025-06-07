# 🚀 Internet Speed Test Flask App

A simple, Dockerized Flask web application to measure internet **download speed**, **upload speed**, and **ping latency** using `speedtest-cli`.  
It includes a clean, modern UI and displays real-time results from Speedtest.net.


## 📦 Tech Stack

- **Python 3.9**
- **Flask 2.1.2**
- **speedtest-cli**
- **Docker**
- HTML + CSS for modern UI

---

## 🚀 Features

- One-click internet speed test
- Displays download & upload speeds (in Mbps)
- Shows ping, server, and ISP info
- Dockerized for portability
- Responsive UI with loading indicator

---

## 📂 Project Structure
/flask-speedtest-app/
├── app.py
├── requirements.txt
├── Dockerfile
└── templates/
    └── index.html


### Step 1. Update System

```bash
sudo apt-get update
```
### Step 2. Install Docker
```bash
 sudo apt-get install docker.io -y
```
### Step 3. Clone The Repo 
```bash
 git clone https://github.com/SaimShaikh/internetspeedtracker.git
cd Whether_app
```
### Step 2. Make a  Dockerfile inside the project
```bash
vim Dockerfile
```
### Step 3. Paste this inside the Dockerfile
```bash
# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies for speedtest-cli
RUN apt-get update && apt-get install -y \
    curl \
    && apt-get clean

# Copy dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

```
### Step 4. Build the Dockerimage
```bash
docker build -t <Any Name you want >
```
### Step 5. Run the Project
```bash
docker run -d -p 5000:5000 <app name>
```
### Step 6. Now Go to Security Groups allow port Number 5000
Images 
<img width="1665" alt="red" src="https://github.com/user-attachments/assets/4276339a-9d41-4d6b-a089-c4dc5a2592f3" />



### Step 7. Now Copy the Public Ip address of Your AWS EC2 Instance and add 5000 at the end of Address 
Images 
<img width="1669" alt="ip " src="https://github.com/user-attachments/assets/976eabcc-97b9-459f-97a3-4ba41c2a0324" />


Output 
<img width="1680" alt="Screenshot 2025-06-07 at 8 06 59 PM" src="https://github.com/user-attachments/assets/e9dddda5-15a1-44fa-b4c5-114698d76442" />


