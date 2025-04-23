import java.nio.ByteBuffer;
import java.nio.IntBuffer;
import java.util.Arrays;

/* loaded from: classes.dex */
public class pain {    
    /* renamed from: a */
    public static ByteBuffer m13963a(ByteBuffer payload, ByteBuffer key) {
        byte[] bArr = new byte[payload.limit() - payload.position()];
        payload.get(bArr);
        ByteBuffer smth = ByteBuffer.wrap(bArr);
        return m13961c(smth, key);
    }

    // switches from array to ByteBuffer (no change to contents)
    /* renamed from: b */
    public static byte[] custom_xxtea_encrypt(byte[] payload, byte[] key) {
        return m13963a(ByteBuffer.wrap(payload), ByteBuffer.wrap(key)).array();
    }

    private static String byteArrayToHexString(byte[] byteArray) {
        StringBuilder result = new StringBuilder();
        for (byte b : byteArray) {
            result.append(String.format("%02X", b));
        }
        return result.toString();
    }

    /* renamed from: c */
    public static ByteBuffer m13961c(ByteBuffer payload, ByteBuffer key) {
        m13960d(payload.asIntBuffer(), key.asIntBuffer());
        byte[] byteArray = new byte[payload.remaining()];
        payload.get(byteArray);
        System.out.println(byteArrayToHexString(byteArray));
        return payload;
    }

    /* renamed from: d */
    public static IntBuffer m13960d(IntBuffer payload, IntBuffer key) {
        if (key.limit() == 4) {
            if (payload.limit() < 2) {
                return payload;
            }
            int i = payload.get(0);
            int limit = ((52 / payload.limit()) + 6) * (-1640531527);
            int limit2 = payload.limit();
            do {
                int i2 = (limit >>> 2) & 3;
                int limit3 = payload.limit() - 1;
                while (limit3 > 0) {
                    int i3 = payload.get(limit3 - 1);
                    i = payload.get(limit3) - (((i ^ limit) + (i3 ^ key.get((limit3 & 3) ^ i2))) ^ (((i3 >>> 5) ^ (i << 2)) + ((i >>> 3) ^ (i3 << 4))));
                    payload.put(limit3, i);
                    limit3--;
                }
                int i4 = payload.get(limit2 - 1);
                i = payload.get(0) - (((i ^ limit) + (key.get(i2 ^ (limit3 & 3)) ^ i4)) ^ (((i4 >>> 5) ^ (i << 2)) + ((i >>> 3) ^ (i4 << 4))));
                payload.put(0, i);
                limit += 1640531527;
            } while (limit != 0);
            return payload;
        }
        throw new IllegalArgumentException("XXTEA needs a 128-bits key");
    }

    // helper function
    private static byte[] hexStringToByteArray(String hexString) {
        int length = hexString.length();
        if (length % 2 != 0) {
            throw new IllegalArgumentException("Hex string must have an even number of characters");
        }

        byte[] byteArray = new byte[length / 2];
        for (int i = 0; i < length; i += 2) {
            byteArray[i / 2] = (byte) ((Character.digit(hexString.charAt(i), 16) << 4)
                    + Character.digit(hexString.charAt(i + 1), 16));
        }

        return byteArray;
    }
    
    // main class
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java <program> <hexString>");
            System.exit(1);
        }

        String hexString = args[0];

        try {
            byte[] payload = hexStringToByteArray(hexString);
            custom_xxtea_encrypt(payload, "tuoroLreWlacrAoh".getBytes());
        } catch (IllegalArgumentException e) {
            System.out.println("Invalid hex string: " + e.getMessage());
        }
    }
}