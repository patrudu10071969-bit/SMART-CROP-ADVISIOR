import zipfile
import os

# File contents
index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Smart Crop Advisory System</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <header>
    <h1>Smart Crop Advisory System</h1>
    <nav>
      <button id="languageToggle">Switch Language</button>
    </nav>
  </header>

  <main>
    <section id="soil-advisory" class="card">
      <h2>Soil Health Advisory</h2>
      <p id="soil-info">Get soil testing info, pH, fertility status, and fertilizer guidance here.</p>
      <button onclick="fetchSoilAdvisory()">Fetch Soil Advisory</button>
    </section>

    <section id="weather-updates" class="card">
      <h2>Weather Updates</h2>
      <p id="weather-info">Real-time weather alerts and crop protection tips.</p>
      <button onclick="fetchWeather()">Get Weather Update</button>
    </section>

    <section id="pest-detection" class="card">
      <h2>Pest & Disease Detection</h2>
      <input type="file" id="pestImage" accept="image/*" />
      <button onclick="uploadPestImage()">Diagnose Pest/Disease</button>
      <p id="pest-result"></p>
    </section>

    <section id="irrigation-advisory" class="card">
      <h2>Irrigation Advisory</h2>
      <p id="irrigation-info">Water requirement stage-wise suggestions.</p>
      <button onclick="fetchIrrigationAdvisory()">Get Irrigation Tips</button>
    </section>

    <section id="market-prices" class="card">
      <h2>Market Prices</h2>
      <p id="market-info">Real-time mandi prices for crops.</p>
      <button onclick="fetchMarketPrices()">Get Market Prices</button>
    </section>

    <section id="feedback" class="card">
      <h2>Feedback</h2>
      <textarea id="feedbackText" placeholder="Your feedback here"></textarea>
      <button onclick="submitFeedback()">Submit Feedback</button>
      <p id="feedbackResponse"></p>
    </section>
  </main>

  <footer>
    <p>© 2025 Smart Crop Advisory System</p>
  </footer>

  <script src="script.js"></script>
</body>
</html>'''

style_css = '''body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #eef6f2;
  color: #333;
  line-height: 1.6;
}

header {
  background-color: #2a6f4a;
  color: white;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

nav button {
  background-color: #6baa1e;
  border: none;
  padding: 0.5rem 1rem;
  color: white;
  font-weight: bold;
  cursor: pointer;
  border-radius: 4px;
}

main {
  max-width: 900px;
  margin: 1rem auto;
  padding: 0 1rem;
}

.card {
  background-color: white;
  padding: 1rem;
  margin-bottom: 1rem;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}

button {
  background-color: #2a6f4a;
  color: white;
  border: none;
  padding: 0.6rem 1.2rem;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

button:hover {
  background-color: #3b8c5a;
}

textarea {
  width: 100%;
  min-height: 80px;
  border-radius: 4px;
  border: 1px solid #ccc;
  padding: 0.5rem;
}

footer {
  text-align: center;
  padding: 1rem;
  background-color: #2a6f4a;
  color: white;
  margin-top: 2rem;
  font-size: 0.9rem;
}

@media (max-width: 600px) {
  main {
    padding: 0 0.5rem;
  }
  header {
    flex-direction: column;
    align-items: flex-start;
  }
  nav button {
    margin-top: 0.5rem;
  }
}'''

script_js = '''// Placeholder functions to simulate API calls

function fetchSoilAdvisory() {
  document.getElementById('soil-info').textContent = 'Soil pH: 6.5, Fertility: Moderate, Recommended fertilizer: NPK 15-15-15';
}

function fetchWeather() {
  document.getElementById('weather-info').textContent = 'Weather today: Sunny, Temp: 32°C, Humidity: 60%. Protect crops from heat stress.';
}

function uploadPestImage() {
  const input = document.getElementById('pestImage');
  const result = document.getElementById('pest-result');
  if (input.files.length === 0) {
    alert('Please select an image to diagnose.');
    return;
  }
  // Simulate AI diagnosis
  result.textContent = 'Diagnosis: Early signs of leaf blight detected. Suggested action: Apply fungicide within 48 hours.';
}

function fetchIrrigationAdvisory() {
  document.getElementById('irrigation-info').textContent = 'Stage 1: 2 liters/day, Stage 2: 3 liters/day, Stage 3: 4 liters/day.';
}

function fetchMarketPrices() {
  document.getElementById('market-info').textContent = 'Wheat: ₹1850/quintal, Rice: ₹2100/quintal, Maize: ₹1700/quintal.';
}

function submitFeedback() {
  const feedbackText = document.getElementById('feedbackText').value.trim();
  if (!feedbackText) {
    alert('Please enter your feedback before submitting.');
    return;
  }
  document.getElementById('feedbackResponse').textContent = 'Thank you for your feedback!';
  document.getElementById('feedbackText').value = '';
}

// Language toggle demo placeholder (can be extended with i18n libs)
document.getElementById('languageToggle').addEventListener('click', () => {
  alert('Language toggle feature coming soon!');
});'''

readme_md = '''# Smart Crop Advisory System - Website

## Overview
This is a simple, deployable frontend website for the Smart Crop Advisory System targeting small and marginal farmers. It includes key UI sections for:
- Soil Health Advisory
- Weather Updates
- Pest & Disease Detection (image upload)
- Irrigation Advisory
- Market Prices
- Feedback submission

## Technologies Used
- HTML5, CSS3
- JavaScript (vanilla)
- Responsive design for mobile devices

## How to Use
1. Open `index.html` in any modern web browser.
2. Use the buttons to simulate fetching advisory data.
3. Upload crop images to simulate pest and disease diagnosis.
4. Enter feedback and submit.

## Next Steps for Development
- Integrate backend APIs for real-time data (weather, mandi prices, soil advisory).
- Implement AI/ML model integration for pest/disease image diagnosis.
- Add multilingual and voice navigation support.
- Improve UI/UX based on farmer feedback.

## Deployment
Simply host the files on any static web hosting service (e.g., GitHub Pages, Netlify, Vercel, or any cloud storage bucket configured for hosting).

## License
MIT License
'''

zip_filename = 'smart-farmer-website.zip'

# Write files to a temp directory and zip
os.makedirs('temp_website', exist_ok=True)

files = {
    'index.html': index_html,
    'style.css': style_css,
    'script.js': script_js,
    'README.md': readme_md
}

for filename, content in files.items():
    with open(os.path.join('temp_website', filename), 'w', encoding='utf-8') as f:
        f.write(content)

# Create zip file
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for filename in files:
        zipf.write(os.path.join('temp_website', filename), arcname=filename)

zip_filename