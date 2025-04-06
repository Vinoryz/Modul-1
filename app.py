from flask import Flask
import os
import time

app = Flask(__name__)
start_time = time.time()

@app.route('/health')
def health():
    return {
        "nama": "Tom Marvolo Riddle",
        "nrp": "5025239999",
        "status": "UP",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "uptime": f"{int(time.time() - start_time)} seconds"
    }

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
