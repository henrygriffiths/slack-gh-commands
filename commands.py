import subprocess


repos = [
    'org/examplerepo'
]

default_subscriptions = [ # Default Subscriptions
    'issues',
    'pulls',
    'releases',
    'deployments',
    'commits',
]

subscriptions = ['releases', 'deployments', 'commits', 'discussions', 'workflows'] # Types to subscribe to


def main():
    copy_to_clipboard('/invite @github')

    for repo in repos:
        copy_to_clipboard(f"/github subscribe {repo}")

        for notif_type in [notif_type for notif_type in default_subscriptions if notif_type not in subscriptions]:
            copy_to_clipboard(f"/github unsubscribe {repo} {notif_type}")

        for notif_type in [notif_type for notif_type in subscriptions if notif_type not in default_subscriptions]:
            copy_to_clipboard(f"/github subscribe {repo} {notif_type}")

    copy_to_clipboard('/github subscribe list features')


def copy_to_clipboard(command: str, wait_input: bool = True) -> None:
    p = subprocess.Popen(['xsel', '-bi'], stdin = subprocess.PIPE)
    p.communicate(input=bytes(str(command).encode('UTF-8')))
    if wait_input is True:
        print(command)



if __name__ == '__main__':
    main()
