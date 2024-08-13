document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('transaction-form');
    const transactionList = document.getElementById('transaction-list');
    const totalSpentElem = document.getElementById('total-spent');
    const dailyBreakdownElem = document.getElementById('daily-breakdown');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const date = document.getElementById('date').value;
        const amount = parseFloat(document.getElementById('amount').value);
        const description = document.getElementById('description').value;

        const response = await fetch('/api/transactions', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ date, amount, description })
        });

        if (response.ok) {
            loadTransactions();
        }
    });

    async function loadTransactions() {
        const response = await fetch('/api/transactions');
        const data = await response.json();
        const transactions = data.transactions;
        const totalSpent = data.total_spent;
        const dailyBreakdown = data.daily_breakdown;

        transactionList.innerHTML = transactions.map(tx =>
            `<li>${tx.date} - ${tx.description}: $${tx.amount.toFixed(2)}</li>`
        ).join('');

        totalSpentElem.textContent = `Total Spent: $${Math.abs(totalSpent).toFixed(2)}`;

        dailyBreakdownElem.innerHTML = Object.entries(dailyBreakdown)
            .map(([date, amount]) => `<li>${date}: $${amount.toFixed(2)}</li>`)
            .join('');
    }

    loadTransactions();
});
