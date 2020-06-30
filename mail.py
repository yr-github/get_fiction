from email.mime.text import MIMEText
import smtplib
import configparser

class SendEmail:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config.ini",encoding='utf-8')
        self._smtp_host=self.config['mail']['smtp_host']
        self._neateasy_user = self.config['mail']['neateasy_user']
        self._neatease_code = self.config['mail']['neatease_code']
        self._send_email = self.config['mail']['send_email']
        self._receive_emails = []
        for receive_email in self.config['receive']:
            self._receive_emails.append(self.config['receive'][receive_email])
        return
    def sendemail(self,content,subject):
        message = MIMEText(content, 'plain', 'utf-8')
        message['Subject'] = subject
        message['From'] = self._send_email
        smtp_obj = smtplib.SMTP()
        try:
            smtp_obj.connect(self._smtp_host, 25)
            smtp_obj.login(self._neateasy_user, self._neatease_code)
            smtp_obj.sendmail(self._send_email, self._receive_emails, message.as_string())
            smtp_obj.quit()

        except smtplib.SMTPException as e:
            smtp_obj.quit()