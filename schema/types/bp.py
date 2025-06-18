from dataclasses import dataclass

from flask import Blueprint


@dataclass
class BlueprintConfig:
    name: str
    bp: Blueprint
    url_prefix: str
