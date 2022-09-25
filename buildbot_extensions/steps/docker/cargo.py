import abc
from typing import List, Optional

from .shell import ShellCommand


class _CargoCmd(ShellCommand, abc.ABC):
    """Wrapper running generic cargo command in docker container"""

    def __init__(
        self,
        image: str,
        workdir: Optional[str] = None,
        volumes: Optional[List[str]] = None,
        **kwargs,
    ):
        super().__init__(
            image=image,
            command=["cargo", self.subcmd],
            workdir=workdir,
            volumes=volumes,
        )

    @property
    @abc.abstractmethod
    def subcmd(self) -> str:
        ...


class Build(_CargoCmd):
    name = "Cargo Build"

    @property
    def subcmd(self) -> str:
        return "build"


class Check(_CargoCmd):
    name = "Cargo Check"

    @property
    def subcmd(self) -> str:
        return "check"


class Test(_CargoCmd):
    name = "Cargo Test"

    @property
    def subcmd(self) -> str:
        return "test"


class Doc(_CargoCmd):
    name = "Cargo Doc"

    @property
    def subcmd(self) -> str:
        return "doc"
