// SPDX-License-Identifier: MIT


pragma solidity ^0.6.6;
pragma experimental ABIEncoderV2;

contract Sharer {

    constructor() public{
        for (uint256 i = 0; i < 1000; i = i + 1){
            string[] storage new2;
            MessageRequests[i] = new2;
        }
    }

    mapping(uint256 => string[]) public MessageRequests;
    //string[1000][] public MessageRequests;


    function IwantToContact(string memory encryptedMessage, uint256 id) public {
        MessageRequests[id].push(encryptedMessage);
    }

    function hashAddress(address add) public pure returns(uint256){
        uint256 x = uint256(uint160(add));
        return x % 1000;
    }

    function getDataFrom(uint256 start) public view returns(string[] memory){
        uint256 myId = hashAddress(msg.sender);


        string[] memory lookingAt = MessageRequests[myId];
        uint256 numNew = lookingAt.length - start + 1;
        string[] memory out = new string[](numNew);
        uint256 counter = 0;
        for (uint256 i = start; i < lookingAt.length; i = i + 1){
            out[counter] = lookingAt[i];
        }
        return out;
    }
}