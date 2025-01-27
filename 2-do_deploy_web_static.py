#!/usr/bin/python3
""" This script uploads tgz archive to remote server """
from fabric.api import local, put, run, env
import os

env.hosts = ['54.160.81.72', '54.84.79.240']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """This function uploads archived file """
    if not os.path.exists(archive_path):
        return False

    try:
        file_name = os.path.basename(archive_path)
        no_ext = file_name.split(".")[0]

        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p /data/web_static/releases/{}".format(no_ext))
        run("tar -xvf /tmp/{} -C /data/web_static/releases/{}".format(file_name, no_ext))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}".format(no_ext, no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static".format(no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current".format(no_ext))

        return True
    except Exception as e:
        return False

