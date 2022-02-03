from flask_app import app
from flask_app.controller import routes

#If anymore controller files are added then they must be imported above here.

if __name__ == "__main__":
    app.run(debug=True)