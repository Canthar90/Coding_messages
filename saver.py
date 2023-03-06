import bcrypt
from sqlalchemy import ForeignKey, String, select
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

    def hash_it(self, password):
        self.salt = bcrypt.gensalt()
        passw = password.encode('utf-8')
        hashed = bcrypt.hashpw(passw, self.salt)
        return hashed
    
    def check_psw(self, password, hashed_psw):
        passw = password.encode('utf-8')
        return bcrypt.checkpw(password=passw, hashed_password=hashed_psw) 
        


        
        
if __name__ ==  "__main__":
    hasher = Hasher()
    # hashed = hasher.hash_it("kopytK0")
    # print(hasher.check_psw("kopytK0", hashed))
    
    engine = create_engine("sqlite:///data.db", echo=True)
    session = Session(engine) 
    # with Session(engine) as session :
    #     Login = "Fernando 66"
    #     password = hashed
    #     key = {'a':'a', 'b':'b'}
    #     newuser = User_info(
    #         Login=Login,
    #         Password=password,
    #         Decode_key=str(key)
    #     )
    #     session.add_all([newuser,])
    #     session.commit()
    stmt = select(User_info).where(User_info.Login.in_(["Fernando 66"]))
    # session.scalar(stmt)
    # print(stmt)
    for user in session.scalars(stmt):
        print(user)
        print(type(user.Decode_key))
        user_name = user.Login
        user_password = user.Password
        user_key = user.Decode_key
        
    print(hasher.check_psw("kopytK0", user_password))
    
        