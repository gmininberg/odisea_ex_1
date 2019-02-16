#!/usr/bin/env python
import dpkt
from twisted.protocols import sip #should be good sip lib but can use any other sip lib.

import sys, getopt

outputPath = ''

#make SDP dialog class which discribes the SDP codec.
class dialog(object):
    """docstring for dialog"""
    def __init__(self, codecs, payloads):
        super(dialog, self).__init__()
        self.arg = arg

def post_output_for_test():
    #post the output files (caller and callee) to check in the exxrcise server

def is_register_request(buf):
    #chcke for the local user address will need that later
    pass

def is_invite(buf):
    #check if the SIP is inivte or 200OK for invite
    pass

def is_invite_dialog_close():
    #check if invite got 200 OK
    pass

def set_neg_codec(dialog):
    #once a dialog is closed then get the codec we are using
    pass

def read_sdp(buf):
    #read the sdp (invite and 200OK)
    pass

def check_rtp_valid(buf):
    #remember to be sure its the correct payload type!!!!
    pass

def convert_rtp_buf_to_stream(buf):
    #rememeber wav file is binary...
    pass

def write_rtp_stream_to_file(stream, fileName):
    #write the stream to file
    pass

def is_local_rtp(buf):
    #check if local rtp (by the ip)
    pass

def check_is_sip(buf):
    pass

def check_is_rtp(buf):
    pass

def check_is_rtcp(buf):
    pass

def analyze_voip(pcap):
    for line in pcap:
        #take line an d decode it buffer
        buf = ''
        if check_is_sip(buf):
            #read and understand the sip message
            if is_register_request(buf):
                #save some meta data
            
            if is_invite(buf):
                read_sdp(buf)
                if is_invite_dialog_close():
                    set_neg_codec(dialog)

        elif check_is_rtp(buf):
            #read and understand the rtp message, and wtite it to file
            if check_rtp_valid(buf):
                if is_local_rtp(buf):
                    write_rtp_stream_to_file(convert_rtp_buf_to_stream(buf), localFileName)
                else:
                    write_rtp_stream_to_file(convert_rtp_buf_to_stream(buf), remoteFileName)
        elif check_is_rtcp(buf):
            #do nothing for now (will use rtcp in exercise 2)
            pass
        else:
            #ignore
            pass
        
def main(argv):
   inputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:")
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

   print 'Input file is ', inputfile
   with open(inputfile, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        analyze_voip(pcap)

if __name__ == "__main__":
   main(sys.argv[1:])
