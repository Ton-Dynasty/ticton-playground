# TICTON Playground
This repository is primarily for the **TICTON quote testing event tutorial**. Everyone can refer to this document or this [tutorial video](https://www.youtube.com/watch?v=5USR937Vt5k) to complete the quote and claim rewards. Those who successfully follow the tutorial can obtain a TICTON-exclusive NFT. In the future, holders of these NFTs will have priority in participating in airdrops and other events.

If you have any questions, feel free to join our [community](https://t.me/TictonOfficial) and discuss with us.

**The following steps will be conducted on TON's testnet!**

## Table of Contents
  - [1. How to Install](#1-how-to-install)
    - [Windows](#windows)
    - [MacOS/Linux](#macoslinux)
  - [2. Mining Testnet USDT](#2-mining-testnet-usdt)
  - [3. Checking the Current TON/USDT Price](#3-checking-the-current-tonusdt-price)
  - [4. Tick](#4-tick)
    - [Windows](#windows-1)
    - [MacOS/Linux](#macoslinux-1)
  - [5. Ring](#5-ring)
  - [6. Wind (Advanced)](#6-wind-advanced)
   
## 1. How to Install
    
First, ensure your Python environment meets the version requirements: `Python version >= 3.10 and < 3.12`. The first step is to git clone this repo, then to install the ticton package, please execute the following command in your terminal:

### Windows

```bash    
git clone https://github.com/Ton-Dynasty/ticton-playground.git
cd ticton-playground
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

### MacOS/Linux

```bash
git clone https://github.com/Ton-Dynasty/ticton-playground.git
cd ticton-playground
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env.example .env
```
> [!IMPORTANT]
> Please ensure that you have filled out the `.env` file before proceeding with the following steps.

TONCENTER_API_KEY can apply at [@tonapibot](https://t.me/tonapibot).

## 📖 Tutorial: Generate a new wallet (Optional)📖 

1. First, run the following command to create a new wallet:

    ```bash
    python3 main.py
    ```

2. Then, type `0` to create a new wallet.
  
    ![mmm](https://github.com/Ton-Dynasty/ticton-playground/assets/87699256/1b4a0e8e-33e5-434a-bcf3-8f00ed03751c)


3. After creation, you will get wallet mnemonic and address. Please save them in a safe place.

4. Import your wallet to your wallet software, such as [TonKeeper Browser Extension](https://chromewebstore.google.com/detail/tonkeeper-%E2%80%94-wallet-for-to/omaabbefbmiijedngplfjmnooppbclkk), [TonKeeper](https://tonkeeper.com/). Click the "Import Wallet" button and paste your mnemonic.
   
5. Go to settings page in your wallet software, click the TON icon 5 times to switch to testnet.

6. Copy your address and go to [Test Giver](https://t.me/testgiver_ton_bot) to get some TON for your new wallet.


## 2. Mining Testnet USDT
    
Next, we will simulate the quotation process for the TON/USDT token pair on the testnet. Ensure you have sufficient funds for the operation. 

- If your TON balance is low, you can obtain additional TON from the [@testgiver_ton_bot](https://t.me/testgiver_ton_bot) on Telegram.
- You can visit [tonviewer-USDT](https://testnet.tonviewer.com/EQBqSpvo4S87mX9tjHaG4zhYZeORhVhMapBJpnMZ64jhrEQK) , scan the QR code, and use "Mint:1" as a comment to receive 1000 our mock USDT tokens for your testnet operations.(Simply pay 0.1 ton as a transaction fee when submitting "Mint:1" as a comment.)

    <img width="719" alt="image" src="https://github.com/Ton-Dynasty/ticton-playground/assets/87699256/e5745920-fa23-4b7d-be39-17986a93f4c2">


## 3. Checking the Current TON/USDT Price
    
To find the current market price of TON/USDT, you can visit the official website ([https://ton.tg](https://ton.tg/)) or consult other exchanges. This will provide you with the latest pricing information necessary for informed trading or minting decisions on the testnet.

## 4. Tick
    
If you believe the current market price of `TON/USDT` to be `2.2`, you can execute the following command to tick:

### Windows
```bash
python main.py
```

### MacOS/Linux
```bash
python3 main.py
```

The image below depicts the process of quoting a price of 1 TON for 2.2 USDT.
![alarm](https://github.com/Ton-Dynasty/ticton-playground/assets/87699256/f6b9ccfb-59fd-41a2-97a0-b2496750e417)



(You can open the tx link to view this transaction. Additionally, please remember your alarm ID, as it will be used in the next steps on Ring.)

        
## 5. Ring
  
        
After calling Tick, you can observe the price of TON. When you believe your quote has deviated from the current price of TON, you can call Ring to close this position to avoid being arbitraged by Timekeeper. 

When calling Ring, if the quote has existed for at least one minute and hasn't been arbitraged by Timekeeper, a reward can be claimed; otherwise, no reward is available.

To complete the Ring process, you can execute the following command to ring:

```bash
python main.py
```
The image below depicts the process of ringing your alarm index you got in the step5.

<img width="750" alt="image" src="https://github.com/Ton-Dynasty/ticton-playground/assets/87699256/cab16cdf-d72d-495a-9e94-12e9de521d1d">


(You can open the tx link to view this transaction.)


Subsequently, you can check the jetton wallet of the TIC token to confirm whether you have received TIC tokens as a reward. 

The address of your TIC wallet is the point **`F`** in the diagram below. You can go to this address, click on Methods, and enter get_wallet_data to view the TIC Balance.
![tic](https://github.com/Ton-Dynasty/ticton-playground/assets/87699256/cc78ed46-48b4-448a-af6a-c18804ea713c)
![bal](https://github.com/Ton-Dynasty/ticton-playground/assets/87699256/7449db16-a1ea-47fc-b89f-8ac5a6f34a76)

    
## 6. Wind (Advanced)
**This quote test event can be completed without Wind to receive an NFT.**

If you find that the quote of an Alarm (which can be seen through the get method: `getAlarmMetadata()` and its `baseAssetPrice`) is no longer accurate, then you can arbitrage this Alarm. For detailed arbitrage mechanisms, refer to this [video](https://www.youtube.com/watch?v=_EwAkiGiw-U) or the [TICTON documentation](https://ton-dynasty.github.io/ticton-doc/).

In simple terms, if you discover Alarm 0 quoting TON at 1 ton = 20u, but you believe 1 ton = 25u, then you can directly spend 20u to buy 1 ton from Alarm 0. For you, this means earning a difference of 5u. Besides arbitraging, you also need to provide a correct quote and offer twice the base asset compared to Alarm 0. Therefore, you need to pay 2 tons and 50u (1 ton = 25u).

For the wind operation, you can refer to `wind.py`

To complete the Wind process, you can execute the following command to wind:
```bash
python main.py
```
The image below depicts the process of arbitraging a alarm where you believe the quoted price is incorrect.



<img width="751" alt="image" src="https://github.com/Ton-Dynasty/ticton-playground/assets/87699256/eb1556e7-84f9-4d9c-a506-4c6cf954b8dd">

Alarm 68 quoted 4U for one ton, but I believe this price overvalues the ton. Therefore, I initiated a Wind with Alarm 68, selling one ton to quoter for 4U and providing a new quote of 1 ton = 2.3U.

(You can open the tx link to view this transaction.)
