from api.repositories import userRepository

def exist(email):
    return userRepository.exist(email) or []

def createUser(email, password):
    return userRepository.createUser(email,password) or False
