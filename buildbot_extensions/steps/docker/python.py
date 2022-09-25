import abc
from typing import List, Optional

from .shell import ShellCommand


class _Check(ShellCommand, abc.ABC):
    def __init__(
        self,
        image: str,
        module: str,
        workdir: Optional[str] = None,
        volumes: Optional[List[str]] = None,
        **kwargs,
    ):
        super().__init__(
            image=image,
            command=self.prefix + [module],
            workdir=workdir,
            volumes=volumes,
        )

    @property
    @abc.abstractmethod
    def prefix(self) -> List[str]:
        ...


class Pylint(_Check):
    name = "Pylint"

    @property
    def prefix(self) -> List[str]:
        return ["pylint"]


class Black(_Check):
    name = "Black"

    @property
    def prefix(self) -> List[str]:
        return ["black", "--check"]


class Mypy(_Check):
    name = "Mypy"

    @property
    def prefix(self) -> List[str]:
        return ["mypy"]
