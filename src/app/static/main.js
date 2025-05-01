//

const form = document.querySelector('#form');
const resultDiv = document.querySelector('#result');
const errorMessage = document.querySelector('#error-message');
const probabilityP = document.querySelector('#probability');
const predictionP = document.querySelector('#prediction');
const submit = form.querySelector('#submit');

/**
 * Sends prediction data to the API.
 * @param {object} data - The form data to send.
 * @returns {Promise<object>} - The prediction result from the API.
 */
const fetchPrediction = async (data) => {
  const response = await fetch('/api/predict-legendary/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error(
      `API request error with status ${response.status}: ${response.statusText}`
    );
  }

  return response.json();
};

/**
 * Updates the UI with the prediction results.
 * @param {object} result - The prediction result data.
 */
const updateUI = (result) => {
  const { probability, prediction } = result;

  errorMessage.textContent = '';
  probabilityP.textContent = `${(probability * 100).toFixed(2)}%`;
  predictionP.textContent = prediction ? 'Legendary' : 'Not Legendary';

  resultDiv.classList.remove('hidden');
};

/**
 * Displays an error message in the UI.
 * @param {string} message - The error message to display.
 */
const showError = (message) => {
  errorMessage.textContent = `Error: ${message}`;
  probabilityP.textContent = '';
  predictionP.textContent = '';

  errorMessage.classList.remove('hidden');
};

/**
 * Handles the form submission event.
 * @param {Event} event - The form submission event.
 */
const onSubmit = async (event) => {
  event.preventDefault();
  submit.disabled = true;
  submit.textContent = 'Predicting...';
  resultDiv.classList.add('hidden');
  errorMessage.textContent = '';

  const formData = new FormData(form);
  const data = Object.fromEntries(formData.entries());

  try {
    const result = await fetchPrediction(data);
    updateUI(result);
  } catch (error) {
    console.error('Prediction error:', error);
    showError(error.message ?? 'An unexpected error occurred.');
  } finally {
    submit.disabled = false;
    submit.textContent = 'Predict Legendary Status';
  }
};

// Add event listener
form.addEventListener('submit', onSubmit);
