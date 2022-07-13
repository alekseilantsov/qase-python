"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import qaseio
from qaseio.api.defects_api import DefectsApi  # noqa: E501


class TestDefectsApi(unittest.TestCase):
    """DefectsApi unit test stubs"""

    def setUp(self):
        self.api = DefectsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_defect(self):
        """Test case for create_defect

        Create a new defect.  # noqa: E501
        """
        pass

    def test_delete_defect(self):
        """Test case for delete_defect

        Delete defect.  # noqa: E501
        """
        pass

    def test_get_defect(self):
        """Test case for get_defect

        Get a specific defect.  # noqa: E501
        """
        pass

    def test_get_defects(self):
        """Test case for get_defects

        Get all defects.  # noqa: E501
        """
        pass

    def test_resolve_defect(self):
        """Test case for resolve_defect

        Resolve a specific defect.  # noqa: E501
        """
        pass

    def test_update_defect(self):
        """Test case for update_defect

        Update defect.  # noqa: E501
        """
        pass

    def test_update_defect_status(self):
        """Test case for update_defect_status

        Update a specific defect status.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
