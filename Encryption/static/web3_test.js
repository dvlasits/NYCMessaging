async function web3_test (){ 
    const abi = [{"inputs":[{"internalType":"bytes","name":"encryptedMessage","type":"bytes"}],"name":"IwantToContact","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"MessageRequests","outputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"bytes","name":"encReceiver","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes","name":"b","type":"bytes"}],"name":"addEncPrivateKey","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes","name":"b","type":"bytes"}],"name":"addPublicKey","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"checkUser","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"add","type":"address"}],"name":"getEncPrivateKey","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"getMessageRequest","outputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"bytes","name":"encReceiver","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getMessageRequestLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"add","type":"address"}],"name":"getPubKey","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"privateKeys","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"publicKeys","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"}];
    const apiKey = "_T9lFqMsIObf3Rhya7UlrMckFSReF3Y0";
    address = "0x56bb189a3DC216523a9E34E6e707969318D5eaEa";

    window.ethereum.enable()

    const provider = new ethers.providers.Web3Provider(window.ethereum, "any");

    let contract = new ethers.Contract(address, abi, provider)

    //let length = await contract.getMessageRequestLength();
    //console.log(length);

    //const provider2 = new ethers.providers.Web3Provider(window.ethereum, "any");
    // Prompt user for account connections
    await provider.send("eth_requestAccounts", []);
    const signer = provider.getSigner();

    contract.addPublicKey("0x0123456789abcdef", signer)
}


