event ValueSet:
    _oldValue: uint256
    _newValue: uint256

stored_data: uint256

@external
def set(new_value : uint256):
    _oldValue : uint256 = self.stored_data
    log ValueSet(_oldValue, new_value)

    self.stored_data = new_value

@external
def get() -> uint256:
    return self.stored_data
