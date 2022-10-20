from enums.peer_type import PeerType
from shopping.ops import CommonOps


class BuyerOps(CommonOps):
    def __init__(self):
        super().__init__(peer_type=PeerType.BUYER)




