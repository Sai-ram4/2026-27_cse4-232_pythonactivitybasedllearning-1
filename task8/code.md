# Python Project: Warehouse Inventory Reconciliation

Project Name: Warehouse Stock Management and Reconciliation System

Objective: To develop a Python program that compares opening stock, incoming stock, dispatched stock, and actual closing stock across multiple products. It identifies stock discrepancies and calculates replenishment requirements.

## 1. Problem Statement

Develop a Python program to manage and reconcile warehouse inventory for multiple products.

The program should:

1. Accept the number of products.
2. Enter product name and opening stock.
3. Enter incoming stock quantities.
4. Enter dispatched stock quantities.
5. Enter actual closing stock.
6. Calculate expected closing stock using the stock formula.
7. Compare expected stock with actual closing stock.
8. Identify stock discrepancies.
9. Calculate replenishment requirements based on minimum stock levels.
10. Display a complete inventory reconciliation report.

Stock calculation formula:

\\[ Expected\ Stock = Opening\ Stock + Incoming\ Stock - Dispatched\ Stock \\]

\\[ Discrepancy = Actual\ Stock - Expected\ Stock \\]

\\[ Replenishment = \max(0, Minimum\ Stock - Actual\ Stock) \\]

## 2. Algorithm

1. Start the program.
2. Enter the number of products.
3. Initialize total stock and discrepancy counters.
4. For each product:
   - Enter product name.
   - Enter opening stock.
   - Enter incoming quantity.
   - Enter dispatched quantity.
   - Enter actual closing stock.
   - Enter minimum stock level.
5. Validate all stock quantities.
6. Calculate expected closing stock.
7. Calculate stock discrepancy.
8. Compare expected stock with actual closing stock.
9. If both are equal, display "Stock Matched".
10. Otherwise, display "Stock Discrepancy Detected".
11. Calculate replenishment requirements.
12. Display product-wise inventory details.
13. Display the final warehouse summary.
14. Stop the program.

## 3. Flowchart



## 4. Python Source Code

```

flowchart TD

    A([Start]) --> B[/Enter Number of Products/]

    B --> C{Valid Product Count?}

    C -->|No| D[Display Invalid Input]
    D --> Z([Stop])

    C -->|Yes| E[Initialize Stock Counters]

    E --> F[/Enter Product Details/]

    F --> G[/Enter Opening, Incoming and Dispatched Stock/]

    G --> H[/Enter Actual Closing and Minimum Stock/]

    H --> I{Valid Stock Quantities?}

    I -->|No| J[Display Invalid Stock]
    J --> Z

    I -->|Yes| K{Dispatch <= Available Stock?}

    K -->|No| L[Display Dispatch Error]
    L --> Z

    K -->|Yes| M[Calculate Expected Closing Stock]

    M --> N[Calculate Stock Discrepancy]

    N --> O{Discrepancy = 0?}

    O -->|Yes| P[Display Stock Matched]

    O -->|No| Q[Display Discrepancy Detected]

    P --> R[Calculate Replenishment]

    Q --> R

    R --> S[Update Warehouse Totals]

    S --> T{More Products?}

    T -->|Yes| F

    T -->|No| U[Display Inventory Report]

    U --> V[Display Warehouse Summary]

    V --> Z([Stop])

```

## 5. Sample Input

```
===== WAREHOUSE INVENTORY SYSTEM =====

Enter Number of Products: 3

Product 1
Enter Product Name: Laptop
Enter Opening Stock: 50
Enter Incoming Stock: 20
Enter Dispatched Stock: 30
Enter Actual Closing Stock: 40
Enter Minimum Stock Level: 25

Product 2
Enter Product Name: Mouse
Enter Opening Stock: 100
Enter Incoming Stock: 50
Enter Dispatched Stock: 80
Enter Actual Closing Stock: 65
Enter Minimum Stock Level: 80

Product 3
Enter Product Name: Keyboard
Enter Opening Stock: 60
Enter Incoming Stock: 20
Enter Dispatched Stock: 30
Enter Actual Closing Stock: 50
Enter Minimum Stock Level: 40
```

## 6. Sample Output

