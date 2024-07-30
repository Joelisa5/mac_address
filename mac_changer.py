#!/usr/bin/env python3

import subprocess
interface = input("interface > ")
new_mac = input("mac address > ")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

print("the new mac address is "+new_mac)
