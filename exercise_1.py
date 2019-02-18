#!/usr/bin/env python
from scapy.all import *
from twisted.protocols import sip #should be good sip lib but can use any other sip lib.
import sys, getopt
import wave

outputPath = ''

def post_output_for_test():
    print "!!!!!!!! call Guy to check the result !!!!!!!!"

#code info that got the codec and and its payloadType
class codecInfo(object):
    """docstring for dialog"""
    def __init__(self, codecName, payloadType):
        super(codecInfo, self).__init__()
        self.codecName = codecName
        self.payloadType = payloadType


#sdp description:
#codeinfo - array of all codecs.
#seq number - number of the request.
#isLocal - local or remote sdp.
#port - the port of the audio
class sdpDescription(object):
    """docstring for sdpDescription"""
    def __init__(self, codecInfoArr, seqNum, isLocal, port):
        super(sdpDescription, self).__init__()
        for codecInfo in codecInfoArr:
            self.codecInfoArr.append(codecInfo)
        self.seqNum = seqNum
        self.isLocal = isLocal
        self.port = port


def is_register_request():
    #chcke for the local user address will need that later
    pass

def is_invite():
    #check if the SIP is inivte or 200OK for invite
    pass

def is_bye():
    #check if the call is ended.
    pass

def is_invite_dialog_close():
    #check if invite got 200 OK (can be both remote or local invite)
    pass

def set_neg_codec():
    #once a dialog is closed then get the codec we are using set the selected codecInfo
    pass

def read_sdp(buf):
    #read the sdp (invite and 200OK) use sdpDescription for saving data
    pass

def check_rtp_valid(buf):
    #remember to be sure its the correct payload type!!!!
    pass

def is_local_rtp(line):
    #check the ports of the message to know that
    pass

def check_is_sip(line):
    #check in the hreaders if you have "SIP/2.0" string
    pass

def check_is_rtp(sorce_port, dest_port):
    #check if the ports are rtp ports
    pass

def check_is_rtcp(sorce_port, dest_port):
    #for this exercise its not relevant
    return False

def analyze_voip(pcap):

    for line in pcap:
        #take line and decode it to buffer
        if check_is_sip(line):
            #read and understand the sip message
            #read the sip message... in the read.me there is example how to do it.
            if is_register_request():
                #save some meta data
                pass
            
            if is_invite():
                read_sdp(line)
                if is_invite_dialog_close():
                    set_neg_codec()

            if is_bye():
                #the call is ended
                break

        elif check_is_rtp(_sorce_port_, _dest_port_):
            #read and understand the rtp message, and wtite it to file
            if check_rtp_valid(line):
                if is_local_rtp(line):
                    #write the raw data as wave to local file
                    pass
                else:
                    #write the raw data as wave to remote file
                    pass
        elif check_is_rtcp(_sorce_port_, _dest_port_):
            #do nothing for now (will use rtcp in exercise 2)
            pass
        else:
            #ignore
            pass
    post_output_for_test()
    print 'done!!!'
        
def main(argv):
   inputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:")
   except getopt.GetoptError:
      print 'exercise_1.py -i <inputfile>'
      sys.exit()
   for opt, arg in opts:
        if opt == '-h':
            print 'exercise_1.py -i <inputFile> -o <outputPath>'
            sys.exit()
        elif opt in ("-i"):
            inputfile = arg
        elif opt in ("-o"):
            outputPath = arg
        else:
            print 'exercise_1.py -i <inputfile>'
            sys.exit()

    pcap = PcapReader(inputfile)
    analyze_voip(pcap)

if __name__ == "__main__":
   main(sys.argv[1:])
