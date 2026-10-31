# Python Project: Multi-Plan Telecommunications Cost Optimization

Project Name: Mobile Recharge Plan Optimization System

Objective: To develop a Python program that compares multiple mobile recharge plans based on data usage, validity, and budget, calculates extra charges, and identifies the most economical eligible plan.

## 1. Problem Statement

Develop a Python program to evaluate different mobile recharge plans based on the user's requirements.

The program should:

1. Accept the user's monthly data usage.
2. Accept the required validity days and budget.
3. Compare multiple mobile plans.
4. Check whether each plan satisfies the data, validity, and budget requirements.
5. Calculate excess data charges if usage exceeds the plan's data limit.
6. Calculate the total cost of each plan.
7. Identify eligible plans.
8. Select the most economical eligible plan.
9. Display all plan details and the best plan.

## 2. Algorithm

1. Start the program.
2. Enter monthly data usage.
3. Enter required validity days.
4. Enter maximum budget.
5. Define available mobile plans with:
   - Plan name
   - Price
   - Data limit
   - Validity
   - Extra data charge
6. Read each mobile plan.
7. Check data usage and validity.
8. Calculate excess data usage.
9. Calculate excess charges.
10. Calculate total plan cost.
11. Check whether the plan is within budget.
12. Store all eligible plans.
13. Find the plan with the lowest total cost.
14. Display the best eligible plan.
15. If no plan is eligible, display a suitable message.
16. Stop the program.

## 3. Flowchart

[Recharge Plan Comparison  | Devpost](https://images.openai.com/static-rsc-4/2nwqI98gZ0hP6X62tL0lyfOjqe3Bafm0pZUkdbUT_pQY8JVwu1nLCGnzS2scrvvqsouE4i-Xg190bOsUfEAiNxF2afVzEubL5C_X-lGpEi2PHL6A3mQaRDkRApMijlNGGwCmMK2aCQ8f8ZqDFPuTZ7Ahyb0216NwNKLCYvXZzSM?purpose=inline)

[devpost.com](https://devpost.com/software/recharge-plan-comparison?utm_source=chatgpt.com)

## 4. Python Source Code

```

flowchart TD

    A([Start]) --> B[/Enter Data Usage/]
    B --> C[/Enter Required Validity/]
    C --> D[/Enter Budget/]

    D --> E{Valid Inputs?}

    E -->|No| F[Display Invalid Input]
    F --> Z([Stop])

    E -->|Yes| G[Load Available Mobile Plans]

    G --> H[Select a Mobile Plan]

    H --> I[Calculate Excess Data]

    I --> J[Calculate Excess Charges]

    J --> K[Calculate Total Cost]

    K --> L{Data and Validity Sufficient?}

    L -->|No| M[Reject Plan]
    L -->|Yes| N{Within Budget?}

    N -->|No| M
    N -->|Yes| O[Store Eligible Plan]

    M --> P{More Plans?}
    O --> P

    P -->|Yes| H
    P -->|No| Q{Eligible Plans Available?}

    Q -->|No| R[Display No Eligible Plan]

    Q -->|Yes| S[Find Lowest Cost Plan]

    S --> T[Display Best Plan]

    R --> U([Stop])
    T --> U

```

## 5. Sample Input

```
===== MOBILE PLAN OPTIMIZATION SYSTEM =====

Enter monthly data usage (GB): 8
Enter required validity days: 28
Enter your budget (Rs.): 300
```

## 6. Sample Output

```
===== PLAN COMPARISON =====

Plan: Basic Plan
Plan Price: Rs. 149
Data Limit: 2 GB
Validity: 28 days
Excess Data: 6.0 GB
Excess Charge: Rs. 120.0
Total Cost: Rs. 269.0

Plan: Smart Plan
Plan Price: Rs. 249
Data Limit: 10 GB
Validity: 28 days
Excess Data: 0 GB
Excess Charge: Rs. 0
Total Cost: Rs. 249.0

Plan: Premium Plan
Plan Price: Rs. 399
Data Limit: 30 GB
Validity: 56 days
Excess Data: 0 GB
Excess Charge: Rs. 0
Total Cost: Rs. 399.0

Plan: Unlimited Plan
Plan Price: Rs. 599
Data Limit: 50 GB
Validity: 84 days
Excess Data: 0 GB
Excess Charge: Rs. 0
Total Cost: Rs. 599.0

===== BEST PLAN RESULT =====

Best Plan: Smart Plan
Total Cost: Rs. 249
Data Limit: 10 GB
Validity: 28 days

Optimization Completed!
```

## 7. Mermaid Flowchart Code

Copy this code into [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com) to generate the flowchart.

\#chatgpt-mermaid-\_r_io\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_io\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_io\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_io\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_io\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_io\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_io\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_io\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_io\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_io\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_io\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_io\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_io\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_io\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_io\_ p{margin:0;}#chatgpt-mermaid-\_r_io\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_io\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_io\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_io\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_io\_ .label text,#chatgpt-mermaid-\_r_io\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_io\_ .node rect,#chatgpt-mermaid-\_r_io\_ .node circle,#chatgpt-mermaid-\_r_io\_ .node ellipse,#chatgpt-mermaid-\_r_io\_ .node polygon,#chatgpt-mermaid-\_r_io\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_io\_ .rough-node .label text,#chatgpt-mermaid-\_r_io\_ .node .label text,#chatgpt-mermaid-\_r_io\_ .image-shape .label,#chatgpt-mermaid-\_r_io\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_io\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_io\_ .rough-node .label,#chatgpt-mermaid-\_r_io\_ .node .label,#chatgpt-mermaid-\_r_io\_ .image-shape .label,#chatgpt-mermaid-\_r_io\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_io\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_io\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_io\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_io\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_io\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_io\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_io\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_io\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_io\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_io\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_io\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_io\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_io\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_io\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_io\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_io\_ .icon-shape,#chatgpt-mermaid-\_r_io\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_io\_ .icon-shape p,#chatgpt-mermaid-\_r_io\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_io\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_io\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_io\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_io\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_io\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_io\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_io\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_io\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_io\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_io\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_io\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_io\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_io\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_io\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_io\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_io\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_io\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_io\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_io\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_io\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_io\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_io\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_io\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_io\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_io\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_io\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_io\_ .node rect,#chatgpt-mermaid-\_r_io\_ .node circle,#chatgpt-mermaid-\_r_io\_ .node ellipse,#chatgpt-mermaid-\_r_io\_ .node polygon,#chatgpt-mermaid-\_r_io\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_io\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_io\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_io\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_io\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_io\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter Data UsageEnter Required ValidityEnter BudgetValid Inputs?Display Invalid InputStopLoad Available Mobile PlansSelect a Mobile PlanCalculate Excess DataCalculate Excess ChargesCalculate Total CostData and Validity Sufficient?Reject PlanWithin Budget?Store Eligible PlanMore Plans?Eligible Plans Available?Display No Eligible PlanFind Lowest Cost PlanDisplay Best PlanStopNoYesNoYesNoYesYesNoNoYes

## 8. Python Concepts Used

| Concept    | Purpose                |
| ---------- | ---------------------- |
| Variables  | Store user details     |
| List       | Store multiple plans   |
| Dictionary | Store plan information |
| `if-else`  | Check eligibility      |
| `for` loop | Compare all plans      |
| `max()`    | Calculate excess data  |
| `min()`    | Find cheapest plan     |
| Functions  | Organize calculations  |

## 9. GitHub Upload

Save your Python program with this filename:

`mobile_plan_optimization.py`

Save your flowchart with this filename:

`flowchart.md`

Project completion checklist

- Problem statement
- Algorithm
- Flowchart
- Python source code
- Sample input and output
- Mermaid flowchart
- Upload to GitHub

Note: All plan prices, data limits, and excess charges are assumed values for educational purposes. Actual mobile operator plans may differ.
