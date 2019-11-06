/**
 * Use this file to configure your truffle project. It's seeded with some
 * common settings for different networks and features like migrations,
 * compilation and testing. Uncomment the ones you need or modify
 * them to suit your project as necessary.
 *
 * More information about configuration can be found at:
 *
 * truffleframework.com/docs/advanced/configuration
 *
 * To deploy via Infura you'll need a wallet provider (like truffle-hdwallet-provider)
 * to sign your transactions before they're sent to a remote public node. Infura API
 * keys are available for free at: infura.io/register
 *
 * You'll also need a mnemonic - the twelve word phrase the wallet uses to generate
 * public/private key pairs. If you're publishing your code to GitHub make sure you load this
 * phrase from a file you've .gitignored so it doesn't accidentally become public.
 *
 */

// const HDWallet = require('truffle-hdwallet-provider');
// const infuraKey = "fj4jll3k.....";
//
// const fs = require('fs');
// const mnemonic = fs.readFileSync(".secret").toString().trim();

require("@babel/polyfill");  // See https://github.com/hussy-io/truffle-ledger-provider/issues/9

const LedgerWalletProvider = require('truffle-ledger-provider');
const fs = require('fs');
let rawdata = fs.readFileSync("config.json");
let web3_config = JSON.parse(rawdata);
console.log(web3_config['infura_project_id']);

const INFURA_APIKEY = web3_config['infura_project_id']; // set your Infura API key
const ledgerOptions = {
  networkId: 3, // mainnet
  path: "44'/60'/0'/0/0", // Ethereum Ledger Live path
  // path: "44'/60'/0'/0", // ledger default derivation path
  // askConfirm: false,
  // accountsLength: 1,
  accountsOffset: 0
}; // use default options

module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",
      port: 7545,
      network_id: "*",
    },
    ropsten: {
      provider: new LedgerWalletProvider(ledgerOptions, `https://ropsten.infura.io/${INFURA_APIKEY}`),
      network_id: 3,
      gas: 4600000
    }
  }
};
