#!/bin/bash
git clone https://github.com/minoplhy/filters-maker ./filters-maker
git clone https://x-access-token:$API_TOKEN_GITHUB@github.com/$Destination_REPO.git ./$Destination_NAME
>>>>>>> d43f04f (Create filters.sh)
filters-maker/crawler.py filters-maker/input/domains.txt
filters-maker/maker-rpz.py filtes-maker/input/domains.txt $Destination_REPO/$Destination_VERSION/rpz.txt
cd $Destination_REPO
git remote add destination https://x-access-token:$API_TOKEN_GITHUB@github.com/$Destination_REPO.git
git config --local user.name $GIT_NAME
git config --local user.email $GIT_EMAIL
git add .
git commit -m "Schedule Building : `date`"
git push -u destination $REPO_BRANCH
