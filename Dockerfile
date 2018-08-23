FROM ubuntu:latest

LABEL maintainer="Brian Schlining <brian@mbari.org"

RUN apt-get update \
  && apt-get dist-upgrade -y \
    build-essential \
    bzip2 \
    curl \
    git 

RUN curl -qsSLkO \
      https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-`uname -p`.sh \
    && bash Miniconda3-latest-Linux-`uname -p`.sh -b \
    && rm Miniconda3-latest-Linux-`uname -p`.sh

ENV APP_HOME=/opt/yoda_im
ENV PORT 4567
ENV PATH=/root/miniconda3/bin:$PATH:${APP_HOME}

RUN conda update -n base conda \
    && conda env create -f environment.yml

COPY . ${APP_HOME}
WORKDIR ${APP_HOME}

RUN chmod a+x ${APP_HOME}/app.sh

CMD ["app.sh"]


