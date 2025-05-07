from flask import Flask, render_template, render_template_string, request
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
scraped_data = []

@app.route('/',methods=["GET"])
def main():
    return render_template("index.html",data=scraped_data)

@app.route('/scrape', methods=['POST', "GET"])
def receive_scrape():
    if request.method == "POST":
        data = request.json
        yrs = "years" in data.get("JDText")
        if yrs:
            x  = data.get("JDText", "")[data.get("JDText", "").index("years")-6:data.get("JDText", "").index("years")+5] 
        else: 
            x = "Not Found"
        scraped_item = {
        "role": data.get("RoleText","Not Found"),
        "exp": x,
        "found_python": "Yes" if "python" in data.get("JDText") or "Python" in data.get("JDText") else "No",
        "found_django": "Yes" if "django" in data.get("JDText") or "Django" in data.get("JDText") else "No",
        "JD": data.get("JDText"),
        }
        scraped_data.append(scraped_item)
        socketio.emit("new_data", scraped_item)
        return {"status": "success"}
    
if __name__ == "__main__":
    socketio.run(app, debug=True)