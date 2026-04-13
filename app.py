
from flask import Flask, render_template, request
import pickle
import requests
from urllib.parse import urlparse
from newspaper import Article
from bs4 import BeautifulSoup

app = Flask(__name__)

# Load model
model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

API_KEY = "94a0a7928ad3491b99a6d27398e0cc47"

history = []

trusted_sources = [
    "bbc.com", "cnn.com", "reuters.com",
    "theguardian.com", "nytimes.com",
    "ndtv.com", "apnews.com"
]


def extract_from_url(url):
    try:
        article = Article(url)
        article.download()
        article.parse()

        if article.text and len(article.text) > 200:
            return article.title, article.text
    except:
        pass

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")
        clean_text = []

        for p in paragraphs:
            text = p.get_text().strip()
            if len(text) > 50 and "copyright" not in text.lower():
                clean_text.append(text)

        final_text = " ".join(clean_text[:20])

        if len(final_text) > 100:
            return "Extracted Article", final_text
    except:
        pass

    return None, None


# Source check
def check_source(url):
    try:
        domain = urlparse(url).netloc.lower()

        for trusted in trusted_sources:
            if trusted in domain:
                return "Trusted Source", "green"

        return "Suspicious Source", "red"
    except:
        return "Unknown Source", "yellow"


# Live news verification
def check_live_news(query):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}"
    response = requests.get(url).json()

    if response.get("status") == "ok" and response.get("totalResults", 0) > 0:
        return True, response["articles"][:3]

    return False, []


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    confidence = None
    is_real = None
    articles = []
    source_status = None
    source_color = None
    error = None

    if request.method == "POST":
        url = request.form.get("url")
        text = request.form.get("news")

        if url:
            source_status, source_color = check_source(url)

            title, extracted_text = extract_from_url(url)

            if extracted_text:
                text = extracted_text
            else:
                error = "⚠ Could not extract article (try another link)"

        if text:
            transformed = vectorizer.transform([text])
            result = model.predict(transformed)[0]
            prob = model.predict_proba(transformed)[0].max()

            ml_prediction = "Fake News" if result == 0 else "Real News"
            confidence = round(prob * 100, 2)

            # 🔥 Live verification
            is_real, articles = check_live_news(text[:120])

            # 🔥 FINAL DECISION LOGIC
            if is_real:
                prediction = "Real News (Verified by Live Sources)"
            else:
                prediction = ml_prediction

            history.append({
                "text": text[:60],
                "result": prediction
            })

    return render_template("index.html",
                           prediction=prediction,
                           confidence=confidence,
                           is_real=is_real,
                           articles=articles,
                           history=history[-5:],
                           source_status=source_status,
                           source_color=source_color,
                           error=error)


if __name__ == "__main__":
    app.run(debug=True)


#This is final code for features