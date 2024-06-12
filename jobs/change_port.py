from nautobot.apps.jobs import Job, StringVar


class ChangePorts(Job):
    var1 = StringVar()

    class Meta:
        name = "Glorbus"
        description = """
            This job does a number of interesting things.
            
            1. It takes your kids to work
            2. It sets your coordinates for a jump to hyperspace
            3. It codes for you
        """

    def run(self, var1):
        if var1 != "Star Wars is the best!":
            self.logger.error("var1 must be 'Star Wars is the best!'")
            raise Exception("Argument input validation failed.")
