from flask import Flask, flash
from flask import session, request, render_template, make_response, redirect, url_for
import obase64, cPickle, StringIO


application = Flask(__name__)


@application.route("/")
def vuln():
  userData = request.args.get("input")
  cPickle.load(StringIO.StringIO(base64.b64decode(userData)))
  print('Payload loaded!', file=sys.stderr)
  return redirect('/')
  


if __name__ == "__main__":
  application.debug = True
  application.run(0.0.0.0, 8080)
