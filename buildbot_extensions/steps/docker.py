""" Docker-related buildbot steps """

import os

from buildbot.steps import shell  # pylint: disable=import-error


class Docker(shell.ShellCommand):
    """Wrapper for running shell commands inside docker container"""

    name = "docker"

    def __init__(self, image, command, workdir=None, **kwargs):
        self._image = image
        self.command = ["docker", "run", "--rm", "-t", "--net=host"]

        if workdir is not None:
            self.command.append(f"-w={workdir}")

        self.command.append(image)
        self.command += command
        super().__init__(**kwargs)

    @property
    def image(self):
        """Docker image name"""
        return self._image


class Build(shell.ShellCommand):
    """Shell wrapper building docker images"""

    name = "docker build"

    def __init__(self, dockerfile, tag, **kwargs):
        if not (ddir := os.path.dirname(os.path.abspath(dockerfile))):
            ddir = "."

        self.command = [
            "docker",
            "build",
            ddir,
            f"-t{tag}",
            "--network=host",
        ]
        super().__init__(**kwargs)


class Prune(shell.ShellCommand):
    """Step removing dangling docker containers"""

    name = "docker prune"
    command = "docker system prune -f"
