from post_office.mail import send, PRIORITY


def test_send():
    email = send(
        "flamsmile18+reciever@gmail.com",
        "flamsmile18+sender@gmail.com",
        subject="Test Subject",
        message="Test Message, Hi!!!",
        priority=PRIORITY.now
    )
    return email
