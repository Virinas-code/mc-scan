# -*- coding: utf-8 -*-
"""
Minecraft module.

Test Minecraft server.
"""
import ipaddress

import dns.resolver
import dramatiq
import mcstatus

from .status import Status


class Server:
    """Base server object."""

    def __init__(self, ip_address: ipaddress.IPv4Address):
        """
        Initialize server.

        :param ipaddress.IPv4Address ip_adress: Server IP.
        """
        self.ip_address: ipaddress.IPv4Address = ip_address
        self.host_name: str = (
            dns.resolver.resolve_address(self.ip_address.exploded)
            .rrset[0]
            .target.to_text(omit_final_dot=True)
        )
        self.status: Status = self._get_status()

    @dramatiq.actor()
    def _get_status(self) -> Status:
        """
        Fetch server status.

        :return modules.minecraft.status.Status: Current server status.
        """
        mcstatus_server: mcstatus.JavaServer = mcstatus.JavaServer(
            self.ip_address.exploded, timeout=10
        )
        return Status(mcstatus_server.status())
