import subprocess
import sys

playbooks = {
    "samba": "playbooks/samba.yml",
    "nfs": "playbooks/nfs.yml",
    "chrony": "playbooks/chrony.yml",
    "docker": "playbooks/docker.yml",
    "iptables": "playbooks/iptables.yml",
    "moodle": "playbooks/moodle.yml",
    "nginx": "playbooks/nginx.yml",
    "yandex": "playbooks/yandex.yml",
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
