# -*- coding:utf-8 -*-
import smtplib
from email.utils import COMMASPACE
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER = 'cuitimage47@gmail.com'
# get password from https://blog.csdn.net/qq_40229790/article/details/128160396
ACCOUNT_INFO = {'username':'cuitimage47@gmail.com', 'password':'bekdydmhywevbmyf'}


def send_mail(receivers, subject, text, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, sender=SENDER, account_info=ACCOUNT_INFO):
    """
    :param receivers: 接受邮箱列表 mail box list receiver
    :param subject:发送邮件主题 mail topic sender
    :param text:发送邮件正文 mail message
    :param filename:发送邮件附件 mail attachment
    :param smtp_server:smtp服务器地址 smtp server address
    :param smtp_port:smtp TLS/STARTTLS port
    :param sender:发送者 sender
    :param account_info:发送者邮箱账号密码 mail sender's account password
    :return:
    """

    # 正文
    msg_root = MIMEMultipart()    # Create an instance with an attachment
    msg_root['SUBJECT'] = subject
    msg_root['To'] = COMMASPACE.join(receivers)
    msg_text = MIMEText(text, 'html', 'utf-8')
    msg_root.attach(msg_text)

    # # attachment
    # att = MIMEApplication(open(filename,'rb').read())
    # att.add_header('Content-Disposition', 'attachment', filename=filename)
    # msg_root.attach(att)
    # # 增加socks5代理 add socks5 proxy
    # socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'x.x.x.x', 29900, True)
    # socks.wrapmodule(smtplib)

    smtp = smtplib.SMTP(f'{smtp_server}:{smtp_port}')
    smtp.ehlo()
    smtp.starttls()
    smtp.login(account_info['username'], account_info['password'])
    smtp.sendmail(sender, receivers, msg_root.as_string())
    smtp.close()

if __name__=="__main__":
    subject="test email"
    message="This message is sent from Python."
    send_mail(['xl090@uowmail.edu.au'], subject, message)

    
