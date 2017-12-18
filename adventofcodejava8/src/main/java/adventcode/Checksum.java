package adventcode;

import java.util.Comparator;
import java.util.List;


public class Checksum
{

    public int check(List<Integer> integers) {
        return integers.stream().max(Comparator.naturalOrder()).get() - integers.stream().min(Comparator.naturalOrder()).get() ;
    }

    public int sumAll(List<List<Integer>> lists) {
        return lists.stream().mapToInt(this::check).sum();
    }

    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
    }
}
