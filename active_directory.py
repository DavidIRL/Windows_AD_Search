class Group:
    def __init__(self, name="default"):
        self._name = name
        self.groups = set()
        self.users = set()

    def add_group(self, group):
        if group is None:
            return TypeError("Cannot add None elements to AD groups")
        if len(str(group)) == 0:
            return TypeError("Group name cannot be empty")
        self.groups.add(group)

    def add_user(self, user):
        if user is None:
            return TypeError("Cannot add None element as user")
        if len(str(user)) == 0:
            return TypeError("User name cannot be empty")
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self._name


def get_user_in_group(user, group):
    if (user is None or group is None):
        return TypeError("None elements cannot exist in AD groups")
    if (len(user) == 0 or len(str(group)) == 0):
        return TypeError("Blank elements cannot be exist in AD groups")
    users = group.get_users() # current group.users set
    if user in users:
        return True

    groups = group.get_groups()
    for current_group in groups:
        return get_user_in_group(user, current_group)

    return False

if __name__ == '__main__':
    p_ou = Group("parent")
    c_ou = Group("child")
    sc_ou = Group("subchild")
    gc_ou = Group("grandchild")

    sc_ou.add_group(gc_ou)
    c_ou.add_group(sc_ou)
    p_ou.add_group(c_ou)

    sc_ou.add_user("sebastian")
    gc_ou.add_user("gustaf")
    p_ou.add_user("priscilla")
    c_ou.add_user("castiel")

    print(f"Is Sebastian a valid user of the child OU?\n")
    print(f"...")
    print(get_user_in_group("sebastian", c_ou))
