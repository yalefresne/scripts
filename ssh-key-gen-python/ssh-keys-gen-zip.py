import argparse
import os
import sys

parser = argparse.ArgumentParser(description='Create a ssh key pairs for dev and zip it with encryption.')

parser.add_argument(
        '-i', '--interactive',
        dest='interactive',
        action='store_true',
        help='To execute this command in interactive mode step by step'
    )

required_arg = '--interactive' not in sys.argv and '-i' not in sys.argv

parser.add_argument(
        '-f', '--firstname',
        dest='first_name',
        help='A string',
        required=required_arg
    )
parser.add_argument(
        '-l', '--lastname',
        dest='last_name',
        help='A string',
        required=required_arg
    )
parser.add_argument(
        '-e', '--email',
        dest='email',
        help='A string',
        required=required_arg
    )
parser.add_argument(
        '-p', '--password',
        dest='password',
        help='A good password',
        required=required_arg
    )

args = parser.parse_args()

if(args.interactive):
    args.first_name = str(input('Enter developer firstname : ') or 'john')

    args.last_name = str(input('Enter developer lastname : ') or 'Doe')

    args.email = str(input('Enter developer email : ') or 'test@test.test')

    args.password = str(input('Enter password for zipped folder : ') or '12345')

last_name = args.last_name.replace(' ', '').lower()
first_name = args.first_name.replace(' ', '').lower()
email = args.email.replace(' ', '').lower()
password = args.password.replace(' ', '')

cwd = os.getcwd()
ssh_keys_dir_name = 'ssh-key-dev'

user_keys_path = os.getcwd() + '/' + ssh_keys_dir_name + '/' + args.first_name
user_keys = user_keys_path + '/' + first_name + '.' + last_name

# TODO propose to the user to change the path
if not os.path.exists(user_keys_path):
    os.makedirs(user_keys_path)

os.system('ssh-keygen -t ed25519 -P "" -C "'+email+'" -f ' + user_keys)

# cd ~/ssh-dev-keys

# # TODO Check if password contain $
# zip -P "$password" -r $firstname.zip $firstname

# echo "Don't forget to try to open the zipped folder to test password"

# open ~/ssh-dev-keys/$firstname.zip
