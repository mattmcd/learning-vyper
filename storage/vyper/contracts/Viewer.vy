
contract Storage:
    def get() -> uint256: constant

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

