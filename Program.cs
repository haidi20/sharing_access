using System;
using System.Data.OleDb;

class HelloWorld
{
    static void Main()
    {
      // string coba = "coba";
      // Connection string and SQL query    
      // string connectionString = @ "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=D:\timbang\DatabaseWb.mdb;";  
      string strSQL = "SELECT * FROM TbTransCustomer";  
      // Create a connection    
      using(OleDbConnection connection = new OleDbConnection("Provider=Microsoft.JET.OLEDB.4.0;" + "data source=D:\\timbang\\DatabaseWb.mdb;Password=")) {  
          // Create a command and set its connection    
          OleDbCommand command = new OleDbCommand(strSQL, connection);  
          // Open the connection and execute the select command.    
          try {  
              // Open connecton    
              connection.Open();  
              // Execute command    
              using(OleDbDataReader reader = command.ExecuteReader()) {  
                  Console.WriteLine("------------Original data----------------");  
                  while (reader.Read()) {  
                      Console.WriteLine("{0} {1}", reader["DATEIN"].ToString());  
                  }  
              }  
          } catch (Exception ex) {  
              Console.WriteLine(ex.Message);  
          }  
          // The connection is automatically closed becasuse of using block.    
      }  
      Console.ReadKey(); 
    }
}