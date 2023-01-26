// Import dependencies
const { SerialPortStream } = require('@serialport/stream')
const { MockBinding } = require('@serialport/binding-mock')

// Create a port and enable the echo and recording.
MockBinding.createPort('/dev/COM1', { echo: true, record: true })
const port = new SerialPortStream({ binding: MockBinding, path: '/dev/COM6', baudRate: 14400 })

if (port) {
    console.info("work");
}

port.on('open', () => {
    port.port.emitData('pretend data from device')
})
port.on('close', () => {
    port.port.emitData('close device')
})