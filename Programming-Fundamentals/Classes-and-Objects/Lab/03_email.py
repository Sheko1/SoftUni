class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False
        self.mails = []

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


class MailBox:
    def __init__(self):
        self.emails = []

    def add_email(self, mail):
        self.emails.append(mail)

    def send_email(self, indexes):
        for i in indexes:
            self.emails[i].send()

    def get_all_info(self):
        info = ""
        for i in self.emails:
            info += f"{i.get_info()}\n"
        return info


command = input()
emails = MailBox()
while command != "Stop":
    data = command.split(" ", maxsplit=2)
    email = Email(data[0], data[1], data[2])
    emails.add_email(email)
    command = input()

index = [int(i) for i in input().split(", ")]
emails.send_email(index)
print(emails.get_all_info())
