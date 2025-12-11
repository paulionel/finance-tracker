console.log("Frontend JS loaded");

// Fetch helper
async function fetchJSON(url, options = {}) {
    const res = await fetch(url, options);
    if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
    return res.json();
}

// Populate dropdowns
async function populateDropdowns() {
    const users = await fetchJSON('/users/');
    const categories = await fetchJSON('/categories/');
    const paymentMethods = await fetchJSON('/payment-methods/');

    const userSelect = document.getElementById('user');
    users.forEach(u => userSelect.appendChild(new Option(u.name, u.id)));

    const categorySelect = document.getElementById('category');
    categories.forEach(c => categorySelect.appendChild(new Option(c.name, c.id)));

    const paymentSelect = document.getElementById('payment-method');
    paymentMethods.forEach(p => paymentSelect.appendChild(new Option(p.name, p.id)));
}

// Fetch and display transactions
async function loadTransactions() {
    const transactions = await fetchJSON('/transactions/');
    const tbody = document.querySelector('#transactions-table tbody');
    tbody.innerHTML = '';
    transactions.forEach(t => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${t.id}</td>
            <td>${t.user}</td>
            <td>${t.category}</td>
            <td>${t.payment_method}</td>
            <td>${t.amount}</td>
            <td>${t.note || ''}</td>
            <td>${new Date(t.timestamp).toLocaleString()}</td>
        `;
        tbody.appendChild(row);
    });
}

// Form submission
document.getElementById('transaction-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const payload = {
        user_id: parseInt(document.getElementById('user').value),
        category_id: parseInt(document.getElementById('category').value),
        payment_method_id: parseInt(document.getElementById('payment-method').value),
        amount: parseFloat(document.getElementById('amount').value),
        note: document.getElementById('note').value,
        is_deposit: false
    };
    await fetchJSON('/transactions/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });
    e.target.reset();
    loadTransactions();
});

// Initial load
populateDropdowns();
loadTransactions();

