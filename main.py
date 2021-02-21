import requests
import flask
import jsonpickle

app = flask.Flask(__name__, static_url_path='')


@app.route('/', methods=['GET'])
def home():
	return flask.render_template("index.html")


@app.route('/', methods=['POST'])
def operate():
	public = flask.request.form["public-key"]
	private = flask.request.form["private-key"]
	article = flask.request.form["article-content"]
	print(public, private, article)
	if public == ""  or private == "":
		data = requests.get("http://34.106.232.173:5000/generate_keys")
		data = jsonpickle.decode(data.text)
		print(data["e"], data["d"], data["n"])
		return flask.render_template("index.html", private_key=data["d"], public_key=data["n"])
	data = {
		"n": public,
		"e": "65537",
		"d": private,
		"text": article
	}
	# requests.post("http://34.106.232.173:5000/broadcast_article?n={}?e={}?d={}?text={}".format(data["n"], data["e"], data["d"], data["text"]))
	requests.post("http://34.106.232.173:5000/broadcast_article", params=data)
	return flask.render_template("index.html")

app.run()
