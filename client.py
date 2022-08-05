# Client IMAP
import imaplib
import email
import os

username = "usuario1"
password = "123456"

# Connection
imap = imaplib.IMAP4_SSL("localhost")
imap.login(username, password)

N = 3

status, data = imap.fetch(str(N), "(RFC822)")

print(status)
print(data)

