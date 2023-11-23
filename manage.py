import os
from Hispanist_flask import create_app

app = create_app()
app.config.from_object(os.environ['APP_SETTINGS'])

if __name__ == '__main__':
    app.run()
