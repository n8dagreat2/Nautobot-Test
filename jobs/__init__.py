from nautobot.apps.jobs import register_jobs
from .change_port import ChangePorts

jobs = [ChangePorts]
register_jobs(*jobs)
