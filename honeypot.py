import time
import socket
import atexit
import os
import smtp
import winsound

BANNER = b'220 ProFTPD 1.2.8 Server\nName: '
LHOST = '0.0.0.0'
LPORT = 21
TIMEOUT = 10

mailService = smtp.SmtpMailService
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def send_log(ip):
    logMessage = f"Attack detected from : {ip} !"
    mailService.send_mail(mailService, "Honeypot triggered", logMessage)


def exit_handler():
    print('\n[*] Honeypot is shutting down!')
    listener.close()


def honeypot_enable():
    print('[*] Honeypot starting on ' + LHOST + ':' + str(LPORT))
    atexit.register(exit_handler)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind((LHOST, LPORT))
    listener.listen(5)

    while True:
        (insock, address) = listener.accept()
        insock.settimeout(TIMEOUT)
        print('[*] Honeypot connection from ' + address[0] + ':' + str(address[1]) + ' on port ' + str(LPORT))
        send_log(address[0])
        winsound.PlaySound("redalarm", winsound.SND_FILENAME)
        try:
            insock.send(BANNER)
            data = insock.recv(1024)

        except socket.error as e:
           # send_log(address[0])
            time.sleep(2)
        else:
            print("Attacker is sending data.")
            break
        finally:
            insock.close()
