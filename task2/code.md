# Python Project: Progressive Electricity Billing

Project Name: Progressive Electricity Billing System

## 1. Problem Statement

Develop a Python program to calculate household electricity bills based on electricity consumption using multiple slabs.

The program should:

- Calculate electricity charges using different consumption slabs.
- Add fixed charges.
- Apply a 5% surcharge.
- Provide a 5% rebate for consumption up to 100 units.
- Compare electricity bills across multiple months.
- Identify unusual bill increases when the bill increases by more than 30% compared with the previous month.

## 2. Algorithm

1. Start the program.
2. Enter the number of months.
3. For each month, enter the month name and electricity units consumed.
4. Calculate energy charges using progressive slabs:
   - First 100 units: ₹1.50 per unit.
   - Next 100 units: ₹2.50 per unit.
   - Above 200 units: ₹4.00 per unit.
5. Add fixed charges of ₹50.
6. Calculate a 5% surcharge.
7. Apply a 5% rebate on energy charges if consumption is 100 units or less.
8. Calculate the final electricity bill.
9. Compare the current month's bill with the previous month's bill.
10. If the increase is greater than 30%, display an unusual increase warning.
11. Display all monthly bills.
12. Stop.

 

## 4. Python Source Code

```

flowchart TD
    A([Start]) --> B[/Enter number of months/]
    B --> C[/Enter month and units/]
    C --> D{Units <= 100?}

    D -->|Yes| E[Energy = Units * 1.50]
    D -->|No| F{Units <= 200?}

    F -->|Yes| G[Energy = 150 + Remaining * 2.50]
    F -->|No| H[Energy = 400 + Remaining * 4.00]

    E --> I[Add fixed charges]
    G --> I
    H --> I

    I --> J[Calculate 5% surcharge]
    J --> K{Units <= 100?}

    K -->|Yes| L[Apply 5% rebate]
    K -->|No| M[No rebate]

    L --> N[Calculate final bill]
    M --> N

    N --> O{Previous month exists?}

    O -->|Yes| P[Compare previous bill]
    O -->|No| Q[Store current bill]

    P --> R{Increase > 30%?}
    R -->|Yes| S[Display unusual increase]
    R -->|No| T[Display normal change]

    S --> Q
    T --> Q

    Q --> U{More months?}
    U -->|Yes| C
    U -->|No| V[/Display all bills/]

    V --> W([Stop])


```

## 5. Sample Input

```
Enter number of months: 3
Month 3

Enter month name: March
Enter electricity units: 260
```

## 6. Sample Output

```
Month 1

Energy Charges: Rs. 120.0
Fixed Charges: Rs. 50
Surcharge: Rs. 8.5
Rebate: Rs. 6.0
Total Bill: Rs. 172.5


Month 2

Energy Charges: Rs. 200.0
Fixed Charges: Rs. 50
Surcharge: Rs. 10.0
Rebate: Rs. 0
Total Bill: Rs. 210.0


Month 3

Energy Charges: Rs. 640.0
Fixed Charges: Rs. 50
Surcharge: Rs. 34.5
Rebate: Rs. 0
Total Bill: Rs. 724.5


----- MONTHLY BILL COMPARISON -----

January : 172.5

February : 210.0
Bill Change: 21.74 %
Normal Bill Change

March : 724.5
Bill Change: 245.0 %
WARNING: Unusual Bill Increase!

Billing Process Completed!
```

## 7. Mermaid Flowchart Code

You can copy this code into [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com) to generate your flowchart.

\#chatgpt-mermaid-\_r_dj\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_dj\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_dj\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_dj\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_dj\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dj\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_dj\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_dj\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_dj\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_dj\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_dj\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_dj\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_dj\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_dj\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_dj\_ p{margin:0;}#chatgpt-mermaid-\_r_dj\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dj\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dj\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dj\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_dj\_ .label text,#chatgpt-mermaid-\_r_dj\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dj\_ .node rect,#chatgpt-mermaid-\_r_dj\_ .node circle,#chatgpt-mermaid-\_r_dj\_ .node ellipse,#chatgpt-mermaid-\_r_dj\_ .node polygon,#chatgpt-mermaid-\_r_dj\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_dj\_ .rough-node .label text,#chatgpt-mermaid-\_r_dj\_ .node .label text,#chatgpt-mermaid-\_r_dj\_ .image-shape .label,#chatgpt-mermaid-\_r_dj\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_dj\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_dj\_ .rough-node .label,#chatgpt-mermaid-\_r_dj\_ .node .label,#chatgpt-mermaid-\_r_dj\_ .image-shape .label,#chatgpt-mermaid-\_r_dj\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_dj\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_dj\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_dj\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_dj\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_dj\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_dj\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_dj\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_dj\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_dj\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_dj\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_dj\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dj\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dj\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_dj\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_dj\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_dj\_ .icon-shape,#chatgpt-mermaid-\_r_dj\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_dj\_ .icon-shape p,#chatgpt-mermaid-\_r_dj\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_dj\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_dj\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_dj\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_dj\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_dj\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_dj\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_dj\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_dj\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_dj\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_dj\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_dj\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_dj\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_dj\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_dj\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_dj\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_dj\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_dj\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_dj\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_dj\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_dj\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_dj\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_dj\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_dj\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_dj\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_dj\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_dj\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_dj\_ .node rect,#chatgpt-mermaid-\_r_dj\_ .node circle,#chatgpt-mermaid-\_r_dj\_ .node ellipse,#chatgpt-mermaid-\_r_dj\_ .node polygon,#chatgpt-mermaid-\_r_dj\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_dj\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_dj\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_dj\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_dj\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_dj\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter number of monthsEnter month and unitsUnits <= 100?Energy = Units \* 1.50Units <= 200?Energy = 150 + Remaining \*2.50Energy = 400 + Remaining \*4.00Add fixed chargesCalculate 5% surchargeUnits <= 100?Apply 5% rebateNo rebateCalculate final billPrevious month exists?Compare previous billStore current billIncrease 30%?Display unusual increaseDisplay normal changeMore months?Display all billsStopYesNoYesNoYesNoYesNoYesNoYesNo

## 8. Expected Result

Electricity Billing Report

Completed

| Month    | Units | Total bill |
| -------- | ----- | ---------- |
| January  | 80    | ₹172.50    |
| February | 120   | ₹210.00    |
| March    | 260   | ₹724.50    |

Unusual increase

March

# 245%

Increase compared with February

Important: These slab rates and charges are assumed for this educational Python project, not actual electricity-board tariff rates.

GitHub upload tip: Save your Python program as `electricity_billing.py` and your flowchart as `flowchart.md`.

You can use this as your Python activity-based learning project.
