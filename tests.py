import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):
    def test_invalid_0_digit(self):
        self.assertFalse(credit_card_validator(''))

    def test_invalid_1_digit(self):
        # Test invalid card with visa prefix
        self.assertFalse(credit_card_validator('4'))

    def test_invalid_2_digit(self):
        # Test invalid card with amex prefix
        self.assertFalse(credit_card_validator('34'))

    def test_invalid_2_digit_2(self):
        # Test invalid card with amex prefix
        self.assertFalse(credit_card_validator('37'))

    def test_invalid_9_digit(self):
        # Test AMEX prefix with valid check sum but invalid length
        self.assertFalse(credit_card_validator('376151049'))

    def test_valid_10_digit(self):
        self.assertTrue(credit_card_validator('3761510449'))

    def test_invalid_10_digit(self):
        self.assertFalse(credit_card_validator('3761510448'))

    def test_valid_11_digit(self):
        self.assertTrue(credit_card_validator('31455071568'))

    def test_invalid_11_digit(self):
        self.assertFalse(credit_card_validator('31455071566'))

    def test_valid_12_digit(self):
        self.assertTrue(credit_card_validator('434256427866'))

    def test_invalid_12_digit(self):
        self.assertFalse(credit_card_validator('434256427865'))

    def test_valid_13_digit(self):
        self.assertTrue(credit_card_validator('1690512642015'))

    def test_invalid_13_digit(self):
        self.assertFalse(credit_card_validator('1690512642012'))

    def test_valid_14_digit(self):
        self.assertTrue(credit_card_validator('71566889496372'))

    def test_invalid_14_digit(self):
        self.assertFalse(credit_card_validator('71566889496371'))

    def test_valid_15_digit(self):
        self.assertTrue(credit_card_validator('683074087568241'))

    def test_invalid_15_digit(self):
        self.assertFalse(credit_card_validator('683074087568240'))

    def test_valid_16_digit(self):
        # not master of visa, just pure length
        self.assertTrue(credit_card_validator('9723233384426544'))

    def test_invalid_16_digit(self):
        # not master of visa, just pure length
        self.assertFalse(credit_card_validator('9723233384426542'))

    def test_valid_17_digit(self):
        self.assertTrue(credit_card_validator('99055597294275368'))

    def test_invalid_17_digit(self):
        self.assertFalse(credit_card_validator('99055597294275364'))

    def test_valid_18_digit(self):
        self.assertTrue(credit_card_validator('730946709430106547'))

    def test_invalid_18_digit(self):
        self.assertFalse(credit_card_validator('730946709430106542'))

    def test_valid_19_digit(self):
        self.assertTrue(credit_card_validator('7718953209133728422'))

    def test_invalid_19_digit(self):
        self.assertFalse(credit_card_validator('7718953209133728421'))

    def test_invalid_exceed_length(self):
        self.assertFalse(credit_card_validator('49003001172256730444'))

    def test_valid_amex_test_card(self):
        self.assertTrue(credit_card_validator('374245455400126'))

    def test_valid_amex_test_card_2(self):
        self.assertTrue(credit_card_validator('370000000100018'))

    def test_invalid_amex_prefix_1(self):
        self.assertFalse(credit_card_validator('370000000100013'))

    def test_valid_amex_prefix_2(self):
        self.assertTrue(credit_card_validator('340000000100007'))

    def test_invalid_amex_prefix_2(self):
        self.assertFalse(credit_card_validator('340000000100013'))

    def test_invalid_amex_length(self):
        self.assertFalse(credit_card_validator('3400000001000071'))

    def test_invalid_amex_length_2(self):
        self.assertFalse(credit_card_validator('3700000000000020'))

    def test_valid_visa_test_card_1(self):
        self.assertTrue(credit_card_validator('4111111145551142'))

    def test_valid_visa_test_card_2(self):
        self.assertTrue(credit_card_validator('4988438843884305'))

    def test_invalid_visa_card(self):
        self.assertFalse(credit_card_validator('4111112014267666'))

    def test_invalid_visa_length(self):
        self.assertFalse(credit_card_validator('498843884388430'))

    def test_invalid_visa_length_2(self):
        self.assertFalse(credit_card_validator('49884388438843051'))

    def test_invalid_visa_length_3(self):
        # incorrect last digit
        self.assertFalse(credit_card_validator('49884388438843052'))

    def test_invalid_mastercard_prefix_1(self):
        # boundary check, invalid prefix and checksum with valid length
        self.assertFalse(credit_card_validator('5000800050018002'))

    def test_invalid_mastercard_prefix_2(self):
        # boundary check, invalid prefix with valid checksum and length
        self.assertFalse(credit_card_validator('5000800050018003'))

    def test_invalid_mastercard_prefix_3(self):
        # boundary check, invalid prefix with valid checksum and length
        self.assertFalse(credit_card_validator('5600800050018007'))

    def test_invalid_mastercard_prefix_4(self):
        # boundary check, invalid prefix and checksum with valid length
        self.assertFalse(credit_card_validator('5600800050018007'))

    def test_invalid_mastercard_prefix_5(self):
        # boundary check, invalid prefix but valid length and checksum
        self.assertFalse(credit_card_validator('2820007000260017'))

    def test_invalid_mastercard_prefix_8(self):
        # valid length but invalid prefix and checksum
        self.assertFalse(credit_card_validator('2220080005001800'))

    def test_invalid_mastercard_prefix_9(self):
        # valid length and checksum but invalid prefix
        self.assertFalse(credit_card_validator('2220080005001807'))

    def test_invalid_mastercard_length(self):
        # valid prefix and checksum but invalid length
        self.assertFalse(credit_card_validator('56008000500180074'))

    def test_valid_mastercard_1(self):
        self.assertTrue(credit_card_validator('513456789012345'))

    def test_valid_mastercard_2(self):
        self.assertTrue(credit_card_validator('523456789012343'))

    def test_valid_mastercard_3(self):
        self.assertTrue(credit_card_validator('5300800050018000'))

    def test_valid_mastercard_4(self):
        self.assertTrue(credit_card_validator('5400800050018009'))

    def test_valid_mastercard_5(self):
        self.assertTrue(credit_card_validator('553456789012346'))

    def test_valid_mastercard_6(self):
        self.assertTrue(credit_card_validator('2221000900180042'))

    def test_valid_mastercard_7(self):
        self.assertTrue(credit_card_validator('2720007000260018'))


if __name__ == '__main__':
    unittest.main()
