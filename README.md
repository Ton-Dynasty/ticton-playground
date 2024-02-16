# ticton-playground
You have the capability to execute the following procedures on the TON blockchain's testnet:

1. **Installing the `ticton` Package**
    
    To begin, ensure your Python environment meets the version requirements: Python >= 3.10 and < 3.12. To install the **`ticton`** package, execute the following command in your terminal:
    
    ```bash
    pip install ticton
    ```
    
2. **Mining Testnet USDT**
    
    Next, we will simulate the quotation process for the TON/USDT token pair on the testnet. Ensure you have sufficient funds for the operation. 
    
    - If your TON balance is low, you can obtain additional TON from the [@testgiver_ton_bot](https://t.me/testgiver_ton_bot) on Telegram.
    - You can visit [tonviewer-USDT](https://testnet.tonviewer.com/EQBqSpvo4S87mX9tjHaG4zhYZeORhVhMapBJpnMZ64jhrEQK) , scan the QR code, and use "Mint:1" as a comment to receive 1000 our mock USDT tokens for your testnet operations.(Simply pay 0.1 ton as a transaction fee when submitting "Mint:1" as a comment.)
        <img src="images/usdt.png" height="231">
        <img src="images/mint.png" width="149">
3. (Optional) Setting the Environment Variables
    
    We requires several environment variables for its operation.You can set the environment variables using the `export` command in your shell. Here are the variables you need to set:
    
    - `TICTON_WALLET_MNEMONICS`: A space-separated list of mnemonics used for wallet authentication and operations.
    - `TICTON_WALLET_VERSION`: Specifies the wallet version. Supported values are "v2r1", "v2r2", "v3r1", "v3r2", "v4r1", "v4r2", "hv2". The default is "v4r2".
    - `TICTON_ORACLE_ADDRESS`: The address of the oracle smart contract on the TON blockchain.
    - `TICTON_TONCENTER_API_KEY`: An API key for accessing TON blockchain data. You can apply for an API key at [@tonapibot](https://t.me/tonapibot).
    - `TICTON_THRESHOLD_PRICE`: A float value that sets a threshold price, with a default of 0.7.
    
    ```bash
    export TICTON_WALLET_MNEMONICS="word1 word2 word3 ... wordN"
    export TICTON_WALLET_VERSION="v4r2"
    export TICTON_ORACLE_ADDRESS="EQBENmfrJP6KwfBBtcHaixDHYCnBcD3QGBJ6NJtY3dwXI0go"
    export TICTON_TONCENTER_API_KEY="your_api_key"
    export TICTON_THRESHOLD_PRICE=0.7
    ```
    
4. Initialization
If you have already set the environment variables by using the `export` command, you can easily initialize the ticton client using the following code:
    
    ```python
    from ticton import TicTonAsyncClient
    
    client = await TicTonAsyncClient.init()
    
    ```
    
    Alternatively, if you prefer not to set global environment variables, you can pass these directly to the initialization function:
    
    ```python
    from ticton import TicTonAsyncClient
    
    client = await TicTonAsyncClient.init(
        mnemonics="word1 word2 word3 ... wordN",
        wallet_version="v4r2",
        oracle_addr="EQBENmfrJP6KwfBBtcHaixDHYCnBcD3QGBJ6NJtY3dwXI0go",
        toncenter_api_key="your_api_key",
        threshold_price=0.7
    )
    
    ```
    
1. **Checking the Current TON/USDT Price**
    
    To find the current market price of TON/USDT, you can visit the official website ([https://ton.tg](https://ton.tg/)) or consult other exchanges. This will provide you with the latest pricing information necessary for informed trading or minting decisions on the testnet.
    
2. **Tick**
    
    If you believe the current market price of TON/USDT to be 2.2, you can execute a tick with the following Python code:
    
    ```python
    result = await client.tick(2.2)
    
    # success message
    Tick Success, tick price: 2.2, spend base asset: 1.23, spend quote asset: 2.2
    ```
    
    Receiving a success message indicates a successful operation. Wait a few seconds, then you can search your wallet address on [tonviewer](https://testnet.tonviewer.com/) to check the transaction.
    
3. **Getting Alarm Metadata**
    
    After completing the tick operation, an alarm contract will be deployed by the oracle. This contract allows you to view the alarm's metadata. The following steps use tonviewer for demonstration:
    
    1. View the transaction you just ticked.
    2. In the illustration below, **`E`** represents your alarm contract.
        
        ![image](https://github.com/Ton-Dynasty/ticton-playground/assets/36180214/b9b3583c-2f6b-4b54-9120-5ba58a9e684d)

        
    3. By calling **`getAlarmMetadata`** on the alarm contract, you can retrieve the alarm index.
        
        ![image](https://github.com/Ton-Dynasty/ticton-playground/assets/36180214/32cfc116-700c-4529-ad3c-cdd73c221807)

        
4. **Ring**
    
    After waiting for more than one minute, you can use the Ring to reclaim your alarm. During this minute, continuously monitor market price changes. If there's a difference from your tick, ring immediately to avoid arbitrage by others. If your tick has been acknowledged by the oracle, you will be rewarded with TIC tokens.
    
    To complete the Ring process, you would typically execute a script similar to the following:
    
    ```python
    alarm_id = 1
    
    result = await client.ring(alarm_id)
    
    # success message
    Ring Success, alarm id: 1
    ```
    
    Receiving a success message indicates a successful operation. Wait a few seconds, then you can search your wallet address on [tonviewer](https://testnet.tonviewer.com/) to check the transaction.
    
    
    Subsequently, you can check the jetton wallet of the TIC token to confirm whether you have received TIC tokens as a reward. 
    
    The address of your TIC wallet is the point F in the diagram below. You can go to this address, click on Methods, and enter get_wallet_data to view the TIC Balance.

    <img src="images/tic.jpg">
    <img src="images/bal.jpg">
    