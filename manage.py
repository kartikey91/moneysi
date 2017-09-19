from searchModule.routes import *
from extensions import Base, engine, app
from config.base import port, hostname
from Amfi_list import *
from searchModule.routes import auto_complete
app.register_blueprint(auto_complete)


if __name__ == '__main__':
    app.run(debug=True, port=port if port else 5001, host=hostname)