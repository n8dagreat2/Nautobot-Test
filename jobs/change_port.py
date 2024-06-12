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
    vlan_name = TextVar(description="Enter the VLAN Name", required=True)
    device_name = StringVar(description="Enter the device name", required=True)

    def run(self, **data):
        location = data["location"]

        return "Job completed successfully"
