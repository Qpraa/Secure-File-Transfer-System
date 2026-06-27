import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
public class EncryptionModule{
public static byte[] encrypt(byte[] d,String k)throws Exception{
Cipher c=Cipher.getInstance("AES");
c.init(Cipher.ENCRYPT_MODE,new SecretKeySpec(k.getBytes(),"AES"));
return c.doFinal(d);
}}
