function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    document.getElementById("message").innerText = "Logging in...";

    fetch("http://localhost:8000/auth/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, password })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw err; });
        }
        return response.json();
    })
    .then(data => {
        localStorage.setItem("user_id", data.user_id);
        localStorage.setItem("role", data.role);
        window.location.href = "dashboard.html";
    })
    .catch(err => {
        document.getElementById("message").innerText =
            err.detail || "Login failed";
    });
}
