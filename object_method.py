class User:
    def __init__(self,username,name,email):#constractor
        self.username = username#properties
        self.name = name
        self.email = email 
        print("user created")
        #custom method
    # def introduce_yourself(self,guestname):
    #     print("hi {} ,I'm {}! contact me at {} .".format(guestname,self.name,self.email))
    def __repr__(self):
         
        return "user(username='{}',name='{}',email='{}')".format(self.username,self.name,self.email)
    def __str__(self):
        return self.__repr__()
# user2 = User('abhi','jhon Doe','abhi@gmail.com')

# user2.introduce_yourself("gopal")
user3  = User('abhi1','jhon1 Doe','abhi1@gmail.com')
user3
akash = User('akashh','akashshing','akash@gmail.com')
birds = User('birds1','birds 1233','birds@gmail.com')
rocky = User('rocky','rocky sing','rocky@gmail.com')
arman = User('armannnn','arman roy','arman@gmail.com')

users = [akash,birds,rocky,arman]
#print(users)


class UserDatabase:
    def __init__(self):
        self.users = []
    def insert(self, user):
        i = 0
        while i < len(self.users):
            #find the first username gater then the new user name
            if self.users[i].username > user.username:
                break
            i +=1
        self.users.insert(i,user)

def find(self,username):
    for user in self.users:
        if user.username == username:
            return user
        
def update(self,user):
    target = self.find(user.username)
    target.name,target.email = user.name , user.email

def list_all(self):
    return self.users

database = UserDatabase()
database.insert(user3)
database.insert(akash)
database.insert(arman)
database.list_all()
#user = database.find(akash)

