async function fetchProperties() {
    try {
        const response = await fetch("https://api.example.com/properties");
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Error:", error);
    }
}

fetchProperties();
