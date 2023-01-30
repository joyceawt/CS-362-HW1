import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):
    def test_invalid_0_digit(self):
        """
        Given that a min of 10 digits is required for a valid credit card, this
        ensures that not having an input returns as false. An empty value is
        a common test for invalid numbers.
        """
        self.assertFalse(credit_card_validator(''))

    def test_invalid_1_digit(self):
        """
        This tests that credit card numbers with a valid visa prefix
        but invalid length and checksums are flagged as invalid credit cards.
        """
        self.assertFalse(credit_card_validator('4'))

    def test_invalid_2_digit(self):
        """
        This tests that credit card numbers with a valid AMEX prefix
        but invalid length and checksums are flagged as invalid credit cards.
        """
        self.assertFalse(credit_card_validator('34'))

    def test_invalid_2_digit_2(self):
        """
        This tests that credit card numbers with a valid AMEX prefix
        but invalid length and checksums are flagged as invalid credit cards.
        """
        self.assertFalse(credit_card_validator('37'))

    def test_invalid_2_digit_3(self):
        """
        This tests that credit card numbers with a valid mastercard prefix
        but invalid length and checksums are flagged as invalid credit cards.
        51 was chosen as its the beginning of the range 51-55.
        """
        self.assertFalse(credit_card_validator('51'))

    def test_invalid_2_digit_4(self):
        """
        This tests that credit card numbers with a valid mastercard prefix
        but invalid length and checksums are flagged as invalid credit cards.
        55 was chosen as its the end of the range 51-55.
        """
        self.assertFalse(credit_card_validator('55'))

    def test_invalid_2_digit_5(self):
        """
        This tests the boundary of mastercard prefix given that only 51-55
        are acceptable. It also tests invalid length and checksums are not
        allowed.
        """
        self.assertFalse(credit_card_validator('50'))

    def test_invalid_2_digit_6(self):
        """
        This tests that credit card numbers with a valid mastercard prefix
        but invalid length and checksums are flagged as invalid credit cards.
        52 was chosen as it is between 51-55.
        """
        self.assertFalse(credit_card_validator('52'))

    def test_invalid_4_digit(self):
        """
        This tests that credit card numbers with a valid mastercard prefix
        but invalid length and checksums are flagged as invalid credit cards.
        2221 was chosen as its the beginning of the range 2221-2720.
        """
        self.assertFalse(credit_card_validator('2221'))

    def test_invalid_4_digit_2(self):
        """
        This tests that credit card numbers with a valid mastercard prefix
        but invalid length and checksums are flagged as invalid credit cards.
        2720 was chosen as its the end of the range 2221-2720.
        """
        self.assertFalse(credit_card_validator('2720'))

    def test_invalid_4_digit_3(self):
        """
        This tests that credit card numbers with a valid mastercard prefix
        but invalid length and checksums are flagged as invalid credit cards.
        2321 was chosen as its between the range 2221-2720.
        """
        self.assertFalse(credit_card_validator('2321'))

    def test_invalid_4_digit_4(self):
        """
        This tests that credit card numbers with an invalid mastercard prefix.
        2721 was chosen as its the boundary of the range 2221-2720.
        """
        self.assertFalse(credit_card_validator('2721'))

    def test_invalid_9_digit(self):
        """
        This tests that credit cards with 9 digits, right outside the boundary
        of 10-19 digits but with correct checksums are invalid.
        """
        self.assertFalse(credit_card_validator('326151040'))

    def test_invalid_10_digit(self):
        """
        This tests that credit cards with 10 digits with a valid checksum but
        invalid prefix and length is flagged as invalid. 10 was chosen as its
        the beginning of the range 10-19.
        """
        self.assertFalse(credit_card_validator('3661510440'))

    def test_invalid_10_digit_2(self):
        """
        This tests that credit cards with 10 digits with a valid AMEX prefix
        but invalid checksum and length is flagged as invalid. 10 was chosen as
        its the beginning of the range 10-19.
        """
        self.assertFalse(credit_card_validator('3761510448'))

    def test_invalid_11_digit(self):
        """
        This tests that credit cards with 11 digits (valid length), a valid
        checksum and an invalid prefix. 11 is within the range of 10-19 so it
        was chosen.
        """
        self.assertFalse(credit_card_validator('31455071568'))

    def test_invalid_11_digit_2(self):
        """
        This tests that credit cards with 11 digits (valid length), with an
        invalid checksum and an invalid prefix. 11 is within the range of 10-19
        so it was chosen.
        """
        self.assertFalse(credit_card_validator('31455071566'))

    def test_invalid_12_digit(self):
        """
        This tests that credit cards with 12 digits (valid length), a valid
        checksum and an invalid prefix. 12 is within the range of 10-19 so it
        was chosen.
        """
        self.assertFalse(credit_card_validator('334256427868'))

    def test_invalid_12_digit_2(self):
        """
        This tests that credit cards with 12 digits (valid length), with an
        invalid checksum and an invalid prefix. 12 is within the range of 10-19
        so it was chosen.
        """
        self.assertFalse(credit_card_validator('334256427865'))

    def test_invalid_13_digit(self):
        """
        This tests that credit cards with 13 digits (valid length), a valid
        checksum and an invalid prefix. 13 is within the range of 10-19 so it
        was chosen.
        """
        self.assertFalse(credit_card_validator('1690512642015'))

    def test_invalid_13_digit_2(self):
        """
        This tests that credit cards with 13 digits (valid length), with an
        invalid checksum and an invalid prefix. 13 is within the range of 10-19
        so it was chosen.
        """
        self.assertFalse(credit_card_validator('1690512642012'))

    def test_invalid_14_digit(self):
        """
        This tests that credit cards with 14 digits (valid length), a valid
        checksum and an invalid prefix. 14 is within the range of 10-19 so it
        was chosen.
        """
        self.assertFalse(credit_card_validator('71566889496372'))

    def test_invalid_14_digit_2(self):
        """
        This tests that credit cards with 14 digits (valid length), with an
        invalid checksum and an invalid prefix. 14 is within the range of 10-19
        so it was chosen.
        """
        self.assertFalse(credit_card_validator('71566889496371'))

    def test_invalid_15_digit(self):
        """
        This tests that credit cards with 15 digits (valid length), a valid
        checksum and an invalid prefix. 15 is within the range of 10-19 so it
        was chosen.
        """
        self.assertFalse(credit_card_validator('683074087568241'))

    def test_invalid_15_digit_2(self):
        """
        This tests that credit cards with 15 digits (valid length), with an
        invalid checksum and an invalid prefix. 15 is within the range of 10-19
        so it was chosen.
        """
        self.assertFalse(credit_card_validator('683074087568240'))

    def test_invalid_16_digit(self):
        """
        This tests that credit cards with 16 digits (valid length), with an
        invalid checksum and an invalid prefix. 16 is within the range of 10-19
        so it was chosen.
        """
        self.assertFalse(credit_card_validator('9723233384426542'))

    def test_invalid_17_digit(self):
        """
        This tests that credit cards with 17 digits (valid length), a valid
        checksum and an invalid prefix. 17 is within the range of 10-19 so it
        was chosen.
        """
        self.assertFalse(credit_card_validator('99055597294275368'))

    def test_invalid_17_digit_2(self):
        """
        This tests that credit cards with 17 digits (valid length), with an
        invalid checksum and an invalid prefix. 17 is within the range of 10-19
        so it was chosen.
        """
        self.assertFalse(credit_card_validator('99055597294275364'))

    def test_invalid_18_digit(self):
        """
        This tests that credit cards with 18 digits (valid length), a valid
        checksum and an invalid prefix. 18 is within the range of 10-19 so it
        was chosen.
        """
        self.assertFalse(credit_card_validator('730946709430106547'))

    def test_invalid_18_digit_2(self):
        """
        This tests that credit cards with 18 digits (valid length), with an
        invalid checksum and an invalid prefix. 18 is within the range of 10-19
        so it was chosen.
        """
        self.assertFalse(credit_card_validator('730946709430106542'))

    def test_invalid_19_digit(self):
        """
        This tests that credit cards with 19 digits (valid length), a valid
        checksum and an invalid prefix. 19 is within the range of 10-19 so it
        was chosen.
        """
        self.assertFalse(credit_card_validator('7718953209133728422'))

    def test_invalid_19_digit_2(self):
        """
        This tests that credit cards with 19 digits (valid length), with an
        invalid checksum and an invalid prefix. 19 is within the range of 10-19
        so it was chosen.
        """
        self.assertFalse(credit_card_validator('7718953209133728421'))

    def test_invalid_exceed_length(self):
        """
        This tests that credit cards outside the boundary of the acceptable
        range of 10-19 digits are not allowed. The cc number also has a valid
        checksum and prefix (visa).
        """
        self.assertFalse(credit_card_validator('49003001172256730444'))

    def test_invalid_exceed_length_2(self):
        """
        This tests that credit cards outside the boundary of the acceptable
        range of 10-19 digits are not allowed. The cc number also has a valid
        checksum and prefix (AMEX).
        """
        self.assertFalse(credit_card_validator('340030011722567304441'))

    def test_invalid_exceed_length_3(self):
        """
        This tests that credit cards outside the boundary of the acceptable
        range of 10-19 digits are not allowed. The cc number also has a valid
        checksum and prefix (AMEX).
        """
        self.assertFalse(credit_card_validator('370030011722567304444'))

    def test_invalid_exceed_length_4(self):
        """
        This tests that credit cards outside the boundary of the acceptable
        range of 10-19 digits are not allowed. The cc number also has a valid
        checksum and prefix (mastercard).
        """
        self.assertFalse(credit_card_validator('5100300117225673044445'))

    def test_invalid_exceed_length_6(self):
        """
        This tests that credit cards outside the boundary of the acceptable
        range of 10-19 digits are not allowed. The cc number also has a valid
        checksum and prefix (mastercard).
        """
        self.assertFalse(credit_card_validator('22213001172256730440'))

    def test_valid_amex_test_card(self):
        """
        This uses a real AMEX test card number to check that it is correctly
        identified.
        """
        self.assertTrue(credit_card_validator('374245455400126'))

    def test_valid_amex_test_card_2(self):
        """
        This uses a real AMEX test card number to check that it is correctly
        identified.
        """
        self.assertTrue(credit_card_validator('370000000100018'))

    def test_valid_amex_prefix(self):
        """
        This tests that AMEX prefixes of 34 with valid checksums and length
        pass as valid cards.
        """
        self.assertTrue(credit_card_validator('340000000100007'))

    def test_invalid_amex_prefix(self):
        """
        This tests that cards with incorrect AMEX prefixes with valid length
        and checksums are flagged as invalid. 38 was chosen as its outside
        the numbers of 34 and 37 but still starts with a 3.
        """
        self.assertFalse(credit_card_validator('380000000100013'))

    def test_invalid_amex_length(self):
        """
        This tests that cards with valid AMEX prefixes, valid checksums
        but invalid length are flagged as invalid. The length is larger than
        the constraint of 15 digits.
        """
        self.assertFalse(credit_card_validator('3400000001000074'))

    def test_invalid_amex_length_2(self):
        """
        This tests that cards with valid AMEX prefixes, valid checksums
        but invalid length are flagged as invalid. The length is shorter
        than the constraint of 15 digits.
        """
        self.assertFalse(credit_card_validator('37000000000007'))

    def test_invalid_amex_length_3(self):
        """
        This tests that cards with valid AMEX prefixes, valid checksums
        but invalid length are flagged as invalid. The length is shorter
        than the constraint of 15 digits.
        """
        self.assertFalse(credit_card_validator('34000000000000'))

    def test_invalid_amex_length_4(self):
        """
        This tests that cards with valid AMEX prefixes, valid checksums
        but invalid length are flagged as invalid. The length is shorter
        than the constraint of 15 digits.
        """
        self.assertFalse(credit_card_validator('3761510449'))

    def test_invalid_amex_length_5(self):
        """
        This tests that cards with valid AMEX prefixes, valid checksums
        but invalid length are flagged as invalid. The length is larger than
        the constraint of 15 digits.
        """
        self.assertFalse(credit_card_validator('3700000001000071'))

    def test_invalid_amex_checksum(self):
        """
        This tests that cards with valid AMEX prefixes, valid length
        but invalid checksums are flagged as invalid.
        """
        self.assertFalse(credit_card_validator('370000000100012'))

    def test_invalid_amex_checksum_2(self):
        """
        This tests that cards with valid AMEX prefixes, valid length
        but invalid checksums are flagged as invalid.
        """
        self.assertFalse(credit_card_validator('340000000100012'))

    def test_valid_visa_test_card_1(self):
        """
        This tests with a valid visa test card to ensure that correct
        card numbers are identified correctly.
        """
        self.assertTrue(credit_card_validator('4111111145551142'))

    def test_valid_visa_test_card_2(self):
        """
        This tests with a valid visa test card to ensure that correct
        card numbers are identified correctly.
        """
        self.assertTrue(credit_card_validator('4988438843884305'))

    def test_invalid_visa_checksum(self):
        """
        This tests that cards with valid VISA prefixes, valid length
        but invalid checksums are flagged as invalid.
        """
        self.assertFalse(credit_card_validator('4111112014267666'))

    def test_invalid_visa_length(self):
        """
        This tests that cards with valid VISA prefixes, valid checksums
        but invalid length are flagged as invalid. The cc number is too
        short and falls below 16 digits.
        """
        self.assertFalse(credit_card_validator('498843884388430'))

    def test_invalid_visa_length_2(self):
        """
        This tests that cards with valid VISA prefixes, valid checksums
        but invalid length are flagged as invalid. The cc number is too
        short and falls below 16 digits.
        """
        self.assertFalse(credit_card_validator('498843884388432'))

    def test_invalid_visa_length_3(self):
        """
        This tests that cards with valid VISA prefixes, valid checksums
        but invalid length are flagged as invalid. The cc number is too
        long and goes above 16 digits.
        """
        self.assertFalse(credit_card_validator('49884388438843051'))

    def test_invalid_visa_length_4(self):
        """
        This tests that cards with valid VISA prefixes but incorrect
        checksum and lengths are flagged as invalid. The cc number is
        too long and goes above 16 digits.
        """
        self.assertFalse(credit_card_validator('49884388438843052'))

    def test_invalid_mastercard_prefix_1(self):
        """
        This is a boundary check for mastercard prefixes between 51-55.
        50 is chosen as it is below the boundary. The card also has an invalid
        checksum despite a valid length.
        """
        self.assertFalse(credit_card_validator('5000800050018002'))

    def test_invalid_mastercard_prefix_2(self):
        """
        This is a boundary check for mastercard prefixes between 51-55.
        50 is chosen as it is below the boundary. The card has a valid
        checksum and a valid length.
        """
        self.assertFalse(credit_card_validator('5000800050018003'))

    def test_invalid_mastercard_prefix_3(self):
        """
        This is a boundary check for mastercard prefixes between 51-55.
        56 is chosen as it is above the boundary. The card has a valid
        checksum and a valid length.
        """
        self.assertFalse(credit_card_validator('5600800050018007'))

    def test_invalid_mastercard_prefix_4(self):
        """
        This is a boundary check for mastercard prefixes between 51-55.
        56 is chosen as it is above the boundary. The card also has an
        invalid checksum despite a valid length.
        """
        self.assertFalse(credit_card_validator('5600800050018008'))

    def test_invalid_mastercard_prefix_5(self):
        """
        This is a boundary check for mastercard prefixes between 2221-2720.
        2820 is chosen as it is above the boundary. The card also has a
        valid length and checksum.
        """
        self.assertFalse(credit_card_validator('2820007000260017'))

    def test_invalid_mastercard_prefix_8(self):
        """
        This is a boundary check for mastercard prefixes between 2221-2720.
        2220 is chosen as it is below the boundary. The card also has an
        invalid checksum despite valid length.
        """
        self.assertFalse(credit_card_validator('2220080005001800'))

    def test_invalid_mastercard_prefix_9(self):
        """
        This is a boundary check for mastercard prefixes between 2221-2720.
        2220 is chosen as it is below the boundary. The card also has a
        valid checksum and valid length.
        """
        self.assertFalse(credit_card_validator('2220080005001807'))

    def test_invalid_mastercard_prefix_10(self):
        """
        This is a boundary check for mastercard prefixes between 2221-2720.
        2721 is chosen as it is right above the boundary. The card also has a
        valid length and checksum.
        """
        self.assertFalse(credit_card_validator('2721080005001801'))

    def test_invalid_mastercard_prefix_11(self):
        """
        This is a boundary check for mastercard prefixes between 2221-2720.
        2721 is chosen as it is right above the boundary. The card also has an
        invalid checksum despite valid length.
        """
        self.assertFalse(credit_card_validator('2721080005001802'))

    def test_invalid_mastercard_length(self):
        """
        This is a length check for mastercard with valid prefix and checksums.
        It has a length of 17, which is too long for the constraint of 16.
        """
        self.assertFalse(credit_card_validator('55008000500180076'))

    def test_invalid_mastercard_length_2(self):
        """
        This is a length check for mastercard with valid checksum but invalid
        prefix (boundary, 56 is right above 55). The cc number is short of a
        digit.
        """
        self.assertFalse(credit_card_validator('560080005001874'))

    def test_invalid_mastercard_length_3(self):
        """
        This is a length check for mastercard with valid checksum and valid
        prefix. The cc number is short of a digit.
        """
        self.assertFalse(credit_card_validator('222180005001872'))

    def test_invalid_mastercard_length_4(self):
        """
        This is a length check for mastercard with valid checksum and valid
        prefix. The cc number is short of a digit.
        """
        self.assertFalse(credit_card_validator('272080005001873'))

    def test_invalid_mastercard_length_5(self):
        """
        This is a length check for mastercard with valid checksum and valid
        prefix. The cc number has an extra digit.
        """
        self.assertFalse(credit_card_validator('27208000500187368'))

    def test_invalid_mastercard_length_6(self):
        """
        This is a length check for mastercard with valid checksum and valid
        prefix. The cc number has an extra digit.
        """
        self.assertFalse(credit_card_validator('22210005001873636'))

    def test_invalid_mastercard_length_7(self):
        """
        This is a length check for mastercard with valid checksum but invalid
        prefix (at boundary value of 50, below 51). The cc number is short of
        a digit.
        """
        self.assertFalse(credit_card_validator('500080005001877'))

    def test_invalid_mastercard_length_8(self):
        """
        This is a length check for mastercard with valid checksum and valid
        prefix. The cc number is short of a digit.
        """
        self.assertFalse(credit_card_validator('510080005001875'))

    def test_invalid_mastercard_length_9(self):
        """
        This is a length check for mastercard with valid checksum and valid
        prefix. The cc number is short of a digit.
        """
        self.assertFalse(credit_card_validator('550080005001876'))

    def test_invalid_mastercard_checksum(self):
        """
        This checks invalid checksums for mastercards with valid prefix and
        valid length.
        """
        self.assertFalse(credit_card_validator('5134567890123462'))

    def test_invalid_mastercard_checksum_2(self):
        """
        This checks invalid checksums for mastercards with valid prefix and
        valid length.
        """
        self.assertFalse(credit_card_validator('5234567890123411'))

    def test_invalid_mastercard_checksum_3(self):
        """
        This checks invalid checksums for mastercards with valid prefix and
        valid length.
        """
        self.assertFalse(credit_card_validator('2221567890123463'))

    def test_invalid_mastercard_checksum_4(self):
        """
        This checks the checksum for mastercards with valid prefix but
        invalid length (too long) and invalid checksum.
        """
        self.assertFalse(credit_card_validator('27205678901234639'))

    def test_invalid_mastercard_checksum_5(self):
        """
        This checks invalid checksums for mastercards with valid prefix and 
        valid length.
        """
        self.assertFalse(credit_card_validator('5534567890123432'))

    def test_invalid_mastercard_checksum_6(self):
        """
        This checks invalid checksum for mastercards with invalid length
        and prefix.
        """
        self.assertFalse(credit_card_validator('27195678901234633'))

    def test_invalid_mastercard_checksum_7(self):
        """
        This checks invalid checksum for mastercards with valid prefix and
        length.
        """
        self.assertFalse(credit_card_validator('2720567890123463'))

    def test_valid_mastercard_1(self):
        """
        This checks valid mastercards with correct length, prefix and
        checksums are correctly identified. 51 is the lower value of
        the prefix range of 51-55.
        """
        self.assertTrue(credit_card_validator('5134567890123454'))

    def test_valid_mastercard_2(self):
        """
        This checks valid mastercards with correct length, prefix and
        checksums are correctly identified. 52 is within the prefix
        range of 51-55.
        """
        self.assertTrue(credit_card_validator('5234567890123438'))

    def test_valid_mastercard_3(self):
        """
        This checks valid mastercards with correct length, prefix and
        checksums are correctly identified. 55 is the high value of the
        prefix range of 51-55.
        """
        self.assertTrue(credit_card_validator('5534567890123468'))

    def test_valid_mastercard_4(self):
        """
        This checks valid mastercards with correct length, prefix and
        checksums are correctly identified. 2221 is the low value of
        the prefix range of 2221-2720.
        """
        self.assertTrue(credit_card_validator('2221000900180042'))

    def test_valid_mastercard_5(self):
        """
        This checks valid mastercards with correct length, prefix and
        checksums are correctly identified. 2222 is within the
        the prefix range of 2221-2720.
        """
        self.assertTrue(credit_card_validator('2222000900180041'))

    def test_valid_mastercard_6(self):
        """
        This checks valid mastercards with correct length, prefix and
        checksums are correctly identified. 2720 is the high value of
        the prefix range of 2221-2720.
        """
        self.assertTrue(credit_card_validator('2720007000260018'))


if __name__ == '__main__':
    unittest.main()