```
===== INVENTORY RECONCILIATION REPORT =====

Product Name: Laptop
Opening Stock: 50
Incoming Stock: 20
Dispatched Stock: 30
Expected Closing Stock: 40
Actual Closing Stock: 40
Discrepancy: 0
Replenishment Required: 0
Status: Stock Matched

Product Name: Mouse
Opening Stock: 100
Incoming Stock: 50
Dispatched Stock: 80
Expected Closing Stock: 70
Actual Closing Stock: 65
Discrepancy: -5
Replenishment Required: 15
Status: Discrepancy Detected

Product Name: Keyboard
Opening Stock: 60
Incoming Stock: 20
Dispatched Stock: 30
Expected Closing Stock: 50
Actual Closing Stock: 50
Discrepancy: 0
Replenishment Required: 0
Status: Stock Matched


===== WAREHOUSE SUMMARY =====

Total Opening Stock: 210
Total Incoming Stock: 90
Total Dispatched Stock: 140
Total Actual Closing Stock: 155

Products With Discrepancies: 1

Total Replenishment Required: 15

Inventory Reconciliation Completed!
```

## 7. Mermaid Flowchart Code

Copy this code into [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com) to generate your flowchart.

\#chatgpt-mermaid-\_r_tt\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_tt\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_tt\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_tt\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_tt\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_tt\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_tt\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_tt\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_tt\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_tt\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_tt\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_tt\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_tt\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_tt\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_tt\_ p{margin:0;}#chatgpt-mermaid-\_r_tt\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_tt\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_tt\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_tt\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_tt\_ .label text,#chatgpt-mermaid-\_r_tt\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_tt\_ .node rect,#chatgpt-mermaid-\_r_tt\_ .node circle,#chatgpt-mermaid-\_r_tt\_ .node ellipse,#chatgpt-mermaid-\_r_tt\_ .node polygon,#chatgpt-mermaid-\_r_tt\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_tt\_ .rough-node .label text,#chatgpt-mermaid-\_r_tt\_ .node .label text,#chatgpt-mermaid-\_r_tt\_ .image-shape .label,#chatgpt-mermaid-\_r_tt\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_tt\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_tt\_ .rough-node .label,#chatgpt-mermaid-\_r_tt\_ .node .label,#chatgpt-mermaid-\_r_tt\_ .image-shape .label,#chatgpt-mermaid-\_r_tt\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_tt\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_tt\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_tt\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_tt\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_tt\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_tt\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_tt\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_tt\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_tt\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_tt\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_tt\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_tt\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_tt\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_tt\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_tt\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_tt\_ .icon-shape,#chatgpt-mermaid-\_r_tt\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_tt\_ .icon-shape p,#chatgpt-mermaid-\_r_tt\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_tt\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_tt\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_tt\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_tt\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_tt\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_tt\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_tt\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_tt\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_tt\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_tt\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_tt\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_tt\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_tt\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_tt\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_tt\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_tt\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_tt\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_tt\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_tt\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_tt\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_tt\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_tt\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_tt\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_tt\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_tt\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_tt\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_tt\_ .node rect,#chatgpt-mermaid-\_r_tt\_ .node circle,#chatgpt-mermaid-\_r_tt\_ .node ellipse,#chatgpt-mermaid-\_r_tt\_ .node polygon,#chatgpt-mermaid-\_r_tt\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_tt\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_tt\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_tt\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_tt\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_tt\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter Number of ProductsValid Product Count?Display Invalid InputStopInitialize Stock CountersEnter Product DetailsEnter Opening, Incoming andDispatched StockEnter Actual Closing andMinimum StockValid Stock Quantities?Display Invalid StockDispatch <= Available Stock?Display Dispatch ErrorCalculate Expected ClosingStockCalculate Stock DiscrepancyDiscrepancy = 0?Display Stock MatchedDisplay Discrepancy DetectedCalculate ReplenishmentUpdate Warehouse TotalsMore Products?Display Inventory ReportDisplay Warehouse SummaryNoYesNoYesNoYesYesNoYesNo

## 8. Python Concepts Used

| Concept              | Purpose                       |
| -------------------- | ----------------------------- |
| Variables            | Store stock quantities        |
| Lists                | Store multiple products       |
| `for` loop           | Process multiple products     |
| `if-else`            | Detect stock discrepancies    |
| `max()`              | Calculate replenishment       |
| `sum()`              | Calculate total replenishment |
| Arithmetic operators | Calculate stock balances      |
| `append()`           | Store inventory records       |

## 9. GitHub Upload

Save your files with these names:

- Python file: `warehouse_inventory.py`
- Flowchart file: `flowchart.md`

Project completion checklist

- Problem Statement
- Algorithm
- Flowchart
- Python Source Code
- Sample Input
- Sample Output
- Mermaid Flowchart Code
- GitHub Upload

Important: In this project, a negative discrepancy means actual stock is lower than expected stock, while a positive discrepancy means actual stock is higher than expected stock.
