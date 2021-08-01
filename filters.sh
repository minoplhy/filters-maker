#!/bin/bash
git clone https://github.com/minoplhy/filters-maker /filters-maker
git clone https://x-access-token:$API_TOKEN_GITHUB@github.com/$INPUT_DESTINATION_UNAME/$INPUT_DESTINATION_REPO.git /repros
mkdir /repros/$INPUT_DESTINATION_FOLDER/$INPUT_DESTINATION_VERSION
pip3 install -r /filters-maker/requirements.txt
python3 /filters-maker/crawler.py /repros/$INPUT_DESTINATION_FOLDER/$INPUT_DESTINATION_VERSION/domains.txt
python3 /filters-maker/maker-rpz.py /repros/Resources/excluded.txt /repros/$INPUT_DESTINATION_FOLDER/$INPUT_DESTINATION_VERSION/domains.txt /repros/$INPUT_DESTINATION_FOLDER/$INPUT_DESTINATION_VERSION/rpz.txt
cd /repros
git config --local user.name $INPUT_GIT_NAME
git config --local user.email $INPUT_GIT_EMAIL
git add .
git commit -m "Schedule Building : `date`"
git push -u origin $INPUT_REPO_BRANCH
