import unittest
from generate_acronymn import main

# DUPLICATE_INVOICE_IDS_ALLOWED -> ignore
# DYNAMIC -> ignore
# dc: DataCollections,DoCancel,date_column
# Date -> ignore
# frsi: FinalizeResponseStatusInfo
# PPMX -> ignore
# auri: account_updater_request_indicator
# au: account_updater, AccountUpdater
# accounts -> ignore
# tan:travel_agency_name, travel_agent_name

# can you write a python program to classify keywords as above?

# In a dict



class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass

    def test_main(self):
        self.assertEqual(main("DUPLICATE_INVOICE_IDS_ALLOWED"),"")
        self.assertEqual(main("Date"),"")
        self.assertEqual(main("DataCollections"),"dc")
        # self.assertEqual(main("date_column"),"dc")
        self.assertEqual(main("FinalizeResponseStatusInfo"),"frsi")
        # self.assertEqual(main("account_updater_request_indicator"),"auri")
        self.assertEqual(main("accounts"),"")
        # self.assertEqual(main("travel_agency_name"),"tan")
        self.assertEqual(main("WebContext"),"wc")
        self.assertEqual(main("_250_x_400"),"")
        self.assertEqual(main("sampleSmallCamelCase"),"sscc")

if __name__ == '__main__':
    unittest.main()