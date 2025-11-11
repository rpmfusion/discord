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
latest_version = minor64.split("/")[5]

h = requests.head("https://discord.com/api/download/stable?platform=linux&format=tar.gz", allow_redirects=True)
last_modified = h.headers.get("Last-Modified")
if last_modified:
    print("Last Modified:", last_modified)

spec = open(spec_file).read()
match = re.search(r'^Version:\s*(\S+)', spec, re.MULTILINE)
current_version = match.group(1)

if current_version != latest_version:
    enviro = os.environ
    pkgcmd = ['rpmdev-bumpspec', '-n', latest_version, '-c', 'Update to %s' % (latest_version),
        spec_file]
    if runme(pkgcmd, enviro):
        print('error running runme')

    print(f"New version available: {current_version} -> {latest_version}")
    print('spectool -g discord.spec')
    print('rfpkg --release f41 mockbuild -N --default-mock-resultdir')
else:
    print(f"Already updated: {current_version}")
    print('spectool -g discord.spec')

print("rfpkg new-sources $(spectool -l --sources discord.spec | grep https | sed 's/.*: //;s#.*/##')")
print('rfpkg ci -c && git show && echo Press enter to push and build; read dummy; rfpkg push && rfpkg build --nowait')
print('git checkout f43 && git merge master && git push && rfpkg build --nowait; git checkout master')
print('git checkout f42 && git merge master && git push && rfpkg build --nowait; git checkout master')
print('git checkout f41 && git merge master && git push && rfpkg build --nowait; git checkout master')
print('git checkout el10 && git merge master && git push && rfpkg build --nowait; git checkout master')
print('git checkout el9 && git merge master && git push && rfpkg build --nowait; git checkout master')
