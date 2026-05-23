"""Quantum entropy generation utilities."""

import os
import hashlib
import logging
from typing import Optional
import struct
import time

logger = logging.getLogger(__name__)


class QuantumEntropyGenerator:
    def __init__(self):
        self._pool = bytearray()
        self._counter = 0

    def add_entropy(self, data: bytes):
        self._pool.extend(data)
        if len(self._pool) > 4096:
            self._pool = self._pool[-2048:]
        self._counter += 1

    def generate(self, num_bytes: int = 32, use_quantum: bool = True) -> bytes:
        self.add_entropy(os.urandom(16))
        self.add_entropy(struct.pack('d', time.time()))
        self.add_entropy(os.urandom(8))
        if use_quantum and self._counter > 0:
            seed = hashlib.sha3_512(bytes(self._pool) + os.urandom(16)).digest()
            return seed[:num_bytes]
        return os.urandom(num_bytes)

    def reseed(self):
        self._pool = bytearray(os.urandom(64))
        self._counter = 0

    @staticmethod
    def generate_quantum_random_bits(num_bits: int = 256) -> str:
        entropy = os.urandom((num_bits + 7) // 8)
        bits = ''.join(format(b, '08b') for b in entropy)[:num_bits]
        return bits


def generate_quantum_entropy(num_bytes: int = 32) -> bytes:
    gen = QuantumEntropyGenerator()
    return gen.generate(num_bytes)
