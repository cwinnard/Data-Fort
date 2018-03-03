#!/bin/bash
project_name="Data-Fort"
# get path
path=$(pwd)
# substring without path(not working)
scripts="/scripts"
# go one level up from the scripts directory(current dir)
project_path=${path//$scripts/}
# path to install virtualenv
virtualenv_path="$project_path/env"
# load depdenecies into variable
deps=$(cat dependencies.txt)
# install virtualenv
pip install virtualenv
# create new virtualenv
virtualenv $virtualenv_path
# activate new virtualenv
. $virtualenv_path/Scripts/activate
# install dependencies in new virtualenv
pip install $deps
echo "source $virtualenv_path/Scripts/activate" > scripts/activate.sh
clear
echo "New virtualenv was installed at: $virtualenv_path"
echo "Use \"source $virtualenv_path/Scripts/activate\" or"
echo "\"$path/activate.sh\" to activate new virtualenv."