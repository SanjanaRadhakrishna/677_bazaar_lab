import random
from typing import List

from peer.model import Peer
from enums.peer_type import PeerType

from utils import get_free_port


class PeerGenerator:
    def __init__(self,
                 num_peers: int,
                 peer_types: List[PeerType],
                 item_quantities_map: dict,
                 max_hop_count: int = 10,
                 ):
        self._host = "localhost"
        self._num_peers = num_peers
        self._peer_types = peer_types
        self._max_hop_count = max_hop_count
        self._item_quantities_map = item_quantities_map

    def _get_peer(self, id: int) -> Peer:
        items = list(self._item_quantities_map.keys())

        selected_item = random.choice(items)
        selected_peer_type = self._peer_types[id % len(self._peer_types)]

        final_quantity = self._item_quantities_map[selected_item] if selected_peer_type == PeerType.SELLER else None

        return Peer(id=id,
                    host=self._host,
                    neighbours=set(),
                    peer_type=selected_peer_type,
                    item=selected_item,
                    available_item_quantity=final_quantity,
                    port=get_free_port(),
                    max_hop_count=self._max_hop_count
                    )

    def init_and_get_peers(self) -> List[Peer]:
        return [self._get_peer(i) for i in range(0, self._num_peers)]

