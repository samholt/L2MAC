from web_application import WebApplication

app = WebApplication()
app.manage_connectivity(True)
print(app.online_status)
app.manage_connectivity(False)
print(app.online_status)
