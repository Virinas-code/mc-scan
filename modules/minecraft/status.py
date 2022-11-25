# -*- coding: utf-8 -*-
"""
Minecraft status module.

Minecraft server status.
"""
from mcstatus.pinger import PingResponse

from .constants import PROTOCOLS


class Status:
    """Status object."""

    def __init__(self, status: PingResponse):
        """
        Load status.

        :param mcstatus.PingResponse status: mcstatus status.
        """
        self.ping: float = status.latency
        self.version: str = status.version.name
        self.protocol: int = status.version.protocol
        self.protocol_version: list[str] = PROTOCOLS.get(
            self.protocol, [self.version]
        )
