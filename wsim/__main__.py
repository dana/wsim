import glob
import json
import os
import threading
import time

from flask import Flask, jsonify, request

app = Flask(__name__)

gdata = {}
gdata_dir = os.path.join(os.path.dirname(__file__), "..", "gdata")


def load_gdata():
    """Loads all .json files in the gdata directory into the global gdata dict."""
    global gdata
    for f in glob.glob(os.path.join(gdata_dir, "*.json")):
        with open(f, "r") as infile:
            key = os.path.splitext(os.path.basename(f))[0]
            gdata[key] = json.load(infile)


def save_gdata():
    """Saves the global gdata dict to .json files in the gdata directory."""
    global gdata
    while True:
        time.sleep(10)
        for key, data in gdata.items():
            with open(os.path.join(gdata_dir, f"{key}.json"), "w") as outfile:
                json.dump(data, outfile, indent=4)


@app.route("/wsim/v1/<path:path>")
def get_gdata(path):
    """Returns a portion of the gdata dict based on the path."""
    return jsonify({"status": "success", path: gdata.get(path)})


def main():
    """Starts the Flask server."""
    save_thread = threading.Thread(target=save_gdata)
    save_thread.daemon = True
    save_thread.start()
    app.run(debug=True)

load_gdata()

if __name__ == "__main__":
    main()
