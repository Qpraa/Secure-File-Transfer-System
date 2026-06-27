import java.net.*;import java.io.*;
public class Client{
public static void main(String[] a)throws Exception{
Socket s=new Socket("localhost",5000);
System.out.println("Secure file transfer client started");
s.close();
}}
