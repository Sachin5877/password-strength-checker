async function checkPassword() {
    const pw = document.getElementById("password").value;
    const res = await fetch("/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ password: pw })
    });
    const data = await res.json();
    document.getElementById("result").textContent = "Strength: " + data.strength;
}
