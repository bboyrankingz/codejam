package codinjam;

import adventcode.ChecksumTest;
import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

public class LevenshteinTest extends TestCase {

    private final Levenshtein levenshtein = new Levenshtein();

    public LevenshteinTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(ChecksumTest.class);
    }



    public void test_should_have_2_sequence_in_simple_words() {
        assertEquals(levenshtein.operations("book", "back"), 2);
    }

    public void test_should_have_3_sequence_in_normal_words() {
        assertEquals(levenshtein.operations("kitten", "sitting"), 3);
    }

    public void test_should_have_0_sequence_when_no_words() {
        assertEquals(levenshtein.operations("", ""), 0);
    }
}