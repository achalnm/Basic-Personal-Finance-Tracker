<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Basic Personal Finance Tracker</h1>
    <p>This project provides a web-based application to track personal finances. It allows users to add, delete, and view transactions, as well as see a daily breakdown of expenses.</p>
    <h2>Features</h2>
    <ul>
        <li><strong>Add Transactions:</strong> Users can add transactions with a description, date, and amount. Amounts are tracked as positive or negative values.</li>
        <li><strong>Delete Transactions:</strong> Users can delete the most recent transaction or clear all transactions.</li>
        <li><strong>View Transactions:</strong> The application displays all recorded transactions and provides a daily breakdown of expenses.</li>
        <li><strong>Total Spent Calculation:</strong> Users can calculate the total amount spent.</li>
    </ul>
    <h2>Technical Details</h2>
    <ul>
        <li><strong>Backend:</strong> Developed using Flask, a lightweight web framework for Python.
            <ul>
                <li><strong>Routes:</strong>
                    <ul>
                        <li><code>GET /api/transactions</code>: Retrieves all transactions and statistics, including total spent and daily breakdown.</li>
                        <li><code>POST /api/transactions</code>: Adds a new transaction.</li>
                        <li><code>DELETE /api/transactions/latest</code>: Deletes the most recent transaction.</li>
                        <li><code>DELETE /api/transactions/all</code>: Deletes all transactions.</li>
                        <li><code>GET /</code>: Renders the main HTML page for the application.</li>
                    </ul>
                </li>
            </ul>
        </li>
        <li><strong>Data Storage:</strong> Transactions are stored in a JSON file (<code>data.json</code>), which is read from and written to by the application.</li>
        <li><strong>Frontend:</strong> Simple HTML interface to interact with the application.</li>
    </ul>
    <h2>Usage</h2>
    <ol>
        <li><strong>Start the Flask Application:</strong> Run the <code>app.py</code> file to start the Flask server.</li>
        <li><strong>Access the Application:</strong> Open your web browser and navigate to <code>http://localhost:5000</code> to use the application.</li>
    </ol>
    <h2>Installation</h2>
    <ol>
        <li><strong>Clone the Repository:</strong>
            <pre><code>git clone https://github.com/achalnm/Basic-Personal-Finance-Tracker.git</code></pre>
        </li>
        <li><strong>Navigate to the Project Directory:</strong>
            <pre><code>cd Basic-Personal-Finance-Tracker</code></pre>
        </li>
        <li><strong>Install Dependencies:</strong>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Run the Application:</strong>
            <pre><code>python app.py</code></pre>
        </li>
    </ol>
    <h2>Project Structure</h2>
    <ul>
        <li><code>app.py</code>: Main Flask application file.</li>
        <li><code>data.json</code>: File to store transaction data.</li>
        <li><code>templates/index.html</code>: HTML template for the user interface.</li>
    </ul>
    <h2>Requirements</h2>
    <ul>
        <li>Flask</li>
        <li>Python 3.x</li>
    </ul>
    <p>For additional information or troubleshooting, please refer to the <a href="https://flask.palletsprojects.com/">Flask documentation</a>.</p>
</body>
        <footer>
        <p>Made by @achalnm</p>
        <p>
            <a href="https://github.com/achalnm" target="_blank">GitHub</a> |
            <a href="https://www.linkedin.com/in/achal-n-35153821b/" target="_blank">LinkedIn</a> |
            <a href="https://instagram.com/achal_n26" target="_blank">Instagram</a>
        </p>
    </footer>
</html>
