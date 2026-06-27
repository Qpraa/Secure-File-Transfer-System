import java.io.*;
public class FileManager{
public static byte[] readFile(String p)throws Exception{
File f=new File(p);
byte[] b=new byte[(int)f.length()];
new FileInputStream(f).read(b);
return b;
}}
