#!/usr/bin/env python

from ncclient import manager

device = manager.connect(host='vmx', port=830, username='admin', password='3159106t',
                         hostkey_verify=False, device_params={}, allow_agent=False,
                         look_for_keys=False)

get_filter = """
<configuration>
    <system>
        <login>
        </login>
    </system>
</configuration>
"""
nc_get_reply = device.get(('subtree', get_filter))

user_list = []

xmlns

