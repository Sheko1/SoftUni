VALID_DOMAINS = (".com", ".bg", ".org", ".net")


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


email = input()

while email != "End":
    is_domain_valid = False

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    email = email.split("@")

    if len(email[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    for domain in VALID_DOMAINS:
        if domain in email[1]:
            is_domain_valid = True

    if not is_domain_valid:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
    email = input()
