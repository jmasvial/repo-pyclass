#!/usr/bin/env python3

from netmiko import ConnectHandler
from pprint import pprint


def prompt(**sw):
    con = ConnectHandler(**sw)
    out = con.find_prompt()
    pprint(out)


device = {
    "username" : "pyclass",
    "password" : "88newclass",
    "host" : "arista1.lasthop.io",
    "device_type" : "arista_eos",
    #"fast_cli" : True
    }


#con = ConnectHandler(**device)

#out = con.find_prompt()
#pprint(out)


prompt(device)
