let address = '0x56bb189a3DC216523a9E34E6e707969318D5eaEa';
let abi = [{"inputs":[{"internalType":"bytes","name":"encryptedMessage","type":"bytes"}],"name":"IwantToContact","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"MessageRequests","outputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"bytes","name":"encReceiver","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes","name":"b","type":"bytes"}],"name":"addEncPrivateKey","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes","name":"b","type":"bytes"}],"name":"addPublicKey","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"checkUser","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"add","type":"address"}],"name":"getEncPrivateKey","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getMessageRequest","outputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"bytes","name":"encReceiver","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getMessageRequestLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"add","type":"address"}],"name":"getPubKey","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"privateKeys","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"publicKeys","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"}];
const apiKey = "0aadf3e86f0a447faf1cc5d7c76f0c58"


let smartC = undefined;

async function initStuff() {
    const provider = new ethers.providers.Web3Provider(window.ethereum)
    await provider.send("eth_requestAccounts", []);
    //const signer = await provider.getSigner();
    smartC = new ethers.Contract(address, abi, provider);
}

async function getMessageRequestLength() {
    let result = await smartC.getMessageRequestLength();
    console.log("Checkpoint")
    return result;
}