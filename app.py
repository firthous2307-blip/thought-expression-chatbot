from flask import Flask, render_template, request

app = Flask(__name__)

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "sad" in user_input or "lonely" in user_input:
        return "I hear that you're feeling low. Do you want to talk about what's bothering you?"

    elif "stress" in user_input or "anxious" in user_input:
        return "Stress can feel heavy. What is causing it right now?"

    elif "happy" in user_input:
        return "Thats great to hear! What made you happy today?"

    else:
        return "Im here to listen. Tell me more."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.form["msg"]
    return chatbot_response(user_text)

if __name__ == "__main__":
    app.run(debug=True)