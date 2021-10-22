import argparse
import os
import sys

parser = argparse.ArgumentParser(
    description='Create a ssh key pairs for dev and zip it with encryption.')

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
    args.first_name = str(input(f'Enter developer firstname (john): ') or 'john')

    args.last_name = str(input(f'Enter developer lastname (Doe): ') or 'Doe')

    args.email = str(input(f'Enter developer email (test@test.test): ') or 'test@test.test')

    args.password = str(
        input(f'Enter password for zipped folder (12345): ') or '12345')

    print('\n')

last_name = args.last_name.replace(' ', '').lower()
first_name = args.first_name.replace(' ', '').lower()
email = args.email.replace(' ', '').lower()
password = args.password.replace('$', '\\$')

cwd = os.getcwd()
ssh_keys_dir_name = 'ssh-key-dev'

user_keys_path = '/'.join([os.getcwd(), ssh_keys_dir_name, args.first_name])
user_keys = '.'.join([first_name, last_name])

# TODO propose to the user to change the path
if not os.path.exists(user_keys_path):
    os.makedirs(user_keys_path)

os.system(f'ssh-keygen -t ed25519 -P "" -C "{email}" -f {user_keys_path}/{user_keys}')

os.chdir(ssh_keys_dir_name)

print(f'The {first_name} folder will be zipped with following passord: {password}')

os.system(f'zip -P "{password}" -r {first_name}.zip {first_name}')
