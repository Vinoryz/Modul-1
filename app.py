from flask import Flask, jsonify
import time
import datetime

app = Flask(__name__)
start_time = time.time()

@app.route("/health")
def health():
    uptime = time.time() - start_time
    response = {
        "nama": "Tom Marvolo Riddle",
        "nrp": "5025239999",
        "status": "UP",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "uptime": f"{uptime:.2f} seconds"
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
