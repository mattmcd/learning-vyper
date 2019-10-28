contract Storage:
    def get() -> uint256: constant
    # def set(uint256)   # We could define the set method here but want to try raw call

# Private state variables
# NB: order of definition is important if using delegate_call to contract with state variables
# In the called contract the state variables from this contract are mapped in the same order to
# the state variables in the called contract

# storage: Storage   # Uncomment to test failure

# For testing delegate_call
local_stored_data: uint256

storage: Storage    # Comment to test failure


@public
def __init__(_storage : address):
    self.local_stored_data = 0
    self.storage = Storage(_storage)


@public
@constant
def view() -> uint256:
    # Call to storage contract
    return self.storage.get()


@public
@constant
def view_local() -> uint256:
    # Local data
    return self.local_stored_data


@public
def set(_new_value : uint256):
    # Call to storage contract via raw_call

    data : bytes[36] = concat(method_id('set(uint256)', bytes[4]), convert(_new_value, bytes32))
    _res : bytes[32] = raw_call(self.storage.address, data, outsize=32, gas=msg.gas, delegate_call=False)


@public
def set_local(_new_value : uint256):
    # Call to storage contract via raw_call using delegate_call
    # Note that this sets the local_stored_data variable in this contract

    data : bytes[36] = concat(method_id('set(uint256)', bytes[4]), convert(_new_value, bytes32))
    _res : bytes[32] = raw_call(self.storage.address, data, outsize=32, gas=msg.gas, delegate_call=True)
