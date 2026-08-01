#######################################################################################################
#   Module name   :         SendMail
#   Function name :         send_mail
#   Input         :         sender, reciever, app_password, subject, body, attchment, filename
#   Description   :         Sends the detailed log files through Email periodically
#   Date          :         26/07/2026
#   Author        :         Prajwal
#######################################################################################################

from email.message import EmailMessage
import smtplib

def send_mail(sender, reciever, app_password, subject, body, attachment, filename):
    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = reciever
    msg["Subject"] = subject

    msg.set_content(body)
    msg.add_attachment(attachment, maintype = "text", subtype = "plain", filename = filename)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(sender, app_password)
    smtp.send_message(msg)
    smtp.quit()