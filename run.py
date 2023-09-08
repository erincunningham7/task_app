import os
from taskmanager import app


# tell our app how and where to run the application
# check the name class is equal to the default main str
if __name__ == "__main__":
    # if its a match we need to have our app running
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
