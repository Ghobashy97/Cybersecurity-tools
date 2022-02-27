import subprocess as spr
import threading as thr
import requests as req
import os
import MAC_changer as macch


def get_nat_table():
    spr.call("iptables")