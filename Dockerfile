# Container image that runs your code
FROM python

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY filters.sh /filters.sh
RUN pip install -r /filters-maker/requirements.txt
RUN apt-get update && apt-get install -y git wget curl
RUN wget -O gh https://github.com/cli/cli/releases/download/v2.30.0/gh_2.30.0_linux_amd64.deb
RUN dpkg -i gh
# Code file to execute when the docker container starts up (`entrypoint.sh`)
RUN chmod 777 /filters.sh
ENTRYPOINT ["/bin/bash","/filters.sh"]
