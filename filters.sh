#!/bin/bash
git clone https://github.com/minoplhy/filters-maker /filters-maker
git clone https://x-access-token:$API_TOKEN_GITHUB@github.com/$INPUT_DESTINATION_UNAME/$INPUT_DESTINATION_REPO.git /repros
git clone https://x-access-token:$API_TOKEN_GITHUB@github.com/$INPUT_DESTINATION_UNAME/$INPUT_DESTINATION_REPO.wiki.git /reprwiki
mkdir /reprwiki/$INPUT_DESTINATION_FOLDER/
mkdir /reprwiki/$INPUT_DESTINATION_FOLDER/$INPUT_DESTINATION_VERSION
pip3 install -r /filters-maker/requirements.txt
cd /reprwiki
python3 /repros/$INPUT_ACTION_FILE
TIMEDATE=`date`
git config --local user.name $INPUT_GIT_NAME
git config --local user.email $INPUT_GIT_EMAIL
git add .
git commit -m "Schedule Building : $TIMEDATE"
git push -u origin $INPUT_REPO_BRANCH
cd /repros
git config --local user.name $INPUT_GIT_NAME
git config --local user.email $INPUT_GIT_EMAIL
git add .
git commit -m "Schedule Building : $TIMEDATE"
git push -u origin $INPUT_BRANCH_VERSION
if [ -f "/repros/$INPUT_SUB_ACTION_LOCATION" ]; then
    echo $API_TOKEN_GITHUB > token.txt
    gh auth login --with-token < token.txt
    rm token.txt
    python3 /repros/$INPUT_SUB_ACTION_LOCATION
    echo "Code Completed!"
    gh release delete latest -y
    git tag | xargs -L 1 | xargs git push origin --delete
    gh release create latest -F /repros/Resources/Releases.md /gh-releases/* -t FILTERS IN RELEASES
fi
