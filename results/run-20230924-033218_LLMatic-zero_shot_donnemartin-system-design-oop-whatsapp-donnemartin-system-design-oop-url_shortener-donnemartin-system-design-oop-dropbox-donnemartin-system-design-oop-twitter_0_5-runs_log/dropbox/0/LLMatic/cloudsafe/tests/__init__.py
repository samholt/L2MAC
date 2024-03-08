from cloudsafe.app import create_app, db

app = create_app()
app.app_context().push()

