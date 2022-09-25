from typing import List, Optional

from .shell import ShellCommand


class _Generic(ShellCommand):
    def __init__(
        self,
        image: str,
        subcmd: str,
        workdir: Optional[str] = None,
        volumes: Optional[List[str]] = None,
        **kwargs,
    ):
        super().__init__(
            image=image, command=["cargo", subcmd], workdir=workdir, volumes=volumes
        )


class Build(_Generic):
    def __init__(
        self,
        image: str,
        workdir: Optional[str] = None,
        volumes: Optional[List[str]] = None,
        **kwargs,
    ):
        super().__init__(image, "build", workdir, volumes, **kwargs)


class Check(_Generic):
    def __init__(
        self,
        image: str,
        workdir: Optional[str] = None,
        volumes: Optional[List[str]] = None,
        **kwargs,
    ):
        super().__init__(image, "check", workdir, volumes, **kwargs)


class Test(_Generic):
    def __init__(
        self,
        image: str,
        workdir: Optional[str] = None,
        volumes: Optional[List[str]] = None,
        **kwargs,
    ):
        super().__init__(image, "test", workdir, volumes, **kwargs)
