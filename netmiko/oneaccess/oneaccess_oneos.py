"""Netmiko driver for OneAccess ONEOS"""

from __future__ import print_function
from __future__ import unicode_literals

from netmiko.cisco_base_connection import CiscoBaseConnection
import time


class OneaccessOneos(CiscoBaseConnection):
    def __init__(self, *args, **kwargs):
        """Init connection - similar as Cisco"""
        default_enter = kwargs.get("default_enter")
        kwargs["default_enter"] = "\r\n" if default_enter is None else default_enter
        super(OneaccessOneos, self).__init__(*args, **kwargs)

    def session_preparation(self):
        """Prepare connection - disable paging"""
        self._test_channel_read()
        self.set_base_prompt()
        self.disable_paging(command="term len 0")
        # Clear the read buffer
        time.sleep(0.3 * self.global_delay_factor)
        self.clear_buffer()

    def save_config(self, cmd="write mem", confirm=False):
        """Save config: write mem"""
        return super(OneaccessOneos, self).save_config(cmd=cmd, confirm=confirm)


class OneaccessOneosSSH(OneaccessOneos):
    pass


class OneaccessOneosTelnet(OneaccessOneos):
    pass
