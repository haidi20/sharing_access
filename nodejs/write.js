// // Import dependencies
// const SerialPort = require("serialport").SerialPort;

// // Defining the serial port
// // const port = new SerialPort("COM5");
// const port = new SerialPort({ path: "/dev/COM5", baudRate: 4800 });

// const person = {
//     name: "Bob",
//     age: 23
// }

// // Write the data to the serial port
// port.write(JSON.stringify(person));

const { SerialPort, ReadlineParser } = require('serialport');
const port = new SerialPort({ path: "COM5", baudRate: 4800 });

// const parser = new ReadlineParser();
// port.pipe(parser)
// parser.on('data', console.log)
// port.write('ROBOT PLEASE RESPOND\n')
// ROBOT ONLINE

// Creating the parser and piping can be shortened to
// const parser = port.pipe(new ReadlineParser())