from django.core.validators import validate_email
from .models import User


def validate_signup(signup_data):
    username = signup_data.get("username")
    password = signup_data.get("password")
    nickname = signup_data.get("nickname")
    birth = signup_data.get("birth")
    first_name = signup_data.get("first_name")
    last_name = signup_data.get("last_name")
    email = signup_data.get("email")

    err_msg_list = []

    # validation
    # validation dup username
    if User.objects.filter(username=username).exists():
        err_msg_list.append({"username" : "이미 존재하는 유저네임입니다."})
    
    # validation email
    try:
        validate_email(email)
    except:
        err_msg_list.append({"email": "올바른 이메일 형식이 아닙니다."})

    # validation dup email
    if User.objects.filter(email=email).exists():
        err_msg_list.append({"email": "이미 존재하는 이메일입니다."})

    if err_msg_list:
        return False, err_msg_list
    else:
        return True, err_msg_list