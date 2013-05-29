#!/usr/bin/env python

#MyfirtPythonScript

interfaces = input("Please enter number of interfaces?\n")
#Basic Zone Based Firewall config
inside = raw_input("Please specify the name of the inside lan interface? Ex. FastEthernet0/1\n")
outside = raw_input("Please spcify the name of the outside interface? Ex. FastEthernet0/0\n")
print ("\n")
print ("!!Copy after this line down!!\n")
print ("policy-map type inspect InsideToOutside")
print ("class class-default")
print ("inspect")
print ("!")
print ("zone security Inside")
print ("description Inside network")
print ("zone security Outside")
print ("description Outside network")
print ("zone-pair security InsideToOutside source Inside destination Outside")
print ("service-policy type inspect InsideToOutside")
print ("!")
print ("interface %s" %inside)
print ("zone-member security Inside")
print ("!")
print ("interface %s" %outside)
print ("zone-member security Outside\n")
print ("!!End of config!!")
