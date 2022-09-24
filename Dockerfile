FROM archlinux:latest
LABEL maintainer="vilhelm.engstrom@tuta.io"

COPY . /buildbot-extensions
WORKDIR /buildbot-extensions

RUN useradd -m builder                              && \
    pacman -Syu --noconfirm --needed python-pylint  && \
    chown -R builder:builder /buildbot-extensions

USER builder
