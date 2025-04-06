from flask import Flask, Response
import json
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
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "uptime": f"{uptime:.2f} seconds"
    }
    pretty_json = json.dumps(response, indent=4)

    return Response(pretty_json, mimetype='application/json')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=30000)
