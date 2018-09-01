FROM yuhangwang/keras-flask-base:latest

# default password: keras
ENV PASSWD='sha1:98b767162d34:8da1bc3c75a0f29145769edc977375a373407824'

# for jupyter
EXPOSE 8888

WORKDIR /notebook/

CMD /bin/bash -c 'jupyter notebook --no-browser --allow-root \
    --ip=* --NotebookApp.password=\"$PASSWD\" "$@"'
