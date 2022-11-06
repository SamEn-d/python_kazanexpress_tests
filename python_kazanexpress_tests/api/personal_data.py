

def personal_data(email: [str] = None, firstname: [str] = 'Евгения', lastname: [str] = 'Иванова', phone: [str] = None):
    return {
        "accountId": 0,
        "birthDate": 'null',
        "email": email,
        "firstname": firstname,
        "lastname": lastname,
        "patronymic": "",
        "phone": phone,
        "sex": ""
    }

def test_asd():
    print(' ')
    print(personal_data())