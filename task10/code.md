# Laboratory Chemical Inventory Validation – Python Project

## 1. Problem Statement

Develop a Python program to analyse hypothetical laboratory inventory records and identify invalid storage combinations.

The system should:

1. Accept the number of inventory records.
2. Collect item name, storage category, compatibility group, and quantity.
3. Validate the entered storage category and quantity.
4. Check whether the total quantity exceeds the maximum allowed limit for each storage category.
5. Check compatibility restrictions between items stored in the same category.
6. Identify and display invalid inventory records.
7. Display a final validation summary.

Note: This project uses fictional categories and compatibility rules for programming practice only. Real laboratory storage decisions must follow institution-approved safety rules.

## 2. Algorithm

1. Start the program.
2. Define maximum quantity limits for storage categories A, B, and C.
3. Define the allowed compatibility groups X, Y, and Z.
4. Define the hypothetical incompatible pair X and Y.
5. Get the number of inventory records.
6. Accept item name, storage category, compatibility group, and quantity.
7. Validate each record.
8. Calculate the total quantity in each storage category.
9. Compare the total with the maximum allowed limit.
10. Check compatibility groups within each storage category.
11. Identify invalid combinations.
12. Display validation results and error messages.
13. Display the total number of valid and invalid records.
14. Stop the program.

## 3. Flowchart



## 4. Python Source Code

`
flowchart TD
    A([Start]) --> B[Define Storage Limits]
    B --> C[Define Compatibility Rules]
    C --> D[Enter Number of Records]
    D --> E[Collect Inventory Details]
    E --> F{Valid Input?}

    F -- No --> G[Display Input Error]
    G --> Z([End])

    F -- Yes --> H[Validate Categories and Groups]
    H --> I[Calculate Category Quantities]
    I --> J{Maximum Limit Exceeded?}

    J -- Yes --> K[Flag Quantity Violation]
    J -- No --> L[Continue Validation]

    K --> M[Check Compatibility]
    L --> M

    M --> N{Incompatible Pair Found?}
    N -- Yes --> O[Flag Compatibility Violation]
    N -- No --> P[Prepare Validation Report]

    O --> P
    P --> Q[Display Valid and Invalid Records]
    Q --> R[Display Total Issues]
    R --> Z([End])
``
```

## 5. Sample Input

The following uses fictional records and rules.

```
===== LABORATORY INVENTORY VALIDATION =====
Enter number of inventory records: 3

Record 1
Enter item name: Sample-1
Enter storage category (A/B/C): A
Enter compatibility group (X/Y/Z): X
Enter quantity: 40

Record 2
Enter item name: Sample-2
Enter storage category (A/B/C): A
Enter compatibility group (X/Y/Z): Y
Enter quantity: 30

Record 3
Enter item name: Sample-3
Enter storage category (A/B/C): B
Enter compatibility group (X/Y/Z): Z
Enter quantity: 90
```

## 6. Sample Output

```
===== INVENTORY VALIDATION REPORT =====

Category A: 70.0 / 100 units
Category B: 90.0 / 80 units

INVALID RECORDS / COMBINATIONS:

- Category B: Quantity limit exceeded (90.0 > 80)
- Compatibility violation: Sample-1 and Sample-2 in Category A

Status: VALIDATION FAILED

Total Records: 3
Total Issues: 2
```

Explanation:

- Sample-1 and Sample-2 belong to the same storage category, and their fictional groups X and Y are incompatible.
- Category B contains 90 units, but its maximum limit is 80 units.
- Therefore, the program identifies two validation issues.

## 7. Mermaid Flowchart Code

Paste this code into [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com) to view the flowchart.

\#chatgpt-mermaid-\_r_138\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_138\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_138\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_138\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_138\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_138\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_138\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_138\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_138\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_138\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_138\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_138\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_138\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_138\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_138\_ p{margin:0;}#chatgpt-mermaid-\_r_138\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_138\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_138\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_138\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_138\_ .label text,#chatgpt-mermaid-\_r_138\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_138\_ .node rect,#chatgpt-mermaid-\_r_138\_ .node circle,#chatgpt-mermaid-\_r_138\_ .node ellipse,#chatgpt-mermaid-\_r_138\_ .node polygon,#chatgpt-mermaid-\_r_138\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_138\_ .rough-node .label text,#chatgpt-mermaid-\_r_138\_ .node .label text,#chatgpt-mermaid-\_r_138\_ .image-shape .label,#chatgpt-mermaid-\_r_138\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_138\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_138\_ .rough-node .label,#chatgpt-mermaid-\_r_138\_ .node .label,#chatgpt-mermaid-\_r_138\_ .image-shape .label,#chatgpt-mermaid-\_r_138\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_138\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_138\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_138\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_138\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_138\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_138\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_138\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_138\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_138\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_138\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_138\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_138\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_138\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_138\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_138\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_138\_ .icon-shape,#chatgpt-mermaid-\_r_138\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_138\_ .icon-shape p,#chatgpt-mermaid-\_r_138\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_138\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_138\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_138\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_138\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_138\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_138\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_138\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_138\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_138\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_138\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_138\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_138\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_138\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_138\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_138\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_138\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_138\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_138\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_138\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_138\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_138\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_138\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_138\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_138\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_138\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_138\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_138\_ .node rect,#chatgpt-mermaid-\_r_138\_ .node circle,#chatgpt-mermaid-\_r_138\_ .node ellipse,#chatgpt-mermaid-\_r_138\_ .node polygon,#chatgpt-mermaid-\_r_138\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_138\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_138\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_138\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_138\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_138\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartDefine Storage LimitsDefine Compatibility RulesEnter Number of RecordsCollect Inventory DetailsValid Input?Display Input ErrorEndValidate Categories and GroupsCalculate Category QuantitiesMaximum Limit Exceeded?Flag Quantity ViolationContinue ValidationCheck CompatibilityIncompatible Pair Found?Flag Compatibility ViolationPrepare Validation ReportDisplay Valid and InvalidRecordsDisplay Total IssuesNoYesYesNoYesNo

## 8. Python Concepts Used

| Concept           | Purpose                         |
| ----------------- | ------------------------------- |
| Dictionary        | Store inventory records         |
| List              | Store multiple records          |
| For loop          | Process inventory               |
| Nested loop       | Compare record pairs            |
| If-else           | Validate conditions             |
| Functions         | Built-in input and calculations |
| Try-except        | Handle invalid input            |
| String formatting | Display report                  |

## 9. GitHub Upload Files

Save these files in your project folder:

- `chemical_inventory.py`
- `flowchart.md`
- `README.md`

Project learning outcome: You will practise Python dictionaries, lists, loops, conditions, input validation, and inventory report generation.
