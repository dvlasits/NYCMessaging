window.get_crypto_object = (password) => { 
    var cryptico = require("cryptico");

    function cryptoObj(passPhrase)
    {
       this.bits = 1024; //2048;
       this.passPhrase = passPhrase;
       this.rsaKey = cryptico.generateRSAKey(this.passPhrase,this.bits);
       this.rsaPublicKey = cryptico.publicKeyString(this.rsaKey);

       this.encrypt = function(message){
         var result = cryptico.encrypt(message,this.rsaPublicKey);
         return result.cipher;
       };

       this.decrypt = function(message){
         var result = cryptico.decrypt(message, this.rsaKey);
         return result.plaintext;
       };
    }


    return new cryptoObj(Math.random(password));
}

window.encrypt_RSA = (message, publicKey) => { 
    var cryptico = require("cryptico");
       
    var result = cryptico.encrypt(message,publicKey);
    return result.cipher;
}