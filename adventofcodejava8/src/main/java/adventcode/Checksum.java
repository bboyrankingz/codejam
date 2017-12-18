package adventcode;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;


public class Checksum
{

    public int check(List<Integer> integers) {
        return integers.stream().max(Comparator.naturalOrder()).orElse(0) - integers.stream().min(Comparator.naturalOrder()).orElse(0) ;
    }

    public int check2(ArrayList<Integer> integers) {
        integers.sort(Comparator.reverseOrder());
        int i = -1;
        while (i < integers.size()) {
            i += 1;
            for (int j = i + 1; j < integers.size(); j++){
                float divid = (float) integers.get(i) / integers.get(j);
                if (Math.round(divid) == divid) {
                    return (int) divid;
                }
            }
        }
        return 0;
    }

    public int sumAll(List<List<Integer>> lists) {
        return lists.stream().mapToInt(this::check).sum();
    }

    public static void main( String[] args )
    {
        System.out.println("zz");
    }
}
