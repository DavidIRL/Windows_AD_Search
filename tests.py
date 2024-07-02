import active_directory 
from active_directory import Group


parent = Group("parent")
child = Group("child")
sub_child = Group("sub_child")

sub_child.add_user("sb_brenda")
child.add_user("c_donny")

child.add_group(sub_child)
parent.add_group(child)
print("ad groups created...")


try:
    def user_from_parent():
        return parent.get_users() ==  None
    
    
    def add_more_users():
        sub_child.add_user("sub_hella")
        child.add_user("c_priscilla")
        output = active_directory.get_user_in_group("c_priscilla", child)
        print(f"The user, 'c_priscilla', is a user of child group: {output}\n")
        

except Exception as err:
    print(f"user_from_parents or add_more_users issue: {err}")

try:
    def get_parent_users():
        output = parent.get_users()
        if "Leonidus" not in output:
            print(f"Leonidus is part of the parent group: {active_directory.get_user_in_group('Leonidus', parent)} ")
            print("Adding Leonidus to parent group of AD...\n")
            parent.add_user("Leonidus")
        
        print(f"Leonidus is part of the parent group: {active_directory.get_user_in_group('Leonidus', parent)}")
        return


    def get_child_name():
        print("Groups of current AD are:")
        print(f"""{parent.get_name()}
{child.get_name()}
{sub_child.get_name()}
            """)
except Exception as err:
    print(f"get_parent or get_child issue: {err}")

try:
    def add_bad_user1():
        print(parent.add_user(None))

    def add_bad_user2():
        print(sub_child.add_user(""))

except Exception as err:
    print(f"add_ bad_users issue: {err}")


def main():
    user_from_parent()
    add_more_users()
    get_parent_users()
    get_child_name()
    add_bad_user1()
    add_bad_user2()
    print(active_directory.get_user_in_group("", None))


if __name__ == '__main__':
    main()

