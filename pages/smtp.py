
import smtplib

SenderAddress = "info@techneith.com"
password = "8M8yXzwHxEAc"



def send_mail(email,subject,msg,cc=[]):
    toaddr = email
    cc_mail = cc
    fromaddr = SenderAddress
    message = "From: {}\r\n".format(fromaddr) + "To: {}\r\n".format(toaddr) + "CC: {}\r\n".format(",".join(cc_mail))+ "Subject: {}\r\n".format(subject)+ "\r\n"+ msg
    toaddrs = [toaddr] + cc
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SenderAddress, password)
    # body = "Subject: {}\n\n{}".format(subject,msg)
    server.sendmail(SenderAddress, toaddrs, message.encode('utf-8'))
    server.quit()