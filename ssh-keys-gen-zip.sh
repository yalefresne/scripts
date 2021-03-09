#!/bin/bash

# ssh-keys-gen-zip - A script to create a ssh key pairs for dev and zip it with encryption.

interactive=null
firstname=john
lastname=doe
email=null
password=123456

usage()
{
    echo "This script allow you to create a ssh key pairs for dev and zip it with encryption."
    echo "ssh-dev-keys -h Print this help"
    echo "ssh-dev-keys -i To execute this command in interactive mode step by step"
    echo "ssh-dev-keys -f yourfirstname -l yourlastname -e your@email -pw yourpassword" 
    exit 0
}

if [ $# = 0 ]; then
    usage
fi

while [ "$1" != "" ]; do
    case $1 in
        -f | --firstname )      shift
                                firstname="$(echo -e "$1" | tr -d '[:space:]' | tr '[:upper:]' '[:lower:]')"
                                ;;
        -l | --lastname )       shift
                                lastname="$(echo -e "$1" | tr -d '[:space:]' | tr '[:upper:]' '[:lower:]')"

                                ;;
        -e | --email )          shift
                                email=$1
                                ;;
        -pw | --password )      shift
                                password=$1
                                ;;
        -i | --interactive )    interactive=1
                                ;;
        -h | --help )           usage
                                exit
                                ;;
        * )                     usage
                                exit 1
    esac
    shift
done

if [ "$interactive" = "1" ]; then

    response=

    read -p "Enter developer firstname [$firstname] > " response
    if [ -n "$response" ]; then
        firstname="$(echo -e "$response" | tr -d '[:space:]' | tr '[:upper:]' '[:lower:]')"
    fi

    read -p "Enter developer lastname [$lastname] > " response
    if [ -n "$response" ]; then
        lastname="$(echo -e "$response" | tr -d '[:space:]' | tr '[:upper:]' '[:lower:]')"
    fi

    read -p "Enter developer email [$email] > " response
    if [ -n "$response" ]; then
        email="$response"
    fi

    read -p "Enter password for zipped folder > " response
    if [ -n "$response" ]; then
        password="$response"
    fi

fi

if [ -d ~/ssh-dev-keys ]; then
    cd ~/ssh-dev-keys && mkdir $firstname
else
    mkdir ~/ssh-dev-keys && mkdir ~/ssh-dev-keys/$firstname
fi

ssh-keygen -t ed25519 -P "" -C "$email" -f ~/ssh-dev-keys/$firstname/$firstname.$lastname

cd ~/ssh-dev-keys

zip -P "$password" -r $firstname.zip $firstname

