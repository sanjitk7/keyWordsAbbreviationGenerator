import unittest
from generate_acronymn import main,checkUnderscore,isMultiWordCamel

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
 
    # def setUp(self):
    #     pass

    # def test_main(self):
    #     self.assertEqual(main("DUPLICATE_INVOICE_IDS_ALLOWED"),"")
    #     self.assertEqual(main("Date"),"")
    #     self.assertEqual(main("DataCollections"),"dc")
    #     # self.assertEqual(main("date_column"),"dc")
    #     self.assertEqual(main("FinalizeResponseStatusInfo"),"frsi")
    #     # self.assertEqual(main("account_updater_request_indicator"),"auri")
    #     self.assertEqual(main("accounts_acc"),"")
    #     # self.assertEqual(main("travel_agency_name"),"tan")
    #     self.assertEqual(main("WebContext"),"wc")
    #     self.assertEqual(main("_250_x_400"),"")
    #     self.assertEqual(main("sampleSmallCamelCase"),"sscc")
    def test_checkUnderscore(self):
        self.assertTrue(checkUnderscore("john_doe"))
        self.assertTrue(checkUnderscore("john_doe"))
        self.assertTrue(checkUnderscore("batman_arkham_night"))  
        self.assertTrue(checkUnderscore("hello_world"))
        self.assertFalse(checkUnderscore("ashokKumar"))
    def test_isMultiWordCamel(self):
        self.assertTrue(isMultiWordCamel("isMultiWordCamel"))
        self.assertTrue(isMultiWordCamel("janeDoe"))
        self.assertTrue(isMultiWordCamel("supermanManOfSteel"))
        self.assertTrue(isMultiWordCamel("theDarkNightRises"))
        self.assertFalse(isMultiWordCamel("adams_lopez"))


if __name__ == '__main__':
    unittest.main()