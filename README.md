# Fake News Detection System

UI updated by Sakshi
# 📰 Fake News Detection System (TruthLens AI)

---

## 📌 Problem Statement

In today’s digital era, misinformation spreads rapidly across social media and online platforms, making it difficult for users to distinguish between real and fake news.

This project aims to develop an **AI-based Fake News Detection System** that analyzes news content and provides insights such as authenticity, confidence score, source credibility, and real-time verification.

---

## 🚀 Project Overview

**TruthLens AI** is a web-based application that allows users to:

* Enter news text or paste a URL
* Automatically extract article content
* Classify news as **Fake or Real**
* Display prediction confidence score
* Check **source credibility**
* Perform **live verification using NewsAPI**
* Visualize risk using an interactive meter

---

## 🧠 Features

* ✔ Fake / Real News Prediction
* ✔ Confidence Score Display
* ✔ URL-Based Article Extraction
* ✔ Source Credibility Check
* ✔ Live News Verification (NewsAPI)
* ✔ Risk Meter Visualization
* ✔ Fact-Check Summary Panel
* ✔ Clean Newspaper-Style UI

---

## 🛠️ Tech Stack

| Layer            | Technology     |
| ---------------- | -------------- |
| Backend          | Python, Flask  |
| Machine Learning | Scikit-learn   |
| Frontend         | HTML, CSS      |
| APIs             | NewsAPI        |
| Version Control  | Git, GitHub    |
| CI/CD Pipeline   | GitHub Actions |
| Testing          | Pytest         |

---

## 📂 Project Structure

```
fake-news-detection-devops/
│
├── app.py
├── requirements.txt
├── README.md
│
├── model/
│   ├── model.pkl
│   ├── vectorizer.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── bg.png
│
├── tests/
│   └── test_app.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/YOUR-USERNAME/fake-news-detection-devops.git
cd fake-news-detection-devops
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   (for Windows)
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🧪 Testing

Run automated tests:

```
pytest
```

---

## 🔄 CI/CD Pipeline

This project uses **GitHub Actions** for Continuous Integration.

### Pipeline performs:

* Install project dependencies
* Run automated tests using Pytest
* Perform static code analysis using Flake8

### Trigger:

* On every push to **main** and **dev** branches
* On pull requests

---

## 🧠 DevOps Workflow

```
Feature Branch → Dev Branch → Main Branch
            ↓
     GitHub Actions CI Pipeline
            ↓
 Automated Testing & Validation
```

---

## 📊 Sample Inputs

### ✅ Real News Example

> Government announces new economic reforms to boost GDP growth.

### ❌ Fake News Example

> Doctors hate this trick! One fruit cures all diseases instantly!

---

## 📸 Screenshots (To be added in report)

* Application UI
* Prediction Results
* CI Pipeline Execution
* GitHub Repository Structure


## 🎯 Conclusion

This project demonstrates the integration of **Artificial Intelligence and DevOps practices** to build a reliable system for fake news detection. The system ensures automated testing, continuous integration, and scalable architecture.

---

## 🔮 Future Enhancements

* Real-time news streaming
* Deep learning-based models
* Browser extension integration
* Mobile application support

---

## 🐳 Docker Setup

### Build Docker Image
docker build -t fake-news-app .

### Run Container
docker run -p 5000:5000 fake-news-app

Open:
http://127.0.0.1:5000
###

## 🚀 Live Deployment

The application is deployed on Render cloud platform:

https://fake-news-detection-devops.onrender.com/
###