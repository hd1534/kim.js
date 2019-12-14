def register_blueprint(app):
    app.register_blueprint(__import__("resources.main", fromlist=["main_resource"]).main_resource)
