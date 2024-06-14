#!/usr/bin/python3

""" Warning not complete """

import requests
import re
import os
import subprocess

def runme(cmd, env, cwd='.'):
    """Simple function to run a command and return 0 for success, 1 for
       failure.  cmd is a list of the command and arguments, action is a
       name for the action (for logging), pkg is the name of the package
       being operated on, env is the environment dict, and cwd is where
       the script should be executed from."""
    try:
        subprocess.check_call(cmd, env=env, cwd=cwd, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        sys.stderr.write('%s failed: %s\n' % (cmd, e))
        return 1
    return 0

spec_file = "discord.spec"

h = requests.head("https://discord.com/api/download/stable?platform=linux&format=tar.gz")
print(h.headers.get("location"))
minor64 = h.headers.get("location")
version64 = minor64.split("/")[5]

spec = open(spec_file).read()
str_mx3 = re.compile(r'(Version:\s*) .*')
spec3 = re.sub(str_mx3, r'\1 %s' % version64, spec)

if spec != spec3:
#    open(spec_file, 'w').write(spec3)
    enviro = os.environ
    pkgcmd = ['rpmdev-bumpspec', '-n', version64, '-c', 'Update to %s' % (version64),
        spec_file]
    if runme(pkgcmd, enviro):
        print('error running runme')

    print("New version available!")
    print('rfpkg mockbuild -N --default-mock-resultdir --root fedora-39-x86_64-rpmfusion_nonfree')
else:
    print("Already updated !")

print('spectool -g discord.spec')
print("rfpkg new-sources $(spectool -l --sources discord.spec | grep https | sed 's/.*: //;s#.*/##')")
print('rfpkg ci -c && git show && echo Press enter to push and build; read dummy; rfpkg push && rfpkg build --nowait')
print('git checkout f40 && git merge master && git push && rfpkg build --nowait; git checkout master')
print('git checkout f39 && git merge master && git push && rfpkg build --nowait; git checkout master')
