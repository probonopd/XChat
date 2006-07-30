#! /usr/bin/python

import dbus

bus = dbus.SessionBus()
proxy_obj = bus.get_object('org.xchat.service', '/org/xchat/Manager')
manager = dbus.Interface(proxy_obj, 'org.xchat.manager')
path = manager.Connect ()
proxy_obj = bus.get_object('org.xchat.service', path)
xchat = dbus.Interface(proxy_obj, 'org.xchat.remote')

channels = xchat.ListGet ("channels")
while xchat.ListNext (channels):
	name = xchat.ListStr (channels, "channel")
	print "------- " + name + " -------"
	xchat.SetContext (xchat.ListInt (channels, "context"))
	users = xchat.ListGet ("users")
	while xchat.ListNext (users):
		print xchat.ListStr (users, "nick")
	xchat.ListFree (users)
xchat.ListFree (channels)
