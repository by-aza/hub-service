
// Toggle Dark Mode
document.getElementById("themeToggle").onclick = function () {
    document.body.classList.toggle("dark-mode");

    if (document.body.classList.contains("dark-mode")) {
        localStorage.setItem("theme", "dark");
        this.textContent = "☀️";
    } else {
        localStorage.setItem("theme", "light");
        this.textContent = "🌙";
    }
};

// La încărcare, aplicăm tema salvată
if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark-mode");
    document.getElementById("themeToggle").textContent = "☀️";
}