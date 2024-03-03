from flask import Flask, request, make_response

# Initial ETag value
current_etag = 1

app = Flask(__name__)


@app.route("/")
def get_string():
    global current_etag
    # Check If-None-Match header
    if request.headers.get("If-None-Match") == str(current_etag):
        response = make_response("", 304)
        print("culprit = ", current_etag)
    else:
        # Return the string along with ETag
        response = make_response("12302727")
        response.headers["ETag"] = str(current_etag)
        current_etag += 1

    return response


if __name__ == "__main__":
    app.run(debug=True)
