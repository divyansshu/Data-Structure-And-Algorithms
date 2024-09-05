package Strings;

public class countNumberOfWords {

    public static void main(String[] args) {

         String[] sentences = {"please wait", "continue to fight", "continue to win"};

         // method 1
        int max = 0;
        int count = 0;

        for(int i = 0; i < sentences.length; i++) {

            String str = sentences[i];
            for(int j = 0; j < str.length(); j++) {
                if(str.charAt(j) == ' ') {
                    count++;
                }
            }
            count += 1;

            if(count >= max) {
                max = count;
            }
            count = 0;

        }

        System.out.println(max);

//        method 2
        int maxWords = 0;
        for(String sentence: sentences) {
            String[] words = sentence.split("\\s+");
            int wordsCount = words.length;
            maxWords = Math.max(maxWords, wordsCount);
        }

        System.out.println(maxWords);


    }
}
