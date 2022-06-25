const Crypto = require("crypto");

window.generate_key_pair = () => {
    const { publicKey, privateKey } = Crypto.generateKeyPairSync("rsa", {
        // The standard secure default length for RSA keys is 2048 bits
        modulusLength: 2048,
    });

    return  { publicKey, privateKey };
}

window.encrypt_data = (data, publicKey) => {
    const encryptedData = Crypto.publicEncrypt(
        {
          key: publicKey,
          padding: Crypto.constants.RSA_PKCS1_OAEP_PADDING,
          oaepHash: "sha256",
        },
        // We convert the data string to a buffer using `Buffer.from`
        Buffer.from(data)
    );
    
    return encryptedData;
}

window.decrypt_data = (data, privateKey) => {
    const decryptedData = Crypto.privateDecrypt(
        {
          key: privateKey,
          // In order to decrypt the data, we need to specify the
          // same hashing function and padding scheme that we used to
          // encrypt the data in the previous step
          padding: Crypto.constants.RSA_PKCS1_OAEP_PADDING,
          oaepHash: "sha256",
        },
        data
    );
    
    return decryptedData;
}

/*let {publicKey, privateKey} = generate_key_pair();


const data = "my secret data";
encrypted = encrypt_data(data, publicKey);

console.log("encypted data: ", encrypted.toString("base64"));

const decrypted = decrypt_data(encrypted, privateKey);

console.log("decrypted data: ", decrypted.toString());*/