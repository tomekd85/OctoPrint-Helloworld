import requests
from singalmessage.phoneData import phone


class SignalMessageSender:

    def send_message(self, message):
        recipient = phone.get("recipient")
        sender = phone.get("sender")
        data = '{"message": "%s", "number": "%s", "recipients": [ "%s" ]}' % (message, sender, recipient)
        headers = {"Content-Type": "application/json"}
        print(requests.post("http://localhost:8080/v2/send", headers=headers, data=data))


if __name__ == '__main__':
    SignalMessageSender().send_message("A test signal message")
