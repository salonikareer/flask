import flask
app = flask.Flask(__name__)

information = [{"Name" : "saloni", "education":"MCA"}]
@app.route('/')
def hello():

 return "Hello World"
@app.route('/get-value', methods = ['GET'])

def GetInfo():

 return flask.jsonify({ 'data' : information })

@app.route('/post-value', methods = ['POST'])
def PostInfo():

 if not flask.request.json :
  return flask. jsonify({'status’ : ‘error'})

 newInfo = {'Name' : flask.request.json["Name"], 'education' : flask.request.json["education"]}
 information. append (newInfo)
 return flask. jsonify({'status' : 'success'})
app.run()
