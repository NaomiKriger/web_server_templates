from flask import Flask, request

app = Flask(__name__)

data_content = {"key_1": "value_1", "key_2": "value_2"}


@app.route("/")
def index():
    return {"message": "Welcome to the templates app server!"}


@app.route("/data", methods=["POST"])
def update_data():
    content = request.json
    data_content.update(content)
    return data_content


@app.route("/data", methods=["GET"])
def get_data():
    return data_content


@app.route("/data/<key>", methods=["GET"])
def get_data_per_key(key: str):
    if key in data_content:
        return {key: data_content[key]}
    return {"message": f"the requested parameter {key} was not found"}


@app.route("/data/delete/<key>", methods=["DELETE"])
def delete_data(key: str):
    if key in data_content:
        del data_content[key]
        return {"message": f"parameter {key} and its content was deleted successfully"}
    else:
        return {"message": f"the parameter {key} was not found"}


app.run(host="0.0.0.0", port=5000, debug=True)
