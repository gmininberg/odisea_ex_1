#!/usr/bin/env python
from scapy.all import *
from twisted.protocols import sip #should be good sip lib but can use any other sip lib.
import sys, getopt

outputPath = ''

def post_output_for_test():
    #post the output files (caller and callee) to check in the exxrcise server

#code info that got the codec and and its payloadType
class codecInfo(object):
    """docstring for dialog"""
    def __init__(self, codecName, payloadType, portSource, portDest):
        super(dialog, self).__init__()
        self.codecName = codecName
        self.payloadType = payloadType
        self.portSource = portSource
        self.portDest = portDest


neg_codec_info = codecInfo("", -1)

#sdp description:
#codeinfo - array of all codecs.
#seq number - number of the request.
#isLocal - local or remote sdp.
class sdpDescription(object):
    """docstring for sdpDescription"""
    def __init__(self, codecInfoArr, seqNum, isLocal):
        super(sdpDescription, self).__init__()
        for codecInfo in codecInfoArr:
            self.codecInfoArr.append(codecInfo)
        self.seqNum = seqNum
        self.isLocal = isLocal

def is_register_request(buf):
    #chcke for the local user address will need that later
    pass

def is_invite(buf):
    #check if the SIP is inivte or 200OK for invite
    pass

def is_bye(buf):
    #check if the call is ended.
    pass

def is_invite_dialog_close():
    #check if invite got 200 OK (can be both remote or local invite)
    pass

def set_neg_codec():
    #once a dialog is closed then get the codec we are using set the selected codecInfo
    neg_codec_info.codecName = "____the_name_of_the_codec_from_the_sdp____"
    neg_codec_info.payloadType = -1 #the payload of the codec from the sdp.

def read_sdp(buf):
    #read the sdp (invite and 200OK) use sdpDescription for saving data
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
    if neg_codec_info.portSource == sorce_port and neg_codec_info.portDest == dest_port:
        return true
    return false

def check_is_sip(buf):
    pass

def check_is_rtp(sorce_port, dest_port):
    if neg_codec_info.portSource == sorce_port and neg_codec_info.portDest == dest_port or neg_codec_info.portSource == dest_port and neg_codec_info.portDest == sorce_port:
        return true
    return false

def check_is_rtcp(buf):
    pass

def analyze_voip(pcap):
    
    for line in pcap:
        #take line and decode it to buffer
        buf = ''
        if check_is_sip(buf):
            #read and understand the sip message
            if is_register_request(buf):
                #save some meta data
            
            if is_invite(buf):
                read_sdp(buf)
                if is_invite_dialog_close():
                    set_neg_codec()

            if is_bye(buf):
                #the call is ended
                break

        elif check_is_rtp(_sorce_port_, _dest_port_):
            #read and understand the rtp message, and wtite it to file
            if check_rtp_valid(buf):
                if is_local_rtp(buf):
                    write_rtp_stream_to_file(convert_rtp_buf_to_stream(buf), localFileName_place_holder)
                else:
                    write_rtp_stream_to_file(convert_rtp_buf_to_stream(buf), remoteFileName_place_holder)
        elif check_is_rtcp(buf):
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

    print 'Input file is \n', inputfile
    print 'Output path is \n', outputPath
    pcap = rdpcap(inputfile)
    analyze_voip(pcap)

if __name__ == "__main__":
   main(sys.argv[1:])
