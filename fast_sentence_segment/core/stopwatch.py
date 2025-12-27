# -*- coding: utf-8 -*-
"""Simple stopwatch for timing operations."""

import time


class Stopwatch:
    """A simple stopwatch for measuring elapsed time."""

    def __init__(self):
        self._start = time.perf_counter()
        self._end = None

    @property
    def duration(self):
        return self._end - self._start if self._end else time.perf_counter() - self._start

    @property
    def running(self):
        return not self._end

    def restart(self):
        self._start = time.perf_counter()
        self._end = None
        return self

    def stop(self):
        if self.running:
            self._end = time.perf_counter()
        return self

    def __str__(self):
        ms = self.duration * 1000
        if ms >= 1000:
            return f'{ms / 1000:.2f}s'
        if ms >= 1:
            return f'{ms:.2f}ms'
        return f'{ms * 1000:.2f}μs'
