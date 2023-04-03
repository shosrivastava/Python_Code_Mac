# This code is used to send an email using Python.

import smtplib

con = smtplib.SMTP('smtp.gmail.com', 587)

con.ehlo()

con.starttls()

con.login('shosrivastava@gmail.com', '--')

con.sendmail('shosrivastava@gmail.com','shosrivastava@gmail.com','Subject: Test mail from Python.\n\nHello,\nThis is a test mail sent from python using VS Code.\n\
Thanks')

con.quit()