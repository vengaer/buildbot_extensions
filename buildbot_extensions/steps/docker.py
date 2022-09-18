''' Docker-related buildbot steps '''

import os

from buildbot.steps import shell  # pylint: disable=import-error

class Docker(shell.ShellCommand):
    ''' Wrapper for running shell commands inside docker container '''
    name = "docker"

    def __init__(self, container, command, workdir, **kwargs):
        self._container = container
        self.command = [
            "docker",
            "run",
            "--rm",
            "-t",
            "--net=host",
            f"-u{os.geteuid()}",
            f"-w={workdir}",
            container,
        ] + command
        super().__init__(**kwargs)

class Prune(shell.ShellCommand):
    ''' Step removing dangling docker containers '''
    name = 'prune'
    command = 'docker system prune -f'
