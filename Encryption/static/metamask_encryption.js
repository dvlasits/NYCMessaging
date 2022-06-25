let account;
let public_key_eth;

async function check_metamask(){
    if (window.ethereum) {
        window.web3 = new Web3(ethereum);
        await ethereum.enable()
            .then(() => {
                console.log("Ethereum enabled");
            })
            .catch(() => {
                console.warn('User didn\'t allow access to accounts.');
                waitLogin();
            });
    } else {
        console.log("Non-Ethereum browser detected. You should consider installing MetaMask.");
        return;
    }
}

async function get_account() {
    await web3.eth.getAccounts(function (err, acc) {
        if (err != null) {
            self.setStatus("There was an error fetching your accounts");
            return;
        }
        if (acc.length > 0) {
            console.log('Accounts:')
            console.log(acc);

            account = acc[0];
        }
        else {
            console.error("No account can be accessed.");
        }
    });
}

async function get_public_key(){
    await ethereum
    .request({
      method: 'eth_getEncryptionPublicKey',
      params: [account], // you must have access to the specified account
    })
    .then((result) => {
        console.log('The public key for the first account is:')
        console.log(result);
        public_key_eth = result;
    })
    .catch((error) => {
      if (error.code === 4001) {
        // EIP-1193 userRejectedRequest error
        console.log("We can't encrypt anything without the key.");
      } else {
        console.error(error);
      }
    });
}

function encrypt_wrapper(message) {
    encrypted = my_encrypt(public_key_eth, message);

    console.log(encrypted);
    return encrypted;
}

async function decrypt(message) {
    let decrypted;
    await ethereum
    .request({
      method: 'eth_decrypt',
      params: [message, account],
    })
    .then((decryptedMessage) => {
        decrypted = decryptedMessage;
        console.log('The decrypted message is:', decryptedMessage);
    }
    )
    .catch((error) => console.log(error.message));

    return decrypted;
}
