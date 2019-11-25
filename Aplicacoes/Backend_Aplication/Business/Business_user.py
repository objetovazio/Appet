# used to resolve the path problem
import sys
from os.path import dirname, abspath
diretorio = dirname(dirname(abspath(__file__)))
sys.path.append(diretorio)
# ---------------------------------
import Model.Usuario as User
import json
from passlib.hash import pbkdf2_sha256

#POST METHOD ZONE


# user_data = (DIC) novo usuario para ser inserido na base
def createUser(user_data):
    hashPass = pbkdf2_sha256.hash(user_data['password'])
    new_user = User.Usuario(nome=user_data['name'], email=user_data['email'],
                            senha=hashPass, sobre=user_data['about'])
    try:
        new_user.save()
    except Exception as err:
        print(err)
        return False
    return True

def createGoogleUser(google_user):
    fakeHash = pbkdf2_sha256.hash(google_user['googleid'][0:5])
    new_user = User.Usuario(nome=google_user['name'],email=google_user['email'],
    google_id=google_user['googleid'], senha=fakeHash)
    try:
        new_user.save()
    except Exception as err:
        print(err)
        return False
    return _makeResultDic(new_user)

# user_data = (DIC) novas informacoes sobre o usuario
# user_id = (STR) id do usuario a ser atualizado
def updateUser(user_data, user_id):
    old_user = User.Usuario.get((User.Usuario.usuario_id == user_id))
    try:
        old_user.nome = user_data['name'] if user_data['name'] != None else old_user.nome
        old_user.email = user_data['email'] if user_data['email'] != None else old_user.email
        old_user.senha = pbkdf2_sha256.hash(user_data['password']) if user_data['password'] != None else old_user.senha
        old_user.sobre = user_data['about'] if user_data['about'] != None else old_user.sobre
        old_user.save()
    except Exception as err:
        print(err)
        return False
    return True

#END ZONE

#GET METHOD ZONE

#user_query = (DIC) paramerto de busca.
def findUsers(user_query):
    query_result = None
    final_result = []
    if(user_query['user_id']!= None):
        query_result = User.Usuario.get_by_id(user_query['user_id'])
        final_result.append(_makeResultDic(query_result))
        return final_result
    if(user_query['googleid']!=None):
        query_result = User.Usuario.select().where(User.Usuario.google_id == user_query['googleid'])
        for result in query_result:
            final_result.append(_makeResultDic(result))
        return final_result
    if(user_query['user_name'] != None):
        if(user_query['email_user'] != None and user_query['about_user'] != None):
            query_result = User.Usuario.select().where((User.Usuario.nome.contains(user_query['user_name'])) &
                                                       (User.Usuario.email == user_query['email_user']) &
                                                       (User.Usuario.is_deleted == 0)  &
                                                       (User.Usuario.sobre.contains(user_query['about_user'])) )
        else:
            
            if (user_query['email_user'] != None):
                query_result = User.Usuario.select().where((User.Usuario.nome.contains(user_query['user_name'])) &
                                                           (User.Usuario.is_deleted == 0)  &
                                                           (User.Usuario.email == user_query['email_user']))
            elif( user_query['about_user'] != None ):
                query_result = User.Usuario.select().where((User.Usuario.nome.contains(user_query['user_name'])) &
                                                           (User.Usuario.is_deleted == 0)  &
                                                           (User.Usuario.sobre.contains(user_query['about_user'])) )
            else:
                query_result = User.Usuario.select().where((User.Usuario.is_deleted == 0)  &
                                                            (User.Usuario.email == user_query['email_user']) )
            
    elif (user_query['email_user'] != None):
        if (user_query['about_user'] != None):
            query_result = User.Usuario.select().where((User.Usuario.email == user_query['email_user']) &
                                                       (User.Usuario.is_deleted == 0)  &
                                                       (User.Usuario.sobre.contains(user_query['about_user'])) )
        else:
            query_result =User.Usuario.select().where(
                (User.Usuario.is_deleted == 0)  &
                (User.Usuario.email == user_query['email_user'])
                )
    else:
        query_result = User.Usuario.select().where(
            (User.Usuario.is_deleted == 0)  &
            (User.Usuario.sobre.contains(user_query['about_user'])) 
            )
    
    for find_user in query_result:
        final_result.append(_makeResultDic(find_user))
    return final_result

def deleteUser(user_ids):
    convert_ids = json.loads(user_ids)
    query_data = User.Usuario.update(is_deleted = 1).where(User.Usuario.usuario_id.in_(convert_ids))
    row_modified = query_data.execute()
    if(row_modified > 0):
        return True
    else:
        False

def userLogin(user_query):
    email = user_query['email_user']
    password = user_query['password']
    if(email != None and password != None):
        user = User.Usuario.select().where((User.Usuario.email == email))
        
        isCorretPassword = pbkdf2_sha256.verify(password, user[0].senha)
        if(len(user) == 1 and isCorretPassword):
            dic_user = _makeResultDic(user[0])
            dic_user['password'] = ''
            print(dic_user)
            return dic_user
        #end-if
    return None
# end

def verifyToken(user_id, user_email):
    user = User.Usuario.get(User.Usuario.email == user_email, User.Usuario.usuario_id == user_id)
    return _makeResultDic(user)
#end

def _makeResultDic(user_obj):
    user_dic = {
        'user_id':user_obj.usuario_id,
        'name':user_obj.nome,
        'email':user_obj.email,
        'password':user_obj.senha,
        'about':user_obj.sobre,
        'admin':user_obj.is_adm,
        'google_id':user_obj.google_id
    }
    return user_dic
#END ZONE
