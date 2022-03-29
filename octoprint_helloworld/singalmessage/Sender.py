import requests
from phoneData import phone
# curl -X POST -H "Content-Type: application/json" 'http://localhost:8080/v2/send'
# -d '{"message": "Test via Signal API!", "number": "+48504496169", "recipients": [ "+48504496169" ]}'


if __name__ == '__main__':
    recipient = phone.get("recipient")
    sender = phone.get("sender")
    message = 'Different message'
    data = '{"message": "%s", "number": "%s", "recipients": [ "%s" ]}' % (message, sender, recipient)
    headers = {"Content-Type": "application/json"}
    requests.post("http://localhost:8080/v2/send", headers=headers, data=data)
