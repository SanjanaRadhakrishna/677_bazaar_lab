

from abc import ABC, abstractmethod

from enums.peer_type import PeerType


class CommonOps(ABC):
    def __init__(self, peer_type: PeerType):
        self._peer_type = peer_type

    def lookup(self):
        pass

    def reply(self):
        pass