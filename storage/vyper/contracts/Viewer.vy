interface Storage:
    def get() -> uint256: view
    # def set(uint256)   # We could define the set method here but want to try raw call

# Private state variables
# NB: order of definition is important if using delegate_call to contract with state variables
# In the called contract the state variables from this contract are mapped in the same order to
# the state variables in the called contract

# storage: Storage   # Uncomment to test failure

# For testing delegate_call
local_stored_data: uint256

storage: address    # Comment to test failure


@external
def __init__(_storage : address):
    self.local_stored_data = 0
    self.storage = _storage


@external
@view
def view() -> uint256:
    # Call to storage contract
    return Storage(self.storage).get()


@external
@view
def view_local() -> uint256:
    # Local data
    return self.local_stored_data


@external
def set(_new_value : uint256):
    # Call to storage contract via raw_call

    data : Bytes[36] = concat(method_id('set(uint256)', output_type=Bytes[4]), convert(_new_value, bytes32))
    _res : Bytes[32] = raw_call(self.storage, data, max_outsize=32, gas=msg.gas, is_delegate_call=False)


@external
def set_local(_new_value : uint256):
    # Call to storage contract via raw_call using delegate_call
    # Note that this sets the local_stored_data variable in this contract

    data : Bytes[36] = concat(method_id('set(uint256)', output_type=Bytes[4]), convert(_new_value, bytes32))
    _res : Bytes[32] = raw_call(self.storage, data, max_outsize=32, gas=msg.gas, is_delegate_call=True)
