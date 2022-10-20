import enum


class PeerType(enum.Enum):
    BUYER = "BUYER"
    SELLER = "SELLER"


peer_types = [ele for ele in PeerType]
