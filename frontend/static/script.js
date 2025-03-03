async function sendVote(option) {
    const response = await fetch('/vote', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ animal: option })
    });

    const result = await response.json();
    document.getElementById("result").innerText = JSON.stringify(result.your_vote);
}

async function fetchResults() {
    const response = await fetch('/results');
    const result = await response.json();
    document.getElementById("vote-results").innerText = JSON.stringify(result);
}

// Auto refresh results every 5 seconds
setInterval(fetchResults, 500);