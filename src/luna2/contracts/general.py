import logging
import common.make_tx
from luna2.contracts.config import CONTRACTS

CONTRACT_REDACTED_RONINS = "terra1hh9rgaxtmfqfkeqkruckwah6qc4ajlxgnweexyjeh4dsptkfnhmqeelzfl"


def handle_as_unknown(elem, txinfo):
    row = common.make_tx.make_unknown_tx(txinfo)
    return [row]


CONTRACTS[CONTRACT_REDACTED_RONINS] = handle_as_unknown
