line = input()


class MustContainAtSymbolError(Exception):
    """Raised when there is no "@" in the email"""
    def __init__(self):
        self.message = "Email must contain @"
    def __str__(self):
        return self.message


class NameTooShortError(Exception):
    """Raised when the name in the email is less than or equal to 4"""
    def __init__(self):
        self.message = "Name must be more than 4 characters"
    def __str__(self):
        return self.message


class InvalidDomainError(Exception):
    """Raised when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org)"""
    def __init__(self):
        self.message = "Domain must be one of the following: .com, .bg, .org, .net"
    def __str__(self):
        return self.message

while line != "End":
    email = line
    valid_domains = ["com", "bg", "net", "org"]
    if "@" not in email:
        raise MustContainAtSymbolError
    elif len(email.split("@")[0]) <= 4:
        raise NameTooShortError
    elif email.split(".")[1] not in valid_domains:
        raise InvalidDomainError
    print("Email is valid")

    line = input()