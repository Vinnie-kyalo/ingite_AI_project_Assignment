from flask import Flask, request, jsonify
import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime

app = Flask(__name__)
load_dotenv()

HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}


def log_to_file(filename, data):
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                content = json.load(f)
        else:
            content = []
        content.append(data)
        with open(filename, 'w') as f:
            json.dump(content, f, indent=4)
    except Exception as e:
        print(f"Error logging to {filename}: {e}")


@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()

        if not data or 'message' not in data:
            return jsonify({'error': 'Missing "message" in JSON payload'}), 400

        user_input = data['message']
        timestamp = datetime.now().isoformat()
        user_log = {"timestamp": timestamp, "message": user_input}

        log_to_file("chat_log.json", user_log)
        log_to_file("submissions.json", {"timestamp": timestamp, "input": user_input})

        # Send to HuggingFace
        response = requests.post(
            HUGGINGFACE_API_URL,
            headers=HEADERS,
            json={"inputs": user_input}
        )

        if response.status_code != 200:
            return jsonify({"error": "Failed to get response from AI API"}), 502

        output = response.json()
        ai_reply = output[0]['generated_text'] if isinstance(output, list) else output

        return jsonify({
            "user_input": user_input,
            "ai_response": ai_reply
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
