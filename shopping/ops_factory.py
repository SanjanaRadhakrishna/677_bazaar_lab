from enums.peer_type import PeerType
from shopping.buyer_ops import BuyerOps
from shopping.seller_ops import SellerOps


class OpsFactory:

    @staticmethod
    def get_ops(type: PeerType):
        if type == PeerType.SELLER:
            return SellerOps()

        if type == PeerType.BUYER:
            return BuyerOps()
