// Event listener for when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function () {
    loadExpenses();
});

// Function to add a new expense
function addExpense() {
    // Retrieve input values from HTML elements
    const amount = document.getElementById('amount').value;
    const category = document.getElementById('category').value;
    const description = document.getElementById('description').value;

    // Check if any of the required fields is empty
    if (!amount || !category || !description) {
        alert('Please fill in all fields');
        return;
    }

    // Create a data object with the expense details
    const data = {
        amount: amount,
        category: category,
        description: description
    };

    // Send a POST request to the server to add the new expense
    fetch('/add_expense', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        alert(result.message);
        // Reload the expenses after adding a new one
        loadExpenses();
    })
    .catch(error => console.error('Error:', error));
}

// Function to load expenses from the server
function loadExpenses() {
    // Fetch the expenses from the server
    fetch('/get_expenses')
    .then(response => response.json())
    .then(data => {
        // Get the element to display the expenses
        const expensesList = document.getElementById('expenses');
        expensesList.innerHTML = '';

        // Iterate through each expense and create a list item for display
        data.expenses.forEach(expense => {
            const listItem = document.createElement('li');
            listItem.innerHTML = `Amount: ₹${expense.amount}<br>Category: ${expense.category}<br>Description: ${expense.description}<br>Date: ${new Date(expense.date).toLocaleString()}`;
            expensesList.appendChild(listItem);
        });
    })
    .catch(error => console.error('Error:', error));
}
