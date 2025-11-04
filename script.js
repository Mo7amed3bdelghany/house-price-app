async function predict() {
  const size_sqft = document.getElementById("size_sqft").value;
  const bedrooms = document.getElementById("bedrooms").value;

  const response = await fetch("http://127.0.0.1:8000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      size_sqft: parseInt(size_sqft),
      bedrooms: parseFloat(bedrooms)
    })
  });

  const data = await response.json();
  document.getElementById("result").innerText =
    "Predicted Price: $" + data.predicted_price.toFixed(2);
}
