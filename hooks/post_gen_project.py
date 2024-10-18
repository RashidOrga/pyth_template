import subprocess

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'Initial commit_'])
subprocess.call(['git', 'remote', 'add', 'origin', "{{cookiecutter.github_repo_link}}"])
