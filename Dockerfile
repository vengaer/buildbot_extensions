FROM archlinux:latest
LABEL maintainer="vilhelm.engstrom@tuta.io"

COPY . /buildbot-extensions
WORKDIR /buildbot-extensions

RUN useradd -m builder                                      && \
    pacman -Syu --noconfirm --needed python-{black,pylint}     \
                                     mypy                   && \
    chown -R builder:builder /buildbot-extensions

USER builder
