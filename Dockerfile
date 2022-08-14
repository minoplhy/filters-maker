# Container image that runs your code
FROM debian

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY filters.sh /filters.sh
RUN apt-get update && apt-get install -y python3 git python3-pip wget curl
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg 
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
RUN apt-get update && apt-get install -y gh
# Code file to execute when the docker container starts up (`entrypoint.sh`)
RUN chmod 777 /filters.sh
ENTRYPOINT ["/bin/bash","/filters.sh"]
