import subprocess
import sys
import os

PLAYBOOKS_DIR = '/usr/share/ansible_playbooks'

playbooks = {
    "samba": os.path.join(PLAYBOOKS_DIR, "samba.yml"),
    "nfs": os.path.join(PLAYBOOKS_DIR, "nfs.yml"),
    "chrony": os.path.join(PLAYBOOKS_DIR, "chrony.yml"),
    "docker": os.path.join(PLAYBOOKS_DIR, "docker.yml"),
    "iptables": os.path.join(PLAYBOOKS_DIR, "iptables.yml"),
    "moodle": os.path.join(PLAYBOOKS_DIR, "moodle.yml"),
    "nginx": os.path.join(PLAYBOOKS_DIR, "nginx.yml"),
    "yandex": os.path.join(PLAYBOOKS_DIR, "yandex.yml"),
}

def run_playbook(playbook):
    if playbook in playbooks:
        print(f"Running playbook: {playbooks[playbook]}...")
        result = subprocess.run(['ansible-playbook', '-i', 'hosts.ini', playbooks[playbook]], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(f"Error executing playbook: {result.stderr}")
            sys.exit(result.returncode)
    else:
        print(f"Unknown playbook: {playbook}")
        print("Available playbooks:", ', '.join(playbooks.keys()))

def main():
    if len(sys.argv) != 2:
        print("Usage: demo <playbook_name>")
        sys.exit(1)
    run_playbook(sys.argv[1])
