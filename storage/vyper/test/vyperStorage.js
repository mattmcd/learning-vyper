const VyperStorage = artifacts.require("VyperStorage");
const Viewer = artifacts.require("Viewer");

contract("VyperStorage", () => {
  it("...should store the value 89.", async () => {
    const storage = await VyperStorage.deployed();

    // Set value of 89
    await storage.set(89);

    // Get stored value
    const storedData = await storage.get();

    assert.equal(storedData, 89, "The value 89 was not stored.");
  });
});

contract("Viewer", () => {
  it("... should get the value from storage", async () => {
    const viewer = await Viewer.deployed();

    // Set value of 145 through viewer
    await viewer.set(145);

    // Get stored value via viewer
    const storedData = await viewer.view();
    assert.equal(storedData, 145, "The value 145 was not stored.");
  })
});

contract("Viewer", () => {
  it("... should get the value from local after setting via delegate call", async () => {
    const viewer = await Viewer.deployed();

    // Set value of 145 through viewer
    await viewer.set_local(145);

    // Get stored value via viewer
    const storedData = await viewer.view_local();
    assert.equal(storedData, 145, "The value 145 was not stored.");
  })
});