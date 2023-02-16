from flask import Flask
from models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.config["SQLALCHEMY_DATABASE_URI"] = f"{app.config.from_envvar['DB']}://{app.config.from_envvar['USER']}:" \
                                            f"{app.config.from_envvar['PASSWORD']}" \
                                            f"@{app.config.from_envvar['DB_NAME']}" \
                                            f":port/{app.config.from_envvar['HOST']}"

    db.init_app(app)
    with app.app_context():
        db.create_all()

    from views.admin import admin
    app.register_blueprint(admin)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
