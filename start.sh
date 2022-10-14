#!/usr/bin/env bash
# linux  . venv/bin/activate para poder activarlo

if [ $VIRTUAL_ENVIRONMENT ]
then 
    deactivate
fi
. venv/Scripts/activate