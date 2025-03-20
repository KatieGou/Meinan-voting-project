async function fetchResults() {
    const response = await fetch('/');
    const result = await response.json();

    // Update the vote counts
    document.getElementById("dogs-votes").innerText = result.dogs;
    document.getElementById("cats-votes").innerText = result.cats;
    document.getElementById("birds-votes").innerText = result.birds;
    document.getElementById("fish-votes").innerText = result.fish;
}

// Auto refresh results every 10 seconds
setInterval(fetchResults, 10000);
