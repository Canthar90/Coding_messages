import bcrypt
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import create_engine


class Base(DeclarativeBase):
    pass

class User_info(Base):
    __tablename__ = "user_information"
    
    Id: Mapped[int] = mapped_column(primary_key=True)
    Login: Mapped[str]
    Password: Mapped[str]
    Decode_key: Mapped[str]
    
    def __repr__(self) -> str:
        return f"User_info(Id={self.Id!r}, Login={self.Login!r}, Password={self.Password!r}), Decode_key={self.Decode_key!r}"


class Hasher:
    def __init__(self):
        self.salt = bcrypt.gensalt()
        
    def hash_it(self, password):
        passw = password.encode('utf-8')
        hashed = bcrypt.hashpw(passw, self.salt)
        return hashed
    
    def check_psw(self, password, hashed_psw):
        passw = password.encode('utf-8')
        return bcrypt.checkpw(password=passw, hashed_password=hashed_psw) 
        


        
        
if __name__ ==  "__main__":
    hasher = Hasher()
    hashed = hasher.hash_it("kopytK0")
    print(hasher.check_psw("kopytK0", hashed))
    
    engine = create_engine("sqlite:///data.db", echo=True)
    with Session(engine) as session :
        Login = "Fernando 66"
        password = hashed
        key = {'a':'a', 'b':'b'}
        newuser = User_info(
            Login=Login,
            Password=password,
            Decode_key=str(key)
        )
        session.add_all([newuser,])
        session.commit()
    