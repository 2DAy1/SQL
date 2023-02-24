from flask import Blueprint, current_app, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

admin = Blueprint('admin', __name__, url_prefix='/admin')


engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
session = Session()
if not database_exists(engine.url):
    create_database(engine.url)

with engine.connect() as con:
    con.execute(f"CREATE USER {current_app.config.from_envvar['USER']} "
                f"WITH PASSWORD {current_app.config.from_envvar['PASSWORD']}")
    con.execute(f"GRANT ALL PRIVILEGES ON DATABASE {current_app.config.from_envvar['DB_NAME']} TO "
                f"{current_app.config.from_envvar['USER']}")


@admin.route('/')
def index():
    return render_template(current_app.config['INDEX_TEMPLATE'])
