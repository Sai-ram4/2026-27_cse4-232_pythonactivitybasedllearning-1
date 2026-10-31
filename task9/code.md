# Smart Parking Fee Management – Python Project

## 1. Problem Statement

Develop a Python program to calculate parking fees based on vehicle category, entry time, and exit time.

The system should:

1. Accept vehicle categories: Bike, Car, and Bus.
2. Accept parking entry and exit times in `HH:MM` format.
3. Validate the entered time values.
4. Calculate parking duration, including overnight parking.
5. Apply different hourly rates for each vehicle category.
6. Apply a daily maximum parking limit.
7. Calculate additional penalties for invalid parking duration or other penalty conditions.
8. Display the final parking bill.

## 2. Algorithm

1. Start the program.
2. Define hourly parking rates for Bike, Car, and Bus.
3. Define the daily maximum parking fee.
4. Get the vehicle category from the user.
5. Validate the vehicle category.
6. Get entry time and exit time.
7. Validate the time format.
8. Calculate the parking duration.
9. If exit time is earlier than entry time, consider overnight parking.
10. Calculate the hourly parking fee.
11. Apply the daily maximum limit.
12. Add the penalty if the parking duration exceeds 24 hours.
13. Calculate the total parking fee.
14. Display the parking details and final amount.
15. Stop the program.

## 3. Flowchart


## 4. Python Source Code

```

flowchart TD
    A([Start]) --> B[Display Parking System]
    B --> C[Enter Vehicle Category]
    C --> D{Valid Vehicle?}
    D -- No --> E[Display Error]
    E --> Z([End])

    D -- Yes --> F[Enter Entry and Exit Times]
    F --> G{Valid Time Format?}

    G -- No --> H[Display Invalid Time]
    H --> Z

    G -- Yes --> I[Calculate Time Difference]
    I --> J{Exit Earlier or Equal?}

    J -- Yes --> K[Calculate Overnight Duration]
    J -- No --> L[Calculate Normal Duration]

    K --> M[Round Hours Up]
    L --> M

    M --> N[Calculate Parking Fee]
    N --> O[Apply Daily Maximum Limit]
    O --> P{Duration Above 24 Hours?}

    P -- Yes --> Q[Add Penalty]
    P -- No --> R[No Penalty]

    Q --> S[Calculate Final Fee]
    R --> S

    S --> T[Display Parking Bill]
    T --> Z([End])

```

Note: This beginner-level version assumes parking lasts no more than one overnight cycle (24 hours). It rounds partial hours up to the next full hour. The extra ₹50 penalty applies when parking exceeds 24 hours.

## 5. Sample Input

```
===== SMART PARKING FEE MANAGEMENT =====
Enter vehicle type (Bike/Car/Bus): car
Enter entry time (HH:MM): 22:00
Enter exit time (HH:MM): 02:30
```

## 6. Sample Output

```
===== PARKING BILL =====
Vehicle Type: Car
Entry Time: 22:00
Exit Time: 02:30
Parking Duration: 5 hours
Hourly Rate: Rs. 20
Parking Fee: Rs. 100
Penalty: Rs. 0
Total Amount: Rs. 100
```

Explanation:

- Vehicle: Car
- Parking duration: 4 hours 30 minutes
- Rounded duration: 5 hours
- Hourly charge: ₹20
- Total: 5 × 20 = ₹100

## 7. Mermaid Flowchart Code

Paste this code into [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com) to view your flowchart.

\#chatgpt-mermaid-\_r_10q\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_10q\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_10q\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_10q\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_10q\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_10q\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_10q\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_10q\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_10q\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_10q\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_10q\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_10q\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_10q\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_10q\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_10q\_ p{margin:0;}#chatgpt-mermaid-\_r_10q\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_10q\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_10q\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_10q\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_10q\_ .label text,#chatgpt-mermaid-\_r_10q\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_10q\_ .node rect,#chatgpt-mermaid-\_r_10q\_ .node circle,#chatgpt-mermaid-\_r_10q\_ .node ellipse,#chatgpt-mermaid-\_r_10q\_ .node polygon,#chatgpt-mermaid-\_r_10q\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_10q\_ .rough-node .label text,#chatgpt-mermaid-\_r_10q\_ .node .label text,#chatgpt-mermaid-\_r_10q\_ .image-shape .label,#chatgpt-mermaid-\_r_10q\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_10q\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_10q\_ .rough-node .label,#chatgpt-mermaid-\_r_10q\_ .node .label,#chatgpt-mermaid-\_r_10q\_ .image-shape .label,#chatgpt-mermaid-\_r_10q\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_10q\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_10q\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_10q\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_10q\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_10q\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_10q\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_10q\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_10q\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_10q\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_10q\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_10q\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_10q\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_10q\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_10q\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_10q\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_10q\_ .icon-shape,#chatgpt-mermaid-\_r_10q\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_10q\_ .icon-shape p,#chatgpt-mermaid-\_r_10q\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_10q\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_10q\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_10q\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_10q\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_10q\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_10q\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_10q\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_10q\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_10q\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_10q\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_10q\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_10q\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_10q\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_10q\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_10q\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_10q\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_10q\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_10q\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_10q\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_10q\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_10q\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_10q\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_10q\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_10q\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_10q\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_10q\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_10q\_ .node rect,#chatgpt-mermaid-\_r_10q\_ .node circle,#chatgpt-mermaid-\_r_10q\_ .node ellipse,#chatgpt-mermaid-\_r_10q\_ .node polygon,#chatgpt-mermaid-\_r_10q\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_10q\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_10q\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_10q\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_10q\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_10q\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartDisplay Parking SystemEnter Vehicle CategoryValid Vehicle?Display ErrorEndEnter Entry and Exit TimesValid Time Format?Display Invalid TimeCalculate Time DifferenceExit Earlier or Equal?Calculate Overnight DurationCalculate Normal DurationRound Hours UpCalculate Parking FeeApply Daily Maximum LimitDuration Above 24 Hours?Add PenaltyNo PenaltyCalculate Final FeeDisplay Parking BillNoYesNoYesYesNoYesNo

## 8. Python Concepts Used

| Concept    | Purpose                 |
| ---------- | ----------------------- |
| Dictionary | Store vehicle rates     |
| Input      | Get user details        |
| If-else    | Check conditions        |
| Try-except | Handle invalid input    |
| Datetime   | Validate time           |
| While loop | Calculate daily charges |
| Arithmetic | Calculate parking fees  |

GitHub upload file names:

- `smart_parking.py`
- `flowchart.md`
- `README.md`

You can use this as your Smart Parking Fee Management Python activity project.
