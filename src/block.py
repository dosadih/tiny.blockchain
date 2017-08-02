#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib as hasher
import datetime as date


class Block:

    def __init__(self, index, timestamp, data, previous_hash):
        """class constructor"""
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        """Return the hash of the block"""
        sha = hasher.sha256()
        sha.update(str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash))

        return sha.hexdigest()


def create_genesis_block():
    """Manually construct a block with index zero and arbitrary previous hash"""
    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    """This function cosntructs a block of data"""
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)
