#!/usr/bin/python3

import logging,re,sys

try :    from dd_util      import *
except : from sara.dd_util import *

class dd_config:

    def __init__(self,logger,config=None,args=None):
        self.logger = logger

    def args(self,args):
        if args == None : return

        i = 0
        while i < len(args):
              n = self.option(args[i:])
              if n == 0 : n = 1
              i = i + n

    def config(self,path):
        if path == None : return

        # keep root config_path
        if self.config_path == None :
           self.config_path = path

        try:
            f = open(path, 'r')
        except:
            (type, value, tb) = sys.exc_info()
            self.logger.error("Type: %s, Value: %s" % (type, value))
            return 

        for line in f.readlines():
            words = line.split()
            if (len(words) >= 2 and not re.compile('^[ \t]*#').search(line)):
                self.option(words)

        f.close()

    def defaults(self):

        self.ask4help             = False

        self.blocksize            = 0

        self.config_path          = None

        self.debug                = False

        self.destination_path     = None

        self.document_root        = None

        self.flags                = Flags()
        self.flags_str            = 'd'
        self.flags.from_str(self.flags_str)

        self.post_broker          = URL()
        self.post_broker.set('amqp://guest:guest@localhost/')

        self.post_exchange        = None

        self.post_topic_key       = None

        self.randomize            = False

        self.reconnect            = True

        self.source               = URL()
        self.source.set('amqp://guest:guest@localhost/')

        self.tag                  = 'default'

        #

        self.destination          = URL()
        self.destination.set('amqp://guest:guest@localhost/')
        self.destination_exchange = 'sx_guest'

        self.exchange_key         = []

        self.instances            = 0


        self.recompute_chksum     = False


    def isTrue(self,s):
        if  s == 'True' or s == 'true' or s == 'yes' or s == 'on' or \
            s == 'Yes'  or s == 'YES' or s == 'TRUE' or s == 'ON' or \
            s == '1'    or s == 'On' :
            return True
        else:
            return False


    def option(self,words):

        n = 0
        try:
                if   words[0] in ['blocksize','-bz','--blocksize']:
                     self.blocksize = chunksize_from_str(words[1])
                     n = 2

                elif words[0] in ['config','-c','--config']:
                     self.config(words[1])
                     n = 2

                elif words[0] in ['debug','-debug','--debug']:
                     if words[0][0:1] == '-' : 
                        self.debug = True
                        n = 1
                     else :
                        self.debug = self.isTrue(words[1])
                        n = 2
                     if self.debug :
                        self.logger.setLevel(logging.DEBUG)

                elif words[0] in ['destination_path','-dp','--destination_path']:
                     self.destination_path = words[1]
                     n = 2

                elif words[0] in ['document_root','-dr','--document_root']:
                     self.document_root = words[1]
                     n = 2

                elif words[0] in ['flags','-f','--flags']:
                     self.str_flags = words[1] 
                     self.flags.from_str(self.str_flags)
                     n = 2

                elif words[0] in ['help','-h','-help','--help']:
                     self.ask4help = True
                     n = 1

                elif words[0] in ['post_broker','-pb','--post_broker'] :
                     self.post_broker.set(words[1])
                     n = 2

                elif words[0] in ['post_exchange','-pe','--post_exchange'] :
                     self.post_exchange = words[1]
                     n = 2

                elif words[0] in ['post_topic_key','-pk','--post_topic_key'] :
                     self.post_topic_key = words[1]
                     n = 2

                elif words[0] in ['randomize','-r','--randomize']:
                     if words[0][0:1] == '-' : 
                        self.randomize = True
                        n = 1
                     else :
                        self.randomize = self.isTrue(words[1])
                        n = 2

                elif words[0] in ['recompute_chksum','-rc','--recompute_chksum']:
                     if words[0][0:1] == '-' : 
                        self.recompute_chksum = True
                        n = 1
                     else :
                        self.recompute_chksum = self.isTrue(words[1])
                        n = 2

                elif words[0] in ['reconnect','-rr','--reconnect']:
                     if words[0][0:1] == '-' : 
                        self.reconnect = True
                        n = 1
                     else :
                        self.reconnect = self.isTrue(words[1])
                        n = 2

                elif words[0] in ['source','-s','--source']:
                     self.source.set(words[1])
                     n = 2
                elif words[0] in ['tag','-t','--tag']:
                     self.tag = words[1] 
                     n = 2


                elif words[0] in ['destination_exchange','-de','--destination_exchange']:
                     self.dest_exchange = words[1]
                     n = 2
                elif words[0] in ['destination','-d','--destination'] :
                     self.destination.set(words[1])
                     n = 2
                elif words[0] in ['exchange_key','-ek','--exchange_key']:
                     self.exchange_key.append(words[1])
                     n = 2
                elif words[0] in ['instances','-i','--instances']:
                     self.instances = int(words[1])
                     n = 2

                elif words[0] in ['source_exchange','-se','--source_exchange']:
                     self.src_exchange = words[1]
                     n = 2
                elif words[0] in ['ssh_keyfile','-sk','--ssh_keyfile']:
                     self.ssh_keyfile = words[1]
                     n = 2
                elif words[0] in ['strip','-st','--strip']:
                     self.strip = int(words[1])
                     n = 2
                elif words[0] in ['transmission_url','-tr','--transmission_url']:
                     self.transmission.set(words[1])
                     n = 2
                elif words[0] in ['transmission_document_root','-tdr','--transmission_document_root']:
                     self.trx_document_root = words[1]
                     n = 2


                elif words[0] in ['clustered','-cl','--clustered']:
                     if words[0][0:1] == '-' : 
                        self.clustered = True
                        n = 1
                     else :
                        self.clustered = self.isTrue(words[1])
                        n = 2
        except:
                pass

        return n
