
from route.web import app

app.config.from_object("config.config.DevelopmentConfig")

if __name__ == "__main__":
    app.run()