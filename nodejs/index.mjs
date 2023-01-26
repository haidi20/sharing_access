import odbc from "odbc";

const connectionString = "DSN=timbangan;UID=admin;PWD=password;DBQ=D:/timbang/DatabaseWb.mdb;";

odbc.connect(connectionString, (error, connection) => {
    if (error) {
        console.error(error);
        return;
    }
    // your code here

    connection.query("SELECT * FROM TbTransCustomer", (error, result) => {
        if (error) {
            console.error(error);
            return;
        }

        console.log(result);
    });
});