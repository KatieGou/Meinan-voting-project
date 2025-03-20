async function sendVote(option) {
    const response = await fetch('/vote', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ animal: option })
    });

    const result = await response.json();

    // Instantly update the "Your Vote" section
    document.getElementById("user-vote").innerText = `Your Vote: ${result.your_vote}`;
}
