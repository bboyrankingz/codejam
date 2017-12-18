package adventcode;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

import static com.google.common.collect.Lists.newArrayList;

/**
 * Unit test for simple App.
 */
public class ChecksumTest
        extends TestCase {
    private final Checksum checksum = new Checksum();

    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public ChecksumTest(String testName) {
        super(testName);
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite() {
        return new TestSuite(ChecksumTest.class);
    }

    public void testChecksumPart1() {

        assertEquals(checksum.check(newArrayList(5, 1, 9, 5)), 8);
        assertEquals(checksum.check(newArrayList(7, 5, 3)), 4);
        assertEquals(checksum.check(newArrayList(2, 4, 6, 8)), 6);
    }

    public void testSumAllPart1() {

        assertEquals(checksum.sumAll(newArrayList(
                newArrayList(5, 1, 9, 5),
                newArrayList(7, 5, 3),
                newArrayList(2, 4, 6, 8))), 18);
    }
}
