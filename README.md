# odisea_ex_1

# WIFI
Network : VonageGuest (Click on -  'Already have an account? Sign in' at the buttom of the page ) 
Username	91406096
Password	029328

# how to use Twisted
you can look at this example: http://cs.uccs.edu/~cs526/svoip/src/shtoom/shtoom/sip.py
but this is the main flow you need:
```
def sipMessageReceived(message):
    print("message %s headers %s body %s"%(message, message.headers, message.body))


def parse_sip_message(buf):
    mp = tpsip.MessagesParser(sipMessageReceived)
    mp.dataReceived(buf)
    mp.dataDone()
```


here are some examples of output of this function:
# Register request:
```
message <SIP Request 4479067488:REGISTER sip:a143131.ac1.vbspbx.com:10000> 

headers OrderedDict([('via', ['SIP/2.0/TCP 192.168.1.24:53400;rport;branch=z9hG4bKPjnwEPC8blILc33PZHISf9hYajKfG7J3Zt']), ('max-forwards', ['70']), ('from', ['<sip:VH4145259@a143131.ac1.vbspbx.com>;tag=sGpud7aX6O7F6oE8Mb6vozD6jt-MQsX7']), ('to', ['<sip:VH4145259@a143131.ac1.vbspbx.com>']), ('call-id', ['LD.Hi4WVgRzUwyv7.OyV8vyiLNKlgAp0']), ('cseq', ['35572 REGISTER']), ('x-connect-type', ['Wifi']), ('user-agent', ['MacBookPro14_3-VoXIPTestApplication-0.7-MacOSX-10.13.6']), ('voxip-version', ['0_7_07']), ('contact', ['<sip:VH4145259@192.168.1.24:53400;transport=TCP>']), ('expires', ['300']), ('allow', ['INVITE, ACK, BYE, CANCEL, INFO, NOTIFY, REFER, OPTIONS']), ('content-length', ['0'])]) 

body 
```

# Register response:
```
message <SIP Response 4479139920:200> 
headers OrderedDict([('via', ['SIP/2.0/TCP 192.168.1.24:53400;received=5.28.134.187;rport=53400;branch=z9hG4bKPjJkQ0fwoc4RwJGiFCUsTl-I4IBYzAuXuH']), ('from', ['<sip:VH4145259@a143131.ac1.vbspbx.com>;tag=sGpud7aX6O7F6oE8Mb6vozD6jt-MQsX7']), ('to', ['<sip:VH4145259@a143131.ac1.vbspbx.com>;tag=de565de9d964914eeb5e9a2408f3d448.5b20']), ('call-id', ['LD.Hi4WVgRzUwyv7.OyV8vyiLNKlgAp0']), ('cseq', ['35573 REGISTER']), ('contact', ['<sip:VH4145259@192.168.1.24:53400;transport=TCP>;expires=300;received="sip:52.200.86.166:5060"']), ('server', ['Vonage']), ('content-length', ['0'])]) 
body 
```

# invite:
```
message <SIP Request 4479125768:INVITE sip:VH4145259@192.168.1.24:53400> 
headers OrderedDict([('via', ['SIP/2.0/TCP 52.200.86.166:10000;branch=z9hG4bKddfd.60977412.0']), ('max-forwards', ['63']), ('from', ['"Guy Mininberg" <sip:934@10.201.135.100>;tag=S6cvN54v8vZaD']), ('to', ['<sip:VH4145259@internal-sip.vocalocity.com>']), ('call-id', ['6f2330e3-ac9a-1237-7d9c-0e2ab6e304d2']), ('cseq', ['609962 INVITE']), ('contact', ['<sip:gw+controller1@52.200.86.166:10000;transport=tcp;did=8e9.2344a541>']), ('user-agent', ['Vonage H2O PBX']), ('supported', ['timer, path, replaces']), ('session-expires', ['1200;refresher=uac']), ('min-se', ['90']), ('content-type', ['application/sdp']), ('content-disposition', ['session']), ('content-length', ['436']), ('x-carrier-id', ['Partner Israel']), ('x-hdap-accountid', ['143131']), ('allow', ['INVITE, ACK, BYE, CANCEL, OPTIONS, MESSAGE, INFO, REGISTER, REFER, NOTIFY'])]) 
body:
v=0
o=H2O 1550300280 1550300281 IN IP4 3.90.141.90
s=H2O
c=IN IP4 3.90.141.90
t=0 0
m=audio 22074 RTP/AVP 121 0 101
a=rtpmap:121 opus/48000/2
a=fmtp:121 useinbandfec=1; maxaveragebitrate=14400; maxplaybackrate=48000; ptime=20; minptime=10; maxptime=40
a=rtpmap:0 PCMU/8000
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-16
a=rtcp-mux
a=rtcp:22075 IN IP4 3.90.141.90
a=silenceSupp:off - - - -
a=ptime:20
a=nortpproxy:yes
```

# SDP:
you can use this example to read the SDP: https://www.kamailio.org/wiki/scripts/python/sdp-parser (keep in mind that the SDP you have is different from the one in the example)

# RTP:
you will have to use bytearray out of the udp[RAW]. just a hint: the header size is 12 byte.
this is the RFC https://tools.ietf.org/html/rfc3550#page-13 (we dont have contributing source (CSRC) identifiers) use the RFC to find the payload type of the RTP.

# wave:
wavfile = wave.open(fieName, 'wb')
wavfile.setnchannels(1)
wavfile.setframerate(8000)
wavfile.setsampwidth(2)
wavfile.writeframesraw(bytearray) or wavfile.writeframes(bytearray)
read more at: https://docs.python.org/2/library/wave.html#module-wave


# GOOD LUCK!!! (there is a cool prize for the winners)
