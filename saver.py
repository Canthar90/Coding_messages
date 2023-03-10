import bcrypt
from sqlalchemy import ForeignKey, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import create_engine
import random
import string


class Base(DeclarativeBase):
    pass

class User_info(Base):
    __tablename__ = "user_information"
    
    Id: Mapped[int] = mapped_column(primary_key=True)
    Login: Mapped[str] = mapped_column(primary_key=True)
    Password: Mapped[str]
    Decode_key: Mapped[str]
    
    def __repr__(self) -> str:
        return f"User_info(Id={self.Id!r}, Login={self.Login!r}, Password={self.Password!r}), Decode_key={self.Decode_key!r}"


class Hasher:

    def hash_it(self, password):
        self.salt = bcrypt.gensalt()
        passw = password.encode('utf-8')
        hashed = bcrypt.hashpw(passw, self.salt)
        return hashed
    
    def check_psw(self, password, hashed_psw):
        passw = password.encode('UTF-8', errors="strict")
        return bcrypt.checkpw(password=passw, hashed_password=hashed_psw) 

    
class DatabaseKelner():
    def __init__(self):
        self.engine = create_engine("sqlite:///data.db", echo=True)
        self.session = Session(self.engine)
        self.hasher = Hasher()
        
    def save_to_db(self, login, password, key):
        with Session(self.engine) as session:
            newuser = User_info(
                Login=login,
                Password=password,
                Decode_key=str(key)
            )
            
            session.add_all([newuser,])
            session.commit()
        
    def check_if_login_is_free(self, login):
        try:
            stmt = (
                select(User_info)
                .where(User_info.Login==login)
            )
            sandy_address = self.session.scalars(stmt).one()
            return False
        except:
            return True
        
    def retrive_key(self, login, password):
        try:
            stmt = select(User_info).where(User_info.Login.in_([login]))
            for elem in self.session.scalars(stmt):
                hashed_password = elem.Password
                decode_key = eval(elem.Decode_key)
            
            if self.hasher.check_psw(password, hashed_password):
                return decode_key

        except:
            return False

        
        
        
