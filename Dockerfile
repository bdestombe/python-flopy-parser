FROM python:3.6.1-alpine

ADD https://github.com/alexellis/faas/releases/download/0.5.1-alpha/fwatchdog /usr/bin
RUN chmod +x /usr/bin/fwatchdog

WORKDIR /root/

RUN apk add --update curl gcc g++ \
    && rm -rf /var/cache/apk/*

RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN pip install numpy

# First install and let the dependencies be cached in a layer
# Then upgrade the flopyparser package every build, also when version number hasnt changed,
# without upgrading the dependencies
RUN pip install https://github.com/bdestombe/python-flopy-parser/zipball/master
RUN pip install --upgrade --no-deps --force-reinstall https://github.com/bdestombe/python-flopy-parser/zipball/master

ENV fprocess="flopyparser --outbase64file - --inbase64file - --logfile -"

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
