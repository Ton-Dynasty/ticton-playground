# TICTON Playground
This repository is primarily for the **TICTON quote testing event tutorial**. Everyone can refer to this document to complete the quote and claim rewards. Those who successfully follow the tutorial can obtain a TICTON-exclusive NFT. In the future, holders of these NFTs will have priority in participating in airdrops and other events.

If you have any questions, feel free to join our [community](https://t.me/TictonOfficial) and discuss with us.

**The following steps will be conducted on TON's testnet!**

## Table of Contents
  - [1. How to Install](#1-how-to-install)
  - [2. Mining Testnet USDT](#2-mining-testnet-usdt)
  - [3. Checking the Current TON/USDT Price](#3-checking-the-current-tonusdt-price)
  - [4. Tick](#4-tick)
  - [5.Getting Alarm Metadata](#5getting-alarm-metadata)
  - [6. Ring](#6-ring)
  - [7. Wind (Advanced)](#7-wind-advanced)
   
## 1. How to Install
    
First, ensure your Python environment meets the version requirements: `Python version >= 3.10 and < 3.12`. The first step is to git clone this repo, then to install the ticton package, please execute the following command in your terminal:

```bash
git clone https://github.com/Ton-Dynasty/ticton-playground.git
cd ticton-playground
pip install -r requirements.txt
cp .env.example .env
```
**Please ensure that you have filled out the `.env` file before proceeding with the following steps.**

TONCENTER_API_KEY can apply at [@tonapibot](https://t.me/tonapibot).

## 2. Mining Testnet USDT
    
Next, we will simulate the quotation process for the TON/USDT token pair on the testnet. Ensure you have sufficient funds for the operation. 

- If your TON balance is low, you can obtain additional TON from the [@testgiver_ton_bot](https://t.me/testgiver_ton_bot) on Telegram.
- You can visit [tonviewer-USDT](https://testnet.tonviewer.com/EQBqSpvo4S87mX9tjHaG4zhYZeORhVhMapBJpnMZ64jhrEQK) , scan the QR code, and use "Mint:1" as a comment to receive 1000 our mock USDT tokens for your testnet operations.(Simply pay 0.1 ton as a transaction fee when submitting "Mint:1" as a comment.)

    <img width="719" alt="image" src="https://github.com/Ton-Dynasty/ticton-playground/assets/87699256/e5745920-fa23-4b7d-be39-17986a93f4c2">


## 3. Checking the Current TON/USDT Price
    
To find the current market price of TON/USDT, you can visit the official website ([https://ton.tg](https://ton.tg/)) or consult other exchanges. This will provide you with the latest pricing information necessary for informed trading or minting decisions on the testnet.

## 4. Tick
    
If you believe the current market price of TON/USDT to be 2.2, you can execute the following command to tick:
```bash
python main.py
```
The image below depicts the process of quoting a price of 1 TON for 2.2 USDT.
<img width="562" alt="image" src="https://github.com/Ton-Dynasty/ticton-playground/assets/87699256/55595002-c8b5-40e4-ba3d-c9df65198734">


Receiving a message_hash indicates a successful operation. Wait a few seconds, then you can search this message_hash on [tonviewer](https://testnet.tonviewer.com/) to check the transaction.
    
## 5.Getting Alarm Metadata
    
After completing the tick operation, an alarm contract will be deployed by the oracle. This contract allows you to view the alarm's metadata. The following steps use tonviewer for demonstration:

1. View the transaction you just ticked.
2. In the illustration below, **`E`** represents your alarm contract.
    
    ![image](https://github.com/Ton-Dynasty/ticton-playground/assets/36180214/b9b3583c-2f6b-4b54-9120-5ba58a9e684d)

    
3. By calling **`getAlarmMetadata`** on the alarm contract, you can retrieve the alarm index.
    
    ![image](https://github.com/Ton-Dynasty/ticton-playground/assets/36180214/32cfc116-700c-4529-ad3c-cdd73c221807)

        
## 6. Ring
  
        
After calling Tick, you can observe the price of TON. When you believe your quote has deviated from the current price of TON, you can call Ring to close this position to avoid being arbitraged by Timekeeper. 

When calling Ring, if the quote has existed for at least one minute and hasn't been arbitraged by Timekeeper, a reward can be claimed; otherwise, no reward is available.

To complete the Ring process, you can execute the following command to ring:

```bash
python main.py
```
The image below depicts the process of ringing your alarm index you got in the step5.

<img width="561" alt="image" src="https://github.com/Ton-Dynasty/ticton-playground/assets/87699256/bdaf1d9b-8d93-49b5-9233-05a4b491c161">

Receiving a message_hash indicates a successful operation. Wait a few seconds, then you can search this message_hash on [tonviewer](https://testnet.tonviewer.com/) to check the transaction.


Subsequently, you can check the jetton wallet of the TIC token to confirm whether you have received TIC tokens as a reward. 

The address of your TIC wallet is the point **`F`** in the diagram below. You can go to this address, click on Methods, and enter get_wallet_data to view the TIC Balance.
![tic](https://github.com/Ton-Dynasty/ticton-playground/assets/87699256/cc78ed46-48b4-448a-af6a-c18804ea713c)
![bal](https://github.com/Ton-Dynasty/ticton-playground/assets/87699256/7449db16-a1ea-47fc-b89f-8ac5a6f34a76)

    
## 7. Wind (Advanced)
**This quote test event can be completed without Wind to receive an NFT.**

If you find that the quote of an Alarm (which can be seen through the get method: `getAlarmMetadata()` and its `baseAssetPrice`) is no longer accurate, then you can arbitrage this Alarm. For detailed arbitrage mechanisms, refer to this [video](https://www.youtube.com/watch?v=_EwAkiGiw-U) or the [TICTON documentation](https://ton-dynasty.github.io/ticton-doc/).

In simple terms, if you discover Alarm 0 quoting TON at 1 ton = 20u, but you believe 1 ton = 25u, then you can directly spend 20u to buy 1 ton from Alarm 0. For you, this means earning a difference of 5u. Besides arbitraging, you also need to provide a correct quote and offer twice the base asset compared to Alarm 0. Therefore, you need to pay 2 tons and 50u (1 ton = 25u).

For the wind operation, you can refer to `wind.py`

To complete the Wind process, you can execute the following command to wind:
```bash
python main.py
```
The image below depicts the process of arbitraging a alarm where you believe the quoted price is incorrect.

<img width="560" alt="image" src="https://github.com/Ton-Dynasty/ticton-playground/assets/87699256/d523e092-503b-4b2a-808f-5444084ba5e0">


Receiving a message_hash indicates a successful operation. Wait a few seconds, then you can search this message_hash on [tonviewer](https://testnet.tonviewer.com/) to check the transaction.
