import docker
import tempfile
import os


def execute_task(task):
    client = docker.from_env()

    with tempfile.TemporaryDirectory() as tmpdir:
        code_file = os.path.join(tmpdir, 'script.py')

        with open(code_file, 'w') as f:
            f.write(task.code)

        cpu_limit = int(task.resources.cpu) * 1000000000  # In nano CPUs
        mem_limit = task.resources.ram

        container = client.containers.run(
            "python:3.9-slim",
            f"python /app/script.py",
            detach=True,
            volumes={tmpdir: {'bind': '/app', 'mode': 'rw'}},
            cpu_period=100000,
            cpu_quota=cpu_limit,
            mem_limit=mem_limit
        )

        container.wait()

        logs = container.logs().decode("utf-8")
        container.remove()

        return logs
