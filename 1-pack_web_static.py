#!/usr/bin/python3
""" This script generates tgz archive """

def do_pack():
    """This function to generate tgz archive"""
    try:
        if not os.path.exists("versions"):
            os.mkdir("versions")

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = f"web_static_{timestamp}.tgz"
        archive_path = f"versions/{archive_name}"

        local(f"tar -cvzf {archive_path} web_static")

        return archive_path
    except Exception as e:
        return None
