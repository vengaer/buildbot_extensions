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
                self.command.append(f"-v{vol}:/{vol}:Z")

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

    def __init__(self, **kwargs):
        self.command = "docker system prune -f"
        super().__init__(**kwargs)


class Volume(shell.ShellCommand):
    """Create a docker volume"""

    name = "docker volume"

    def __init__(self, volume, **kwargs):
        self._volume = volume
        self.command = ["docker", "volume", "create", volume]
        super().__init__(**kwargs)

    @property
    def volume(self):
        """Get name of the volume"""
        return self._volume
