package codinjam;

import java.util.*;
import java.util.stream.*;

import static java.util.stream.Collectors.toList;

public class Levenshtein {

    public static int operations(String word1, String word2) {
        Integer n = word1.length();
        Integer m = word2.length();

        List<String> xWord = Stream.of(word1.split("")).collect(toList());
        List<String> yWord = Stream.of(word2.split("")).collect(toList());

        List<List<Integer>> matrice = IntStream.range(0, n + 1).boxed().map(i ->
                IntStream.range(0, m + 1).boxed().map(j -> j + i).collect(toList()))
                .collect(toList());

        IntStream.range(0, n).forEach(i -> IntStream.range(0, m).forEach(j -> {
            Integer a = xWord.get(i).equals(yWord.get(j)) ? 0 : 1;
            matrice.get(i + 1).add(j + 1, IntStream.of(matrice.get(i).get(j + 1) + 1,
                    matrice.get(i + 1).get(j) + 1,
                    matrice.get(i).get(j) + a).min().getAsInt());
        }));

        return matrice.get(n).get(m);
    }
}
