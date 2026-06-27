import java.net.*;
public class Server{
public static void main(String[] a)throws Exception{
ServerSocket ss=new ServerSocket(5000);
System.out.println("Server started");
ss.close();
}}
