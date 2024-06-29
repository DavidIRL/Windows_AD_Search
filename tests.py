import unittest
import active_directory as ad
from active_directory import Group

class TestAD(unittest.TestCase):
    def setUp(self):
        #create initial ad structure
        self.parent = Group("parent")
        self.child = Group("child")
        self.sub_child = Group("sub_child")

        self.sub_child.add_user("sb_brenda")
        self.child.add_user("c_donny")

        self.child.add_group(self.sub_child)
        self.parent.add_group(self.child)


    def user_from_parent(self):
        self.assertEqual(self.parent.get_users(), None)
    
    
    def add_more_users(self):
        self.subchild.add_user("sub_hella")
        self.child.add_user("c_priscilla")
        self.assertEqual(self.ad.get_user_in_group("c_priscilla", child), True)
        
        self.parent.add_user("Leonidus")


    def get_parent_users(self):
        self.assertEqual(self.parent.get_users(), "Leonidus")


    def get_child_name(self):
        self.assertEqual(self.child.get_name("c_donny"), "c_donny")


    def add_bad_users(self):
        with self.assertRaise(TypeError):
            self.parent.add_user(None)
        with self.assertRaise(TypeError):
            self.sub_child.add_user("")


    def tearDown(self):
        self.parent.dispose()
        self.child.dispose()
        self.sub_child.dispose()


if __name__ == '__main__':
    unittest.main()

