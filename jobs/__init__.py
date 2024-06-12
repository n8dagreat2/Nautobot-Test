from nautobot.apps.jobs import register_jobs
from .change_port import AddVlan

jobs = [AddVlan]
register_jobs(*jobs)
