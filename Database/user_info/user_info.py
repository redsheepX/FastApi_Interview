from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pathlib import Path
from models import User


db = declarative_base()


class user_info_database_control:
    ENGINE_PATH = Path(__file__).parent.joinpath("user_info.db")
    ENGINE_URL = f"sqlite:///{str(ENGINE_PATH)}"
    engine = create_engine(ENGINE_URL, echo=True)

    def create_table(self):
        db.metadata.create_all(self.engine)

    def drop_table(self):
        db.metadata.drop_all(self.engine)

    def create_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        return session

    def add_new_user(self, name, email, password):
        session = self.create_session()
        user_data = {
            "name": name,
            "email": email,
            "password": password,
        }
        try:
            session.add(User(**user_data))
            session.commit()
        except Exception as e:
            print(f"{e.__class__.__name__} : {str(e)}")
        finally:
            session.close()

    def search_data(self, search_filter: dict):
        session = self.create_session()
        try:
            result = session.query(User).filter_by(**search_filter).first()
        except Exception as e:
            print(f"{e.__class__.__name__} : {str(e)}")
        finally:
            session.close()
        return result

    def search_by_id(self, id: int):
        session = self.create_session()
        try:
            result = session.query(User).filter_by(id=id).first()
        except Exception as e:
            print(f"{e.__class__.__name__} : {str(e)}")
        finally:
            session.close()
        return result

    def update_data(self): ...

    def delete_data(self): ...


if __name__ == "__main__":
    a = user_info_database_control()
    print(a.search_data({"id": 5}).__dict__)
