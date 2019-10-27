contract Storage:
    def get() -> uint256: constant
    # def set(uint256)   # We could define the set method here but want to try raw call

storage: Storage


@public
def __init__(_storage : address):
    self.storage = Storage(_storage)


@public
@constant
def view() -> uint256:
    # Call to storage contract
    _res : uint256 = self.storage.get()
    return _res


@public
def set(_new_value : uint256):
    # Call to storage contract via raw_call

    data : bytes[36] = concat(method_id('set(uint256)', bytes[4]), convert(_new_value, bytes32))
    _res : bytes[32] = raw_call(self.storage.address, data, outsize=32, gas=msg.gas, delegate_call=False)
