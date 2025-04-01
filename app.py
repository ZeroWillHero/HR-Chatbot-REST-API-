from flask import Flask, request, jsonify
from chat import get_response

app = Flask(__name__)

@app.route('/apiV1/message', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        msg = data.get('message')
        if not msg:
            return jsonify({"error": "No message provided"}), 400
        
        # process the message through the chatbot 
        # For demonstration, we will just echo the message back
        # In a real scenario, you would call your chatbot model here
        resposne = get_response(msg)

        return jsonify({"response" : resposne}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)