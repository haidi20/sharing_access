import { readFileSync } from "fs";
import MDBReader from "mdb-reader";

const path = "D:/timbang/DatabaseWb.mdb";
// const path = "//DESKTOP-N0ELQRQ/timbang/DatabaseWb.mdb";
const query = 'SELECT TOP 10 * FROM TbTransCustomer tc ORDER BY DATEIN DESC';

const buffer = readFileSync(path);
const reader = new MDBReader(buffer);

const table = reader.getTable("TbTransCustomer");
// table.getColumnNames(); // ['id', 'name', 'color']

console.log(table.getData());