from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import constantes as cons
class PostgreSQLConnection:
    def __init__(self):
        self.connection_url = f"postgresql://{cons.user}:{cons.password}@{cons.host}:{cons.port}/{cons.dbname}"
        self.engine = create_engine(self.connection_url)
        self.Session = sessionmaker(bind=self.engine)
        self.session = None

    def connect(self):
        self.session = self.Session()

    def execute_query(self, query, params=None):
        try:
            result = self.session.execute(query, params)
            return result.fetchall()
        except Exception as e:
            print(e)
            return None
        finally:
            self.session.close()

    def disconnect(self):
        self.session = None