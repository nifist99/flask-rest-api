from route.web import app
import os

app.config.from_object("config.config.DevelopmentConfig")
app.config["SECRET_KEY"]=os.getenv("SECRET_KEY")

if __name__ == "__main__":
    app.run()