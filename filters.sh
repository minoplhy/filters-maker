#!/bin/bash
git clone https://github.com/minoplhy/filters-maker /filters-maker
git clone https://x-access-token:$API_TOKEN_GITHUB@github.com/$INPUT_DESTINATION_UNAME/$INPUT_DESTINATION_REPO.git /repros
mkdir /repros/Private-Build/$INPUT_DESTINATION_VERSION
pip3 install -r /filters-maker/requirements.txt
python3 /filters-maker/crawler.py /filters-maker/input/domains.txt
python3 /filters-maker/maker-rpz.py /filters-maker/input/excluded.txt /filters-maker/input/domains.txt /repros/Private-Build/$INPUT_DESTINATION_VERSION/rpz.txt
cd /repros
git config --local user.name $INPUT_GIT_NAME
git config --local user.email $INPUT_GIT_EMAIL
git add .
git commit -m "Schedule Building : `date`"
git push -u origin $INPUT_REPO_BRANCH
