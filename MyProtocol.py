import crc8
import time

class SimpleProtocolFactory:
    def __init__(self, DLE = b'\xff', STX = b'\x80', ETX = b'\x81', callback = None, databytes = 0) -> None:
        self.DLE = DLE
        self.STX = STX
        self.ETX = ETX
        self.callback = callback
        self.databytes = databytes

    def create(self):
        if self.DLE == None:
            return SimpleLoopProtocol(self.callback, self.databytes)
        elif self.databytes == 0:
            return SimpleVariableProtocol(self.DLE, self.STX, self.ETX, self.callback)
        else:
            return SimpleStaticProtocol(self.DLE, self.STX, self.ETX, self.callback, self.databytes)
    
    def setDLE(self, DLE):
        self.DLE = DLE
    def setSTX(self, STX):
        self.STX = STX
    def setETX(self, ETX):
        self.ETX = ETX
    def setCallback(self, callback):
        self.callback = callback
    def setDatabytes(self, databytes):
        self.databytes = databytes
    
class SimpleLoopProtocol:
    def __init__(self, callback, databytes) -> None:
        self._callback = callback
        self._databytes = databytes
        self._buffer = b''
        self._counter = 0
        self._timeDiff = 0
        self._timeCheckPoint = 0

    def check(self, data):
        self._buffer += data
        self._counter += 1
        if self._counter == self._databytes:
            self._timer()
            self._callback(self._buffer, self._timeDiff)
            self._counter = 0
            self._buffer = b''

    def _timer(self):
        temp = time.time()
        self._timeDiff = temp - self._timeCheckPoint
        self._timeCheckPoint = temp

class SimpleStaticProtocol:
    def __init__(self, dle, stx, etx, callback, databytes) -> None:
        self._dle = dle
        self._stx = stx
        self._etx = etx
        self._callback = callback
        self._databytes = databytes

        self._state = self._ENTRY
        self._buffer = b''
        self._counter = 0
        self._checksum = False
        self._timeDiff = time.time()
        self._timeCheckPoint = 0

    def check(self, data):
        self._state(data)
    
    def timeout(self):
        self._state = self._ENTRY

    def _ENTRY(self, data):
        if data == self._dle:
            self._timer()
            self._state = self._STX

    def _STX(self, data):
        if data == self._stx:
            self._counter = 0
            self._buffer = b''
            self._state = self._DATA
        elif data == self._dle:
            self._Err("Unexpected data from STX")
        else:
            self._state = self._ENTRY
            self._Err("Unexpected data from STX")

    def _DATA(self, data):
        self._counter += 1
        if self._counter <= self._databytes:
            self._buffer += data
        else:
            self._calcCRC(data)
            self._state = self._FULL

    def _FULL(self, data):
        if data == self._dle:
            self._state = self._ETX
        else:
            self._state = self._ENTRY
            self._Err("Unexpected data from FULL")
        
    def _ETX(self, data):
        if data == self._etx:
            if self._checksum:
                self._callback(self._buffer, self._timeDiff)
            else:
                self._Err('Checksum Dismatch')
            self._state = self._ENTRY
        elif data == self._dle:
            self._state = self._STX
            self._Err("Unexpected data from ETX")
        else:
            self._state = self._ENTRY
            self._Err("Unexpected data from ETX")

    def _calcCRC(self, data):
        crc = crc8.crc8()
        crc.update(self._buffer)
        if data == crc.digest():
            self._checksum = True
        else:
            self._checksum = False
    
    def _timer(self):
        temp = time.time()
        self._timeDiff = temp - self._timeCheckPoint
        self._timeCheckPoint = temp

    def _Err(self, err):
        print(err)

class SimpleVariableProtocol:
    def __init__(self, dle, stx, etx, callback) -> None:
        self._dle = dle
        self._stx = stx
        self._etx = etx
        self._callback = callback

        self._state = self._ENTRY
        self._buffer = b''
        self._checksum = False
    
    def check(self, data):
        self._state(data)

    def timeout(self):
        self._state = self._ENTRY

    def _ENTRY(self, data):
        if data == self._dle:
            self._state = self._STX

    def _STX(self, data):
        pass

    def _calcCRC(self, data):
        crc = crc8.crc8()
        crc.update(self._buffer)
        if data == crc.digest():
            self._checksum = True
        else:
            self._checksum = False
    
    def _Err(self, err):
        print(err)
