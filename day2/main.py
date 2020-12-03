#!/usr/bin/env python3
def read_password_file(filename: str):
    """Used to open the password file and pass back the contents

    Args:
        filename (str): filepath/filename of password file

    Returns:
        list: returns list of passwords to process
    """
    try:
        with open(filename, "r") as f:
            # Return list of passwords to perform password logic on
            contents = f.readlines()
        return contents
    except FileNotFoundError:
        print("File %s not found" % filename)


def check_password1(data):
    """Used to check the password policy one problem

    Args:
        data (str): A list object containing all the passwords that we want to check against policy
    """
    TOTAL = 0

    for password in data:
        DATA = password.split()
        RANGE = DATA[0].split('-')
        POLICY_LETTER = DATA[1].replace(':', '')
        POLICY_MIN = int(RANGE[0])
        POLICY_MAX = int(RANGE[1])
        PASSWORD = DATA[2]
        LIMIT = 0

        for letter in PASSWORD:
            if letter == POLICY_LETTER:
                LIMIT += 1
        if LIMIT >= POLICY_MIN and LIMIT <= POLICY_MAX:
            TOTAL += 1

    return str(TOTAL)


def check_password2(data):
    """Used to check the password policy two problem

    Args:
        data (str): A list object containing all the passwords that we want to check against policy
    """
    TOTAL = 0

    for password in data:
        DATA = password.split()
        RANGE = DATA[0].split('-')
        POLICY_LETTER = DATA[1].replace(':', '')
        POLICY_MIN = (int(RANGE[0]) - 1)
        POLICY_MAX = (int(RANGE[1]) - 1)
        PASSWORD = list(DATA[2])

        if PASSWORD[POLICY_MIN] == POLICY_LETTER or PASSWORD[POLICY_MAX] == POLICY_LETTER:
            if PASSWORD[POLICY_MIN] != PASSWORD[POLICY_MAX]:
                TOTAL += 1

    return str(TOTAL)


PASSWORD_DATA = read_password_file('passwords.txt')
print(check_password1(PASSWORD_DATA) +
      " passwords that meet password policy one")
print(check_password2(PASSWORD_DATA) +
      " passwords that meet password policy two")
