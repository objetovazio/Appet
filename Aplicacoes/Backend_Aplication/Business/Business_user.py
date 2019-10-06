# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
# ---------------------------------
import Model.Usuario as User


# user_data = (DIC) new user to be insert
def createUser(user_data):
    new_user = User.Usuario(nome=user_data['name'], email=user_data['email'],
                       senha=user_data['password'], sobre=user_data['about'])
    try:
        print(user_data)
        print(new_user.nome)
        print(new_user)
        new_user.save()
    except Exception as err:
        print(err)
        return False
    return True


# user_data = (DIC) new informations about the user
# user_id = (STR) id user
def updateUser(user_data, user_id):
    return 0
