from MyGui import Ui_MainWindow
from MySerial import ReaderThread
from MyProtocol import SimpleProtocolFactory
import serial
import crc8

class MyEvents:
    FORMAT_ASCII, FORMAT_HEX, FORMAT_DEC = (0, 1, 2)
    PROTOCOL_NONE, PROTOCOL_STATIC, PROTOCOL_VARIABLE = (0, 1, 2)
    SAMPLING_1HZ, SAMPLING_2HZ, SAMPLING_10HZ, SAMPLING_20HZ = ('1.00', '0.50', '0.10', '0.05')
    PORTS = ['COM1', 'COM2', 'COM3', 'COM4', 'COM5']
    BAUDS = [1200, 2400, 4800, 9600, 14400, 19200, 115200]
    DATAS = [serial.FIVEBITS, serial.SIXBITS, serial.SEVENBITS, serial.EIGHTBITS]
    STOPS = [serial.STOPBITS_ONE, serial.STOPBITS_ONE_POINT_FIVE, serial.STOPBITS_TWO]
    PARITYS = [serial.PARITY_NONE, serial.PARITY_EVEN, serial.PARITY_ODD, serial.PARITY_MARK, serial.PARITY_SPACE]
    PROTOCOLS = [PROTOCOL_NONE, PROTOCOL_STATIC, PROTOCOL_VARIABLE]
    FORMATS = [FORMAT_ASCII, FORMAT_HEX, FORMAT_DEC]
    SAMPLINGS = [SAMPLING_1HZ, SAMPLING_2HZ, SAMPLING_10HZ, SAMPLING_20HZ]
    RATES = [1, 2, 10, 20]

    def __init__(self, ui:Ui_MainWindow):
        self.ui = ui
        self.port = None
        self.baud = 9600
        self.data = serial.EIGHTBITS
        self.stop = serial.STOPBITS_ONE
        self.parity = serial.PARITY_NONE
        self.protocol = self.PROTOCOL_NONE
        self.format = self.FORMAT_ASCII
        self.sampling_rate = self.SAMPLING_1HZ
        self.serial = serial.Serial()
        
        self.isConnected = False
        self.first_timediff = True
        self.recieve_count = 0
        self.outlier_count = 0
        self.command_STX = b'\x80'
        self.command_active_mask = 128

        self.connecting()

    #----------------------------------------------------------------------------------------------------
    
    def connecting(self):
        self.ui.connect_button.clicked.connect(self.connect_button_listner)
        self.ui.clear_button.clicked.connect(self.clrear_button_listner)
        self.ui.outlier_checking_button.clicked.connect(self.outlier_checking_button_listner)
        self.ui.send_button.clicked.connect(self.send_button_listner)
        self.ui.port_box.currentIndexChanged.connect(self.port_box_listner)
        self.ui.baud_box.currentIndexChanged.connect(self.baud_box_listner)
        self.ui.data_box.currentIndexChanged.connect(self.data_box_listner)
        self.ui.stop_box.currentIndexChanged.connect(self.stop_box_listner)
        self.ui.parity_box.currentIndexChanged.connect(self.parity_box_listner)
        self.ui.protocol_box.currentIndexChanged.connect(self.protocol_box_listner)
        self.ui.format_box.currentIndexChanged.connect(self.format_box_listner)
        self.ui.sampling_box.currentIndexChanged.connect(self.sampling_box_listner)
        self.protocolFactory = SimpleProtocolFactory(callback=self.protocol_listner)

    def connect_button_listner(self):
        if self.port == None:
            self.ui.packet_list_widget.addItem("Please Select Port")
            return
        if self.isConnected:
            self._closeConnection()
            self.ui.connect_button.setText("Connect")
            self.isConnected = False
            self._properties_enable(True)
            self._clearCount()
        else:
            self._openConnection()
            self.ui.connect_button.setText("Disconnect")
            self.isConnected = True
            self._properties_enable(False)
    def clrear_button_listner(self):
        self.ui.packet_list_widget.clear()
        if self.ui.outlier_checking_button.isChecked():
            self._clearCount()
    def outlier_checking_button_listner(self):
        if self.ui.outlier_checking_button.isChecked():
            self.ui.sampling_box.setEnabled(True)
            self.ui.recieved_text.setEnabled(True)
            self.ui.outliers_text.setEnabled(True)
            self.ui.ratio_text.setEnabled(True)
            self.ui.sampling_box.setCurrentIndex(0)
            self.ui.recieved_text.setText('0')
            self.ui.outliers_text.setText('0')
            self.ui.ratio_text.setText('0')
        else:
            self.ui.sampling_box.setEnabled(False)
            self.ui.recieved_text.setEnabled(False)
            self.ui.outliers_text.setEnabled(False)
            self.ui.ratio_text.setEnabled(False)
            self.ui.sampling_box.setCurrentIndex(-1)
            self.ui.recieved_text.clear()
            self.ui.outliers_text.clear()
            self.ui.ratio_text.clear()
    def send_button_listner(self):
        length = self.ui.change_data_length_text.text()
        rate = self.ui.change_sampling_rate_box.currentIndex()
        if length != None and length != '':
            command_length = int(length) | self.command_active_mask
        else:
            command_length = 0
        command_rate = self.RATES[rate] | self.command_active_mask
        command = command_length.to_bytes(1, 'big') + command_rate.to_bytes(1, 'big')
        crc = crc8.crc8()
        crc.update(command)
        command += crc.digest()
        command = self.command_STX + command
        if self.reader is not None and command is not None:
            self.reader.write(command, int(length))
    def port_box_listner(self, index):
        self.port = self.PORTS[index]
    def baud_box_listner(self, index):
        self.baud = self.BAUDS[index]
    def data_box_listner(self, index):
        self.data = self.DATAS[index]
    def stop_box_listner(self, index):
        self.stop = self.STOPS[index]
    def parity_box_listner(self, index):
        self.parity = self.PARITYS[index]
    def protocol_box_listner(self, index):
        self.protocol = self.PROTOCOLS[index]
        self._protocol_properties_enable(True)
    def format_box_listner(self, index):
        self.format = self.FORMATS[index]
    def sampling_box_listner(self, index):
        self.sampling_rate = self.SAMPLINGS[index]
    def protocol_listner(self, data, timeDiff):
        message = self._format_convert(data)
        if self.ui.outlier_checking_button.isChecked():
            message += ' ' + self._check_outlier(timeDiff)
        self.ui.packet_list_widget.addItem(message)
        self.ui.packet_list_widget.scrollToBottom()

    #----------------------------------------------------------------------------------------------------

    def _openConnection(self):
        self._serialUpdate()
        self._protocolUpdate()
        self.reader = ReaderThread(self.serial, self.protocolFactory)
        self.reader.start()

    def _closeConnection(self):
        self.reader.close()
        self.reader = None

    def _serialUpdate(self):
        self.serial.port = self.port
        self.serial.baudrate = self.baud
        self.serial.bytesize = self.data
        self.serial.stopbits = self.stop
        self.serial.parity = self.parity
        self.serial.timeout = 1

    def _protocolUpdate(self):
        if self.protocol == self.PROTOCOL_NONE:
            self.protocolFactory.DLE = None
            self.protocolFactory.STX = None
            self.protocolFactory.ETX = None
            self.protocolFactory.databytes = int(self.ui.datalength_text.text())
        elif self.protocol == self.PROTOCOL_STATIC:
            self.protocolFactory.DLE = self._str2byte(self.ui.dle_text.text())
            self.protocolFactory.STX = self._str2byte(self.ui.stx_text.text())
            self.protocolFactory.ETX = self._str2byte(self.ui.etx_text.text())
            self.protocolFactory.databytes = int(self.ui.datalength_text.text())
        else:
            self.protocolFactory.DLE = self._str2byte(self.ui.dle_text.text())
            self.protocolFactory.STX = self._str2byte(self.ui.stx_text.text())
            self.protocolFactory.ETX = self._str2byte(self.ui.etx_text.text())
            self.protocolFactory.databytes = 0

    def _properties_enable(self, enable:bool):
        self.ui.port_box.setEnabled(enable)
        self.ui.baud_box.setEnabled(enable)
        self.ui.data_box.setEnabled(enable)
        self.ui.stop_box.setEnabled(enable)
        self.ui.parity_box.setEnabled(enable)
        self.ui.protocol_box.setEnabled(enable)

        self.ui.change_data_length_text.setEnabled(not enable)
        self.ui.change_sampling_rate_box.setEnabled(not enable)
        self.ui.send_button.setEnabled(not enable)

        self._protocol_properties_enable(enable)
    
    def _protocol_properties_enable(self, enable:bool):
        if self.protocol == self.PROTOCOL_NONE:
            self.ui.dle_text.setEnabled(False)
            self.ui.stx_text.setEnabled(False)
            self.ui.etx_text.setEnabled(False)
            self.ui.datalength_text.setEnabled(enable)
        elif self.protocol == self.PROTOCOL_STATIC:
            self.ui.dle_text.setEnabled(enable)
            self.ui.stx_text.setEnabled(enable)
            self.ui.etx_text.setEnabled(enable)
            self.ui.datalength_text.setEnabled(enable)
        else:
            self.ui.dle_text.setEnabled(enable)
            self.ui.stx_text.setEnabled(enable)
            self.ui.etx_text.setEnabled(enable)
            self.ui.datalength_text.setEnabled(False)

    def _format_convert(self, data):
        message = ''
        if self.format == self.FORMAT_ASCII:
            for row in data:
                row_byte = bytes([row])
                try:
                    message += row_byte.decode('ascii')
                except UnicodeDecodeError:
                    message += '?'
            message += ' '
            message = message.replace('\x00', '?')
        elif self.format == self.FORMAT_HEX:
            for row in data:
                row_hex = format(row, '02X')
                message += row_hex + ' '
        else:
            for row in data:
                message += str(row) + ' '
        return message[0:-1]

    def _check_outlier(self, timeDiff):
        self.recieve_count += 1
        message = 'Time Diff: '
        timeDiff_str = format(timeDiff, '.2f')
        if self.first_timediff:
            self.first_timediff = False
            self._countUpdate()
            return message + 'First'
        if timeDiff_str != self.sampling_rate:
            self.outlier_count += 1
        self._countUpdate()
        return message + timeDiff_str

    def _countUpdate(self):
        ratio = (self.outlier_count / self.recieve_count) * 100
        self.ui.recieved_text.setText(str(self.recieve_count))
        self.ui.outliers_text.setText(str(self.outlier_count))
        self.ui.ratio_text.setText(format(ratio, '.1f'))

    def _str2byte(self, text) -> bytes:
        val_str = '0x' + text
        val_int = int(val_str, 16)
        return bytes([val_int])

    def _clearCount(self):
        self.ui.recieved_text.setText('0')
        self.ui.outliers_text.setText('0')
        self.ui.ratio_text.setText('0')
        self.recieve_count = 0
        self.outlier_count = 0
        self.first_timediff = True
