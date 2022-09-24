FROM archlinux:latest
LABEL maintainer="vilhelm.engstrom@tuta.io"

RUN useradd -m builder

COPY . /buildbot-extensions

RUN pacman -Syu --noconfirm --needed python-pylint

WORKDIR /buildbot-extensions
RUN chown -R builder:builder /buildbot-extensions
USER builder
