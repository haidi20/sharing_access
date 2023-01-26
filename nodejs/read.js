// Import dependencies
const { SerialPortStream } = require('@serialport/stream')
const { SerialPort } = require('serialport')
const { MockBinding } = require('@serialport/binding-mock')

// Create a port and enable the echo and recording.
// MockBinding.createPort('/dev/COM1', { echo: true, record: true })
// const port = new SerialPortStream({ binding: MockBinding, path: '/dev/COM1', baudRate: 14400 })
const port = new SerialPort({ path: '/COM1', baudRate: 9600 })

if (port) {
    console.info("work");
}

port.on('open', () => {
    // port.port.emitData('pretend data from device')
    console.log('pretend data from device')
})
port.on('close', () => {
    // port.port.emitData('close device')
    port.port.emitData('close device')
})
port.on('data', function(data) {
    const intData = parseInt(data, 16);
    const floatData = parseFloat(data);
    // console.log('Data:', data.toString());
    // console.log('Data type', typeof(data));
    // console.log(isNaN(intData));
    if (!isNaN(intData)) {
        // if (intData > 0) {
        console.log("valueInt " + intData);
        console.log("valueFloat " + floatData);
        // }
    }
    // console.log("valueString " + data.toString());
    // console.log("length " + data.length);
    // console.log('Data int', intData);
    // console.log('Data float', floatData);

})