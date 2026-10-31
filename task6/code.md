# Python Project: ATM Transaction Sequence Simulation

Project Name: ATM Transaction Management System

Objective: To develop a Python program that simulates ATM transactions, processes deposits and withdrawals, maintains account balance, enforces withdrawal limits, rejects invalid transactions, and generates a transaction summary.

## 1. Problem Statement

Develop a Python program to simulate ATM transactions using a sequence of deposits and withdrawals.

The program should:

1. Accept the initial account balance.
2. Accept the number of transactions.
3. Process deposits and withdrawals.
4. Update the account balance after every valid transaction.
5. Enforce a maximum withdrawal limit of ₹10,000 per transaction.
6. Reject withdrawals exceeding the available balance.
7. Reject negative or zero transaction amounts.
8. Maintain a record of successful and rejected transactions.
9. Display the final account balance.
10. Generate a transaction summary showing total deposits, withdrawals, and rejected transactions.

## 2. Algorithm

1. Start the program.
2. Enter the initial account balance.
3. Enter the number of transactions.
4. Initialize deposit, withdrawal, and rejected transaction counters.
5. Read the transaction type.
6. Enter the transaction amount.
7. Validate the transaction amount.
8. If the transaction is a deposit:
   - Add the amount to the account balance.
   - Update the total deposits.
9. If the transaction is a withdrawal:
   - Check the withdrawal limit.
   - Check the available balance.
   - If valid, subtract the amount from the balance.
   - Otherwise, reject the transaction.
10. Repeat until all transactions are completed.
11. Display the final balance.
12. Display the transaction summary.
13. Stop.

## 3. Flowchart


## 4. Python Source Code

```

flowchart TD

    A([Start]) --> B[/Enter Initial Balance/]

    B --> C{Valid Balance?}

    C -->|No| D[Display Invalid Balance]
    D --> Z([Stop])

    C -->|Yes| E[/Enter Number of Transactions/]

    E --> F[Initialize Counters]

    F --> G[/Enter Transaction Type and Amount/]

    G --> H{Valid Amount?}

    H -->|No| I[Reject Transaction]
    H -->|Yes| J{Transaction Type?}

    J -->|Deposit| K[Add Amount to Balance]

    J -->|Withdraw| L{Amount <= Withdrawal Limit?}

    L -->|No| I

    L -->|Yes| M{Sufficient Balance?}

    M -->|No| I

    M -->|Yes| N[Subtract Amount from Balance]

    J -->|Invalid| I

    K --> O[Update Transaction Summary]
    N --> O
    I --> O

    O --> P{More Transactions?}

    P -->|Yes| G

    P -->|No| Q[Display Transaction History]

    Q --> R[Display Final Balance and Summary]

    R --> Z([Stop])

```

## 5. Sample Input

```
===== ATM TRANSACTION SYSTEM =====

Enter Initial Balance: Rs. 15000

Enter Number of Transactions: 5

Transaction 1
Enter Transaction Type (deposit/withdraw): deposit
Enter Amount: Rs. 5000

Transaction 2
Enter Transaction Type (deposit/withdraw): withdraw
Enter Amount: Rs. 3000

Transaction 3
Enter Transaction Type (deposit/withdraw): withdraw
Enter Amount: Rs. 12000

Transaction 4
Enter Transaction Type (deposit/withdraw): withdraw
Enter Amount: Rs. 20000

Transaction 5
Enter Transaction Type (deposit/withdraw): deposit
Enter Amount: Rs. 2000
```

## 6. Sample Output

```
===== ATM TRANSACTION SYSTEM =====

Transaction 1
Deposit Successful!
Current Balance: Rs. 20000.0

Transaction 2
Withdrawal Successful!
Current Balance: Rs. 17000.0

Transaction 3
Withdrawal Rejected: Withdrawal Limit Exceeded!

Transaction 4
Withdrawal Rejected: Withdrawal Limit Exceeded!

Transaction 5
Deposit Successful!
Current Balance: Rs. 19000.0


===== TRANSACTION HISTORY =====

1 Deposit Rs. 5000.0 - Successful
2 Withdraw Rs. 3000.0 - Successful
3 Withdraw Rs. 12000.0 - Rejected
4 Withdraw Rs. 20000.0 - Rejected
5 Deposit Rs. 2000.0 - Successful


===== ATM TRANSACTION SUMMARY =====

Total Deposits: Rs. 7000.0
Total Withdrawals: Rs. 3000.0
Rejected Transactions: 2
Final Account Balance: Rs. 19000.0

ATM Transaction Process Completed!
```

## 7. Mermaid Flowchart Code

Copy this code into [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com) to generate your flowchart.

\#chatgpt-mermaid-\_r_o6\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_o6\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_o6\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_o6\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_o6\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_o6\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_o6\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_o6\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_o6\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_o6\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_o6\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_o6\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_o6\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_o6\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_o6\_ p{margin:0;}#chatgpt-mermaid-\_r_o6\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_o6\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_o6\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_o6\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_o6\_ .label text,#chatgpt-mermaid-\_r_o6\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_o6\_ .node rect,#chatgpt-mermaid-\_r_o6\_ .node circle,#chatgpt-mermaid-\_r_o6\_ .node ellipse,#chatgpt-mermaid-\_r_o6\_ .node polygon,#chatgpt-mermaid-\_r_o6\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_o6\_ .rough-node .label text,#chatgpt-mermaid-\_r_o6\_ .node .label text,#chatgpt-mermaid-\_r_o6\_ .image-shape .label,#chatgpt-mermaid-\_r_o6\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_o6\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_o6\_ .rough-node .label,#chatgpt-mermaid-\_r_o6\_ .node .label,#chatgpt-mermaid-\_r_o6\_ .image-shape .label,#chatgpt-mermaid-\_r_o6\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_o6\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_o6\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_o6\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_o6\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_o6\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_o6\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_o6\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_o6\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_o6\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_o6\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_o6\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_o6\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_o6\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_o6\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_o6\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_o6\_ .icon-shape,#chatgpt-mermaid-\_r_o6\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_o6\_ .icon-shape p,#chatgpt-mermaid-\_r_o6\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_o6\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_o6\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_o6\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_o6\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_o6\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_o6\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_o6\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_o6\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_o6\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_o6\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_o6\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_o6\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_o6\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_o6\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_o6\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_o6\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_o6\_ .node rect,#chatgpt-mermaid-\_r_o6\_ .node circle,#chatgpt-mermaid-\_r_o6\_ .node ellipse,#chatgpt-mermaid-\_r_o6\_ .node polygon,#chatgpt-mermaid-\_r_o6\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_o6\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_o6\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_o6\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_o6\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_o6\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter Initial BalanceValid Balance?Display Invalid BalanceStopEnter Number of TransactionsInitialize CountersEnter Transaction Type andAmountValid Amount?Reject TransactionTransaction Type?Add Amount to BalanceAmount <= Withdrawal Limit?Sufficient Balance?Subtract Amount from BalanceUpdate Transaction SummaryMore Transactions?Display Transaction HistoryDisplay Final Balance andSummaryNoYesNoYesDepositWithdrawNoYesNoYesInvalidYesNo

## 8. Python Concepts Used

| Concept              | Purpose                        |
| -------------------- | ------------------------------ |
| Variables            | Store account balance          |
| `input()`            | Accept transactions            |
| `if-elif-else`       | Validate transactions          |
| `for` loop           | Process multiple transactions  |
| Lists                | Store transaction history      |
| Arithmetic operators | Update balance                 |
| Counters             | Track deposits and withdrawals |
| `enumerate()`        | Display transaction numbers    |

## 9. GitHub Upload

Save your files using these names:

- Python file: `atm_transaction.py`
- Flowchart file: `flowchart.md`

Project completion checklist

- Problem Statement
- Algorithm
- Flowchart
- Python Source Code
- Sample Input
- Sample Output
- Mermaid Flowchart
- GitHub Upload

Note: This is an educational ATM simulation. The withdrawal limit of ₹10,000 is an assumed project rule, not a real bank limit.
