// Placeholder functions to simulate API calls

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
});