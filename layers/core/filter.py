from layers.core.exceptions import typeCheckerArray, categoryChecker, \
    UNSETVALUE


class Filter:
    def __init__(self, domain="mitre-enterprise"):
        """
            Initialization - Creates a filter object, with an optional
                domain input

            :param domain: The domain used for this layer (mitre-enterprise
                or mitre-mobile)
        """
        self.__stages = UNSETVALUE
        self.domain = domain
        self.__platforms = UNSETVALUE

    @property
    def stages(self):
        if self.__stages != UNSETVALUE:
            return self.__stages

    @stages.setter
    def stages(self, stage):
        typeCheckerArray(type(self).__name__, stage, str, "stage")
        categoryChecker(type(self).__name__, stage[0], ["act", "prepare"],
                        "stages")
        self.__stages = stage

    @property
    def platforms(self):
        if self.__platforms != UNSETVALUE:
            return self.__platforms

    @platforms.setter
    def platforms(self, platforms):
        typeCheckerArray(type(self).__name__, platforms, str, "platforms")
        self.__platforms = []
        valids = ["Windows", "Linux", "macOS", "AWS", "GCP", "Azure",
                  "Azure AD", "Office 365", "SaaS"]
        if self.domain == "mitre-mobile":
            valids = ['Android', 'iOS']
        for entry in platforms:
            categoryChecker(type(self).__name__, entry, valids, "platforms")
            self.__platforms.append(entry)

    def get_dict(self):
        """
            Converts the currently loaded data into a dict
            :returns: A dict representation of the local filter object
        """
        temp = dict()
        listing = vars(self)
        for entry in listing:
            if entry == 'domain':
                continue
            if listing[entry] != UNSETVALUE:
                temp[entry.split(type(self).__name__ + '__')[-1]] \
                    = listing[entry]
        if len(temp) > 0:
            return temp