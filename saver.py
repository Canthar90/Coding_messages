import bcrypt


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
    