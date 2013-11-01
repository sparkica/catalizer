from flask import Flask, render_template, request
from catcomplexity import calculate_score
from twython import Twython
import simplejson as json

app = Flask(__name__)

def get_friends_from_twitter(screenname):
	
	# get api key and the secret from Twitter site for developers
	APP_KEY = 'enter-your-api-key'
	APP_SECRET = 'enter-your-secret'

	twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
	ACCESS_TOKEN = twitter.obtain_access_token()
	twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

	results = twitter.lookup_user(screen_name=screenname)
	
	# there should be only one result as we use only one screename
	for result in results:
		return result['friends_count']


@app.route('/complicate', methods=['GET', 'POST'])
def get_catcomplexity_score():
	print request.method
	
	if request.method == 'POST':
		
		user_name = request.form['user_name']
		gender = request.form['gender']
		age = request.form['age']
		friends = request.form['friends']
		screen_name = request.form['twitter']
		# get friends from Twitter
		virtual_friends = get_friends_from_twitter(screen_name)
		
		return render_template('catcomp_result.html', user = user_name, complexity = calculate_score(gender, int(age), int(friends), virtual_friends))

	return render_template('catcomp.html')

def jsonpify(obj):
	"""
	Like jsonify but wraps result in a JSONP callback if a 'callback'
	query param is supplied.
	"""
	try:
		callback = request.args['callback']
		response = app.make_response("%s(%s)" % (callback, json.dumps(obj)))
		response.mimetype = "text/javascript"
		return response
	except KeyError:
		return json.dumps(obj)


@app.route('/info', methods=['GET'])
def get_catcomplicator_info():
	
	metadata = {
		"name": "Catcomplicator",
		"version": "0.1",
		"author", "sparkica"
	}
	
	return jsonpify(metadata)

@app.route('/')
def home():
	
	return render_template('home.html')

if __name__ == '__main__':
	app.run(debug=True)