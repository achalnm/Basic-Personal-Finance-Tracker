from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

def load_transactions():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_transactions(transactions):
    with open('data.json', 'w') as file:
        json.dump(transactions, file, indent=4)

@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    transactions = load_transactions()
    total_spent = sum(tx['amount'] for tx in transactions if tx['amount'] < 0)
    daily_breakdown = {}
    for tx in transactions:
        date = tx['date']
        if date not in daily_breakdown:
            daily_breakdown[date] = 0
        daily_breakdown[date] += tx['amount']
    return jsonify({
        'transactions': transactions,
        'total_spent': total_spent,
        'daily_breakdown': daily_breakdown
    })

@app.route('/api/transactions', methods=['POST'])
def add_transaction():
    data = request.json
    data['amount'] = float(data['amount'])
    transactions = load_transactions()
    transactions.append(data)
    save_transactions(transactions)
    return jsonify({'status': 'success'})

@app.route('/api/transactions/latest', methods=['DELETE'])
def delete_latest_transaction():
    transactions = load_transactions()
    if transactions:
        transactions.pop()
        save_transactions(transactions)
        return jsonify({'status': 'success'})
    return jsonify({'status': 'no transactions to delete'})

@app.route('/api/transactions/all', methods=['DELETE'])
def delete_all_transactions():
    save_transactions([])
    return jsonify({'status': 'success'})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
