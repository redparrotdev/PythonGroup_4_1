"""
Interface segregation principle
Принцип разделения интерфейсов

Класс не должен зависеть от методов, которые не использует
"""

from abc import ABC, abstractmethod


class CanPrint(ABC):

    @abstractmethod
    def print_data(self): pass


class CanFax(ABC):

    @abstractmethod
    def send_fax(self): pass


class CanScan(ABC):

    @abstractmethod
    def scan_file(self): pass


class BasicPrinter(CanPrint):
    ...


class MFD(CanPrint, CanScan, CanFax):
    ...
