from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Calculator! Use /calculate?num1=5&num2=3&operation=add"

@app.route('/calculate', methods=['GET'])
def calculate():
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    operation = request.args.get('operation')

    if num1 is None or num2 is None or operation not in ['add', 'subtract', 'multiply', 'divide']:
        return jsonify({"error": "Invalid parameters"}), 400

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({"error": "Cannot divide by zero"}), 400
        result = num1 / num2
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({"num1": num1, "num2": num2, "operation": operation, "result": result})

if __name__ == "__main__":
    app.run(debug=True)
