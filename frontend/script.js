async function predict() {
    const data = {
        age: parseInt(document.getElementById("age").value),
        weight: parseInt(document.getElementById("weight").value),
        exercise: parseInt(document.getElementById("exercise").value),
        smoking: parseInt(document.getElementById("smoking").value)
    };

    const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById("result").innerText =
        `Risk: ${result.risk} | Advice: ${result.advice}`;
}
