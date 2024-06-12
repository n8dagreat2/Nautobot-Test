from nautobot.apps.jobs import (
    Job,
    StringVar,
    ObjectVar,
    IntegerVar,
    MultiObjectVar,
    TextVar,
)
from nautobot.dcim.models import Location, Device, DeviceType, Manufacturer, Interface
from nautobot.ipam.models import VLAN
from nautobot.extras.models import CustomField, Role, Status
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType


class AddVlan(Job):

    class Meta:
        name = "Add a VLAN to a Site"

    location = ObjectVar(
        model=Location,
        display_field="name",
        required=True,
        description="Select a location",
    )
    vlan_id = IntegerVar(description="Enter the VLAN ID", required=True)
    vlan_name = StringVar(description="Enter the VLAN Name", required=True)
    vlan_description = StringVar(
        description="***Optional: Enter an SVI description.", required=False
    )

    def run(self, **data):
        location = data["location"]
        vlan_id = data["vlan_id"]
        vlan_name = data["vlan_name"]

        return "Job completed successfully"
