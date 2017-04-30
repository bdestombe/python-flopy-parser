FROM python:3.6.1-alpine

ADD https://github.com/alexellis/faas/releases/download/0.5.1-alpha/fwatchdog /usr/bin
RUN chmod +x /usr/bin/fwatchdog

WORKDIR /root/

RUN apk add --update curl gcc g++ \
    && rm -rf /var/cache/apk/*

RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN pip install numpy 

RUN pip install https://github.com/bdestombe/flopymetascript/zipball/master

ENV fprocess="flopymetascript --inbase64file - --outbase64file -"

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
