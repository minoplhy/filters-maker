#!/bin/bash
git clone https://github.com/minoplhy/filters-maker /filters-maker
git clone https://x-access-token:$API_TOKEN_GITHUB@github.com/$Destination_REPO.git /$Destination_NAME
pip3 install -r /filters-maker/requirements.txt
python3 /filters-maker/crawler.py /filters-maker/input/domains.txt
python3 /filters-maker/maker-rpz.py /filtes-maker/input/domains.txt /$Destination_NAME/$Destination_VERSION/rpz.txt
cd /$Destination_NAME
git remote add destination https://x-access-token:$API_TOKEN_GITHUB@github.com/$Destination_REPO.git
git config --local user.name $GIT_NAME
git config --local user.email $GIT_EMAIL
git add .
git commit -m "Schedule Building : `date`"
git push -u destination $REPO_BRANCH
