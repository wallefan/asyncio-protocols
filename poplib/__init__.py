import asyncio

class POP3(asyncio.Protocol):
    def __init__(self):
        super().__init__()
        self._mutex=asyncio.Lock()
        
    def connection_made(self, transport):
        self._transport=transport
        self._pending_operations=[]
    
    def data_received(self, data):
        data = self._newline_decoder.decode(data)
        if '\n' in data:
            pass
        (mode, fut, arg) = self._pending_operations[-1]
        if mode=='feed':
            arg.feed(
    
    async def getresp(self, mode='line', arg=None):
        if mode=='line':
