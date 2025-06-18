from abc import ABC, abstractmethod
from threading import Lock

from flask import Flask


class BaseExtension(ABC):
    _instances = {}
    _lock: Lock = Lock()

    @classmethod
    def instances(cls):
        return cls._instances

    def __new__(cls, *args, **kwargs):
        if cls is BaseExtension:
            return super().__new__(cls)
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]

    def __init__(self, enabled: bool = True):
        if getattr(self, "_initialized", False):
            return
        self.enabled = enabled
        self._initialized = True

    def init_app(self, app: Flask):
        if self.enabled:
            self._init_app(app)
        else:
            raise (f"[{self.__class__.__name__}] 未启用，跳过注册")

    @abstractmethod
    def _init_app(self, app: Flask):
        """子类必须实现具体注册逻辑"""
        raise NotImplementedError
