// SPDX-License-Identifier: MIT


pragma solidity ^0.6.6;
pragma experimental ABIEncoderV2;

contract Sharer {

    mapping(uint256 => bytes[]) public MessageRequests;

    mapping(address => bytes) public publicKeys;
    mapping(address => bytes) public privateKeys;

    function addPublicKey(bytes memory b) public{
        publicKeys[msg.sender] = b;
    }

    function getPubKey(address add) public view returns(bytes memory){
        return publicKeys[add];
    }

    function addPrivateKey(bytes memory b) public{
        privateKeys[msg.sender] = b;
    }

    function getPrivateKey(address add) public view returns(bytes memory){
        return privateKeys[add];
    }

    function checkUser() public view returns(bool){
        if(publicKeys[msg.sender].length> 0){
            return true;
        }
        else{
            return false;
        }
    }

    function IwantToContact(bytes memory encryptedMessage, uint256 id) public {
        MessageRequests[id].push(encryptedMessage);
    }

    function getDataBasic() public view returns(bytes[] memory){
        return MessageRequests[msg.sender];
    }
}