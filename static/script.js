const pw = document.getElementById("password");
const meter = document.getElementById("meter");
const label = document.getElementById("label");

pw.addEventListener("input", async () => {
    const password = pw.value;

    const res = await fetch("/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ password })
    });

    const data = await res.json();

    meter.style.width = (data.score * 20) + "%";
    meter.style.background = data.color;
    label.textContent = data.label;
});
