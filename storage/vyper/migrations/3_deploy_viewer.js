var VyperStorage = artifacts.require("VyperStorage")
var Viewer = artifacts.require("Viewer");

module.exports = function(deployer) {
  deployer.deploy(Viewer, VyperStorage.address);
};
