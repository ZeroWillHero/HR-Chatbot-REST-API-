from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
from bot.chat import get_response

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['chatbot_db']
conversations = db['conversations']

@app.route('/apiV1/chat', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        msg = data.get('message')
        user_id = data.get('user_id')
        conversation_id = data.get('conversation_id')
        if not msg:
            return jsonify({"error": "No message provided"}), 400
        
        # Process the message through the chatbot 
        # For demonstration, we will just echo the message back
        # In a real scenario, you would call your chatbot model here
        resposne = get_response(msg)
        
        if not conversation_id:
            conversation = {
                "user_id": user_id,
                "messages": [{"message": msg, "response": resposne}]
            }
            conversation_id = conversations.insert_one(conversation).inserted_id
        else:
            # Convert incoming conversation_id string to ObjectId
            conversation_obj_id = ObjectId(conversation_id)
            conversation = conversations.find_one({"_id": conversation_obj_id})
            if not conversation:
                return jsonify({"error": "Conversation not found"}), 404
            
            conversations.update_one(
                {"_id": conversation_obj_id},
                {"$push": {"messages": {"message": msg, "response": resposne}}}
            )
            conversation_id = conversation_obj_id

        response_data = {
            "chat": resposne,
            "conversation_id": str(conversation_id),  # Convert ObjectId to string
            "user_id": user_id
        }

        return jsonify({"response": response_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

@app.route('/apiV1/conversations/<user_id>', methods=['GET'])
def get_conversations(user_id):
    filtered_conversations = conversations.find({"user_id": int(user_id)})
    conversation_list = []

    for conversation in filtered_conversations:
        conversation_data = {
            "conversation_id": str(conversation["_id"]),
            "user_id": conversation["user_id"],
            "messages": conversation["messages"]
        }
        conversation_list.append(conversation_data)

    
    return jsonify({"conversations": conversation_list}), 200



if __name__ == '__main__':
    app.run(debug=True)