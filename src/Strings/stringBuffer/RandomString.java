package Strings.stringBuffer;

import java.util.Random;

class RandomString {
    static String generate(int size) {
        StringBuffer buffer = new StringBuffer(size);

        Random random = new Random();

        for(int i = 0; i < size; i++) {
            int randomChar =  97 + (int)(random.nextFloat() * 26);
            buffer.append((char)randomChar);
        }

        return buffer.toString();
    }
}
