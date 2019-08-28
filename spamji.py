import smtplib
import pyfiglet
from getpass import getpass



# ******************* Spaming Script ********************#
#  inputs <= list of targets emails, number of sending   #
#  output => sending mails to the targets                #
#  tool made by th3m7J0                                  #
#********************************************************#

ascii_banner = pyfiglet.figlet_format("Spamji")
print(ascii_banner)
print('This Tool Was Created  By th3m7J0 ¯\_(ツ)_/¯\n For Any Queries Contact Me !'
      '\n           Mail : th3m7j0@gmail.com'
      '\n       Facebook : https://www.facebook.com/th3m7J0'
      '\n      Instagram : Joseph_youcef198\n\n\n')


test = True
nbTest = 0

while test:
    try:
        targets = open(input('1 # /path/to/your/emails.txt => '),"r")
        test = False
    except:
        if (nbTest == 2):
            print("\n ಠ_ಠ  File Not Found ⚠\n\n")
            exit(0)
        print('Try again ...')
        nbTest+=1




# targets
emails = [email.split("\n")[0] for email in targets.readlines()]



print(' targets <= '+str(emails)+'\n\n')

# attacker

print('⚠️  --- Please enable less secure application access in your attacker account --- ⚠')
print('~(^-^)~ attacker info ~(^-^)~ ')

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

test = True
nbTest = 0

while test:
    try:
        attacker_email = input(' Enter Your Email  => ')
        attacker_password = getpass(prompt='( ͡° ͜ʖ ͡°) Enter Your Password => ', stream=None)
        server.login(attacker_email,attacker_password)
        test = False
    except:
        if (nbTest == 2):
            print("\n ಠ_ಠ  Wrong Username / Password ⚠\n\n")
            exit(0)
        print('Try again ...')
        nbTest += 1




# payload

msg = "how are you today I hope that everything is OK with you as it is my great pleasure to contact you in having communication with you starting from today,\n" \
      "i was just going through the Internet search when i found your email address, I want to make a very new and special friend,\n" \
      "so i decided to contact you to see how we can make it work if we can.\n" \
      "Please i wish you will have the desire with me so that we can get to know each other better and see what happens in future.\n" \
      "My name is Lisa Williams, I am an American  presently I live in the UK,\n" \
      "I will be very happy if you can write me through my private email address( xxx@x.x ) for easy communication so that we can know each other,\n" \
      "I will give you my pictures and details about me.\n\n\n" \
      "bye\n" \
      "Lisa\n"
subject = "Hi Dear,"
body = "Subject : {}\n\n{}".format(subject,msg)





# processing

numberOfEmails = int(input('\n\n2 # Number of emails => '))
sent = numberOfEmails
print('\n\n% processing % ... <= ')
for email in emails:
    print('+ target <= ' + email)
    for number in range(numberOfEmails):
        try:
            server.sendmail(attacker_email,email,body)
            print('('+str(number+1)+') sweet ✔')
        except:
            print('Error : Connection time out ..')
            sent-=1
    print(str(sent) + ' email(s) sent successfully to ' + email + ' ♥‿♥ ')
server.quit()

