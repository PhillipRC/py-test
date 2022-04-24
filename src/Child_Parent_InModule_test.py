import pytest
import unittest
from unittest.mock import patch
from Child_Parent_InModule import Child

# Need to import here, allowing tests mock the anything in the module
import ParentModule

class Child_Parent_InModule_Tests(unittest.TestCase):

    # this test will test using the real ParentModule
    # should result in more coverage because the real Parent.__init__ will fire
    @pytest.mark.skip
    def test_Child_Parent(self):
        import Child_Parent_InModule
        testObject = Child_Parent_InModule.Child(message="test message")
        assert testObject.message == "test message"

    # this test uses a MagicMock to replace the Parent.__init__
    # should result in less coverage because the real Parent.__init__ will NOT fire
    @patch('Child_Parent_InModule_test.ParentModule.Parent.__init__')
    def test_Child_Only(self, mockParentInit):
        # init should return None
        mockParentInit.return_value = None
        testObject = Child(message="test message")
        mockParentInit.assert_called_with(message="test message")
