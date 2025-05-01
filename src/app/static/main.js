//

const form = document.querySelector('#form');

const probability = document.querySelector('#probability');
const prediction = document.querySelector('#prediction');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const formData = new FormData(form);
  const data = Object.fromEntries(formData.entries());

  try {
    const response = await fetch('/api/predict-legendary/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    if (response.ok) {
      result.classList.remove('hidden');

      const json = await response.json();

      const { is_legendary_probability, predicted_is_legendary } = json;

      probability.innerText = `${(is_legendary_probability * 100).toFixed(2)}%`;
      prediction.innerText = `${predicted_is_legendary}`;
    }
  } catch (error) {
    console.error('Fetch error:', error);
  }
});
