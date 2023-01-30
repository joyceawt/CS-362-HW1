import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):
    def test_invalid_0_digit(self):
        self.assertFalse(credit_card_validator(''))

    def test_invalid_1_digit(self):
        # Test invalid card with visa prefix
        self.assertFalse(credit_card_validator('4'))

    def test_invalid_1_digit_2(self):
        # Test invalid card with 0 prefix
        self.assertFalse(credit_card_validator('0'))

    def test_invalid_2_digit(self):
        # Test invalid card with amex prefix
        self.assertFalse(credit_card_validator('34'))

    def test_invalid_2_digit_2(self):
        # Test invalid card with amex prefix
        self.assertFalse(credit_card_validator('37'))

    def test_invalid_2_digit_3(self):
        # Test invalid card with mastercard prefix
        self.assertFalse(credit_card_validator('51'))

    def test_invalid_2_digit_4(self):
        # Test invalid card with mastercard prefix
        self.assertFalse(credit_card_validator('55'))

    def test_invalid_2_digit_5(self):
        # Test invalid card with invalid prefix (boundary of mastercard)
        self.assertFalse(credit_card_validator('50'))

    def test_invalid_2_digit_6(self):
        # Test invalid card with mastercard prefix
        self.assertFalse(credit_card_validator('52'))

    def test_invalid_2_digit_7(self):
        # Test invalid card with mastercard prefix
        self.assertFalse(credit_card_validator('53'))

    def test_invalid_2_digit_8(self):
        # Test invalid card with mastercard prefix
        self.assertFalse(credit_card_validator('54'))

    def test_invalid_4_digit(self):
        # Test invalid card with mastercard prefix
        self.assertFalse(credit_card_validator('2221'))

    def test_invalid_4_digit_2(self):
        # Test invalid card with mastercard prefix
        self.assertFalse(credit_card_validator('2720'))

    def test_invalid_4_digit_3(self):
        # Test invalid card with mastercard prefix
        self.assertFalse(credit_card_validator('2321'))

    def test_invalid_4_digit_4(self):
        # Test invalid card with mastercard prefix
        self.assertFalse(credit_card_validator('2421'))

    def test_invalid_4_digit_5(self):
        # Test invalid card with invalid prefix (boundary of mastercard)
        self.assertFalse(credit_card_validator('2719'))

    def test_invalid_4_digit_6(self):
        # Test invalid card with invalid prefix (boundary of mastercard)
        self.assertFalse(credit_card_validator('2721'))

    def test_invalid_9_digit(self):
        # Test valid check sum but invalid length
        self.assertFalse(credit_card_validator('326151040'))

    def test_invalid_10_digit(self):
        # Test valid check sum but invalid prefix and invalid length
        self.assertFalse(credit_card_validator('3661510440'))

    def test_invalid_10_digit_2(self):
        # Test AMEX prefix with invalid checksum and length
        self.assertFalse(credit_card_validator('3761510448'))

    def test_invalid_10_digit_3(self):
        # Test valid invalid check sum but valid length
        self.assertFalse(credit_card_validator('3161510445'))

    def test_invalid_11_digit(self):
        # valid length and checksum but invalid prefix
        self.assertFalse(credit_card_validator('31455071568'))

    def test_invalid_11_digit_2(self):
        # valid length but invalid prefix and checksum
        self.assertFalse(credit_card_validator('31455071566'))

    def test_invalid_12_digit(self):
        # valid length and checksum but invalid prefix
        self.assertFalse(credit_card_validator('334256427868'))

    def test_invalid_12_digit_2(self):
        # valid length but invalid prefix and checksum
        self.assertFalse(credit_card_validator('334256427865'))

    def test_invalid_13_digit(self):
        # valid length and checksum but invalid prefix
        self.assertFalse(credit_card_validator('1690512642015'))

    def test_invalid_13_digit_2(self):
        # valid length but invalid prefix and checksum
        self.assertFalse(credit_card_validator('1690512642012'))

    def test_invalid_14_digit(self):
        # valid length and checksum but invalid prefix
        self.assertFalse(credit_card_validator('71566889496372'))

    def test_invalid_14_digit_2(self):
        # valid length but invalid prefix and checksum
        self.assertFalse(credit_card_validator('71566889496371'))

    def test_invalid_15_digit(self):
        # valid length and checksum but invalid prefix
        self.assertFalse(credit_card_validator('683074087568241'))

    def test_invalid_15_digit_2(self):
        # valid length but invalid prefix and checksum
        self.assertFalse(credit_card_validator('683074087568240'))

    def test_valid_16_digit(self):
        # not master of visa, just pure length
        self.assertTrue(credit_card_validator('9723233384426544'))

    def test_invalid_16_digit(self):
        # not master of visa, just pure length
        self.assertFalse(credit_card_validator('9723233384426542'))

    def test_invalid_17_digit(self):
        # invalid prefix with valid checksum and length
        self.assertFalse(credit_card_validator('99055597294275368'))

    def test_invalid_17_digit_2(self):
        # invalid prefix with valid length and invalid checksum
        self.assertFalse(credit_card_validator('99055597294275364'))

    def test_invalid_18_digit(self):
        # invalid prefix with valid checksum and length
        self.assertFalse(credit_card_validator('730946709430106547'))

    def test_invalid_18_digit_2(self):
        # invalid prefix and invalid checksum with valid length
        self.assertFalse(credit_card_validator('730946709430106542'))

    def test_invalid_19_digit(self):
        # invalid prefix with valid length and valid checksum
        self.assertFalse(credit_card_validator('7718953209133728422'))

    def test_invalid_19_digit_2(self):
        # invalid prefix and invalid checksum with valid length
        self.assertFalse(credit_card_validator('7718953209133728421'))

    def test_invalid_exceed_length(self):
        # 20 digits exceeds length, but valid checksum and prefix (visa)
        self.assertFalse(credit_card_validator('49003001172256730444'))

    def test_invalid_exceed_length_2(self):
        # 20 digits exceeds length, but valid checksum and prefix (amex)
        self.assertFalse(credit_card_validator('340030011722567304441'))

    def test_invalid_exceed_length_3(self):
        # 20 digits exceeds length, but valid checksum and prefix (amex)
        self.assertFalse(credit_card_validator('370030011722567304444'))

    def test_invalid_exceed_length_4(self):
        # 20 digits exceeds length, but valid checksum and prefix (mastercard)
        self.assertFalse(credit_card_validator('5100300117225673044445'))

    def test_invalid_exceed_length_6(self):
        # 20 digits exceeds length, but valid checksum and prefix (mastercard)
        self.assertFalse(credit_card_validator('22213001172256730440'))

    def test_valid_amex_test_card(self):
        # https://support.bluesnap.com/docs/test-credit-card-numbers
        self.assertTrue(credit_card_validator('374245455400126'))

    def test_valid_amex_test_card_2(self):
        # https://docs.adyen.com/development-resources/testing/test-card-numbers#american-express-amex
        self.assertTrue(credit_card_validator('370000000100018'))

    def test_valid_amex_prefix(self):
        # testing a valid card with correct prefix, length and checksum
        self.assertTrue(credit_card_validator('340000000100007'))

    def test_invalid_amex_prefix_1(self):
        # valid length and checksum but invalid prefix
        self.assertFalse(credit_card_validator('380000000100013'))

    def test_invalid_amex_prefix_2(self):
        # valid length and checksum but invalid prefix
        self.assertFalse(credit_card_validator('350000000100012'))

    def test_invalid_amex_prefix_3(self):
        # valid length and checksum but invalid prefix
        self.assertFalse(credit_card_validator('360000000100010'))

    def test_invalid_amex_prefix_4(self):
        # valid length and checksum but invalid prefix
        self.assertFalse(credit_card_validator('320000000100019'))

    def test_invalid_amex_length(self):
        # too long, valid prefix and checksum
        self.assertFalse(credit_card_validator('3400000001000074'))

    def test_invalid_amex_length_2(self):
        # too short
        self.assertFalse(credit_card_validator('37000000000007'))

    def test_invalid_amex_length_3(self):
        # too short, valid prefix and checksum
        self.assertFalse(credit_card_validator('34000000000000'))

    def test_invalid_amex_length_4(self):
        # Test AMEX prefix with valid check sum but invalid length for amex(10)
        self.assertFalse(credit_card_validator('3761510449'))

    def test_invalid_amex_length_5(self):
        # too long, valid prefix and checksum
        self.assertFalse(credit_card_validator('3700000001000071'))

    def test_invalid_amex_checksum(self):
        # Test valid AMEX prefix and length but invalid checksum
        self.assertFalse(credit_card_validator('370000000100012'))

    def test_invalid_amex_checksum_2(self):
        # Test valid AMEX prefix and length but invalid checksum
        self.assertFalse(credit_card_validator('340000000100012'))

    def test_valid_visa_test_card_1(self):
        self.assertTrue(credit_card_validator('4111111145551142'))

    def test_valid_visa_test_card_2(self):
        self.assertTrue(credit_card_validator('4988438843884305'))

    def test_invalid_visa_checksum(self):
        # visa prefix and valid length with invalid checksum
        self.assertFalse(credit_card_validator('4111112014267666'))

    def test_invalid_visa_length(self):
        # too short (length 15) with incorrect checksum
        self.assertFalse(credit_card_validator('498843884388430'))

    def test_invalid_visa_length_2(self):
        # too short (length 15) with correct checksum
        self.assertFalse(credit_card_validator('498843884388432'))

    def test_invalid_visa_length_3(self):
        # too long (length 17) with correct checksum and prefix
        self.assertFalse(credit_card_validator('49884388438843051'))

    def test_invalid_visa_length_4(self):
        # too long (length 17) and incorrect checksum
        self.assertFalse(credit_card_validator('49884388438843052'))

    def test_invalid_mastercard_prefix_1(self):
        # boundary check, invalid prefix and invalid checksum with valid length
        self.assertFalse(credit_card_validator('5000800050018002'))

    def test_invalid_mastercard_prefix_2(self):
        # boundary check, invalid prefix with valid checksum and length
        self.assertFalse(credit_card_validator('5000800050018003'))

    def test_invalid_mastercard_prefix_3(self):
        # boundary check, invalid prefix with valid checksum and valid length
        self.assertFalse(credit_card_validator('5600800050018007'))

    def test_invalid_mastercard_prefix_4(self):
        # boundary check, invalid prefix and invalid checksum with valid length
        self.assertFalse(credit_card_validator('5600800050018008'))

    def test_invalid_mastercard_prefix_5(self):
        # boundary check, invalid prefix but valid length and checksum
        self.assertFalse(credit_card_validator('2820007000260017'))

    def test_invalid_mastercard_prefix_8(self):
        # valid length but invalid prefix and invalid checksum
        self.assertFalse(credit_card_validator('2220080005001800'))

    def test_invalid_mastercard_prefix_9(self):
        # valid length and checksum but invalid prefix
        self.assertFalse(credit_card_validator('2220080005001807'))

    def test_invalid_mastercard_prefix_10(self):
        # valid length and checksum but invalid prefix
        self.assertFalse(credit_card_validator('2721080005001801'))

    def test_invalid_mastercard_prefix_11(self):
        # valid length but invalid checksum and invalid prefix
        self.assertFalse(credit_card_validator('2721080005001802'))

    def test_invalid_mastercard_length(self):
        # valid prefix and checksum but invalid length (too long)
        self.assertFalse(credit_card_validator('55008000500180076'))

    def test_invalid_mastercard_length_2(self):
        # valid checksum but invalid length (too short) and invalid prefix (boundary)
        self.assertFalse(credit_card_validator('560080005001874'))

    def test_invalid_mastercard_length_3(self):
        # valid prefix and checksum but invalid length (too short)
        self.assertFalse(credit_card_validator('222180005001872'))

    def test_invalid_mastercard_length_4(self):
        # valid prefix and checksum but invalid length (too short)
        self.assertFalse(credit_card_validator('272080005001873'))

    def test_invalid_mastercard_length_5(self):
        # valid prefix and checksum but invalid length (too long)
        self.assertFalse(credit_card_validator('27208000500187368'))

    def test_invalid_mastercard_length_6(self):
        # valid prefix and checksum but invalid length (too long)
        self.assertFalse(credit_card_validator('2221000500187363'))

    def test_invalid_mastercard_length_7(self):
        # valid checksum but invalid length (too short) and invalid prefix (boundary)
        self.assertFalse(credit_card_validator('500080005001877'))

    def test_invalid_mastercard_length_8(self):
        # valid checksum and prefix but invalid length (too short)
        self.assertFalse(credit_card_validator('510080005001875'))

    def test_invalid_mastercard_length_9(self):
        # valid checksum and prefix but invalid length (too short)
        self.assertFalse(credit_card_validator('550080005001876'))

    def test_invalid_mastercard_checksum(self):
        # valid prefix and length but invalid checksum
        self.assertFalse(credit_card_validator('513456789012346'))

    def test_invalid_mastercard_checksum_2(self):
        # valid prefix and length but invalid checksum
        self.assertFalse(credit_card_validator('523456789012346'))

    def test_invalid_mastercard_checksum_3(self):
        # valid prefix and length but invalid checksum
        self.assertFalse(credit_card_validator('2221567890123463'))

    def test_invalid_mastercard_checksum_4(self):
        # valid prefix and length but invalid checksum
        self.assertFalse(credit_card_validator('27205678901234639'))

    def test_invalid_mastercard_checksum_5(self):
        # valid prefix and length but invalid checksum
        self.assertFalse(credit_card_validator('553456789012343'))

    def test_invalid_mastercard_checksum_6(self):
        # valid prefix and length but invalid checksum
        self.assertFalse(credit_card_validator('27195678901234634'))

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
        self.assertTrue(credit_card_validator('2222000900180041'))

    def test_valid_mastercard_8(self):
        self.assertTrue(credit_card_validator('2250987654321026'))

    def test_valid_mastercard_9(self):
        self.assertTrue(credit_card_validator('2720007000260018'))

    def test_valid_mastercard_10(self):
        self.assertTrue(credit_card_validator('2719234567890127'))


if __name__ == '__main__':
    unittest.main()
