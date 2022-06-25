// bundle this using: browserify encryption.js -o bundle.js

const ethUtil = require('ethereumjs-util');
const sigUtil = require('@metamask/eth-sig-util');

window.my_encrypt = (encryptionPublicKey, message) => {
    const encryptedMessage = ethUtil.bufferToHex(
        Buffer.from(
          JSON.stringify(
            sigUtil.encrypt({
              publicKey: encryptionPublicKey,
              data: message,
              version: 'x25519-xsalsa20-poly1305',
            })
          ),
          'utf8'
        )
      );

      return encryptedMessage
};


