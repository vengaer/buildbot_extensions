""" Docker-related buildbot steps """

from buildbot.steps import shell  # pylint: disable=import-error


class Docker(shell.ShellCommand):
    """Wrapper for running shell commands inside docker container"""

    name = "docker"

    def __init__(self, image, command, workdir=None, volumes=None, **kwargs):
        self._image = image
        self.command = ["docker", "run", "--rm", "-t", "--net=host"]

        if workdir is not None:
            self.command.append(f"-w={workdir}")

        if volumes is not None:
            for vol in volumes:
                self.command.append(f"-v{vol}:/{vol}")

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

    def __init__(self, tag, path=".", **kwargs):
        self.command = [
            "docker",
            "build",
            path,
            f"-t{tag}",
            "--network=host",
        ]
        super().__init__(**kwargs)


class Prune(shell.ShellCommand):
    """Step removing dangling docker containers"""

    name = "docker prune"
    command = "docker system prune -f"


class Volume(shell.ShellCommand):
    """Create a docker volume"""

    name = "docker volume"

    def __init__(self, name, **kwargs):
        self._name = name
        self.command = ["docker", "volume", "create", self._name]
        super().__init__(**kwargs)

    @property
    def volume_name(self):
        """Get name of the volume"""
        return self._name
