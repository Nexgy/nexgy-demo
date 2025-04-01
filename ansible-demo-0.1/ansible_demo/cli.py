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
        playbook_path = playbooks[playbook]
        print(f"Trying to run playbook at path: {playbook_path}")

        if not os.path.exists(playbook_path):
            print(f"Playbook file does NOT exist at: {playbook_path}")
            sys.exit(1)

        inventory_file = '/root/hosts'
        print(f"Using inventory file: {inventory_file}")

        result = subprocess.run(['ansible-playbook', '-i', inventory_file, playbook_path],
                                capture_output=True, text=True)

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

if __name__ == "__main__":
    main()
