#!/bin/bash
git clone https://github.com/minoplhy/filters-maker /filters-maker
git clone https://x-access-token:$API_TOKEN_GITHUB@github.com/$INPUT_DESTINATION_UNAME/$INPUT_DESTINATION_REPO.git /repros
git clone https://x-access-token:$API_TOKEN_GITHUB@github.com/$INPUT_DESTINATION_UNAME/$INPUT_DESTINATION_REPO.wiki.git /reprwiki
mkdir /reprwiki/$INPUT_DESTINATION_FOLDER/
mkdir /reprwiki/$INPUT_DESTINATION_FOLDER/$INPUT_DESTINATION_VERSION
pip3 install -r /filters-maker/requirements.txt
cd /reprwiki
python3 /repros/$INPUT_ACTION_FILE
git config --local user.name $INPUT_GIT_NAME
git config --local user.email $INPUT_GIT_EMAIL
git add .
git commit -m "Schedule Building : `date`"
git reflog expire --all --expire=now
git gc --prune=now --aggressive
git push -u origin $INPUT_REPO_BRANCH
cd /repros
git config --local user.name $INPUT_GIT_NAME
git config --local user.email $INPUT_GIT_EMAIL
git add .
git commit -m "Schedule Building : `date`"
git reflog expire --all --expire=now
git gc --prune=now --aggressive
