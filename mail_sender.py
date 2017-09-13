import smtplib
import getpass

recv = raw_input('Send To: ')
meso = raw_input('Msg: ')

sender = raw_input('Your email address: ')
sender_pswd = getpass.getpass('Password: ')

mail = smtplib.SMTP('smtp.gmail.com',587)
mail.starttls()
mail.login(sender,sender_pswd)
mail.sendmail(sender,recv,meso)
mail.quit()
