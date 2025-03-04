async function sendVote(option) {
    const response = await fetch('/vote', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ animal: option })
    });

    const result = await response.json();

    // Instantly update the "Your Vote" section
    document.getElementById("user-vote").innerText = `Your Vote: ${result.your_vote}`;

    // Fetch updated vote results
    fetchResults();
}

async function fetchResults() {
    const response = await fetch('/results');
    const result = await response.json();

    // Update the vote counts
    document.getElementById("dogs-votes").innerText = result.dogs;
    document.getElementById("cats-votes").innerText = result.cats;
    document.getElementById("birds-votes").innerText = result.birds;
    document.getElementById("fish-votes").innerText = result.fish;
}

// Auto refresh results every 5 seconds
setInterval(fetchResults, 1000);