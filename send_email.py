import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "my@gmail.com"
    password = "my_app_password"
    reciever = "my@gmail.com"
    # create ssl connection
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.send_message(username, reciever, message)
