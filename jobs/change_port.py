from nautobot.apps.jobs import Job, StringVar, ObjectVar, MultiObjectVar, TextVar
from nautobot.dcim.models import Location, Device, DeviceType, Manufacturer, Interface
from nautobot.extras.models import CustomField, Role, Status
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType


class ChangePorts(Job):

    class Meta:
        name = "Choose Interface and Device"
        description = """
            This job does a number of interesting things.
            
            1. It takes your kids to work
            2. It sets your coordinates for a jump to hyperspace
            3. It codes for you
        """

    location = ObjectVar(
        model=Location,
        display_field="name",
        required=True,
        description="Select a location",
    )
    device_name = StringVar(description="Enter the device name", required=True)

    def run(self, **data):
        location = data["location"]
        device_name = data["device_name"]

        return "Job completed successfully"
