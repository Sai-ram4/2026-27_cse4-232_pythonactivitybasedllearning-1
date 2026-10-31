# Python Project: Attendance Recovery Computation

Project Name: Student Attendance Eligibility and Recovery Calculator

Objective: To develop a Python program that calculates student attendance percentages and determines the minimum number of consecutive classes required to reach the eligibility threshold under different future attendance scenarios.

## 1. Problem Statement

Develop a Python program to calculate current student attendance and determine how many additional classes a student must attend to reach the required attendance percentage.

The program should:

1. Accept the total number of classes conducted.
2. Accept the number of classes attended.
3. Calculate the current attendance percentage.
4. Set the minimum eligibility threshold (example: 75%).
5. Calculate the minimum consecutive classes required to reach 75% attendance.
6. Consider different future attendance scenarios:
   - Attend all upcoming classes.
   - Attend 90% of upcoming classes.
   - Attend 80% of upcoming classes.
7. Display the required number of additional classes.
8. Display whether the student is currently eligible.
9. Display the final attendance percentage for each scenario.

## 2. Algorithm

1. Start the program.
2. Enter the total number of classes conducted.
3. Enter the number of classes attended.
4. Enter the attendance eligibility percentage.
5. Validate the entered values.
6. Calculate current attendance percentage.
7. Check whether the student is eligible.
8. If attendance is below the threshold:
   - Calculate the minimum consecutive classes needed.
   - Calculate future attendance under different scenarios.
9. Display the current attendance percentage.
10. Display the required additional classes.
11. Display future attendance percentages.
12. Stop the program.

## 3. Flowchart


## 4. Python Source Code

```

flowchart TD

    A([Start]) --> B[/Enter Total Classes/]

    B --> C[/Enter Attended Classes/]

    C --> D[/Enter Eligibility Percentage/]

    D --> E{Valid Inputs?}

    E -->|No| F[Display Invalid Input]

    F --> Z([Stop])

    E -->|Yes| G[Calculate Current Attendance]

    G --> H{Attendance >= Threshold?}

    H -->|Yes| I[Display Eligible Status]

    I --> Z

    H -->|No| J[Initialize Required Classes = 0]

    J --> K[Add One Future Class]

    K --> L[Calculate New Attendance]

    L --> M{Attendance >= Threshold?}

    M -->|No| K

    M -->|Yes| N[Display Minimum Classes Required]

    N --> O[Calculate 100% Scenario]

    O --> P[Calculate 90% Scenario]

    P --> Q[Calculate 80% Scenario]

    Q --> R[Display Future Attendance Results]

    R --> S[Display Final Report]

    S --> Z([Stop])

```

## 5. Sample Input

```
===== ATTENDANCE RECOVERY CALCULATOR =====

Enter Total Classes Conducted: 100

Enter Classes Attended: 60

Enter Eligibility Percentage: 75
```

## 6. Sample Output

```
===== CURRENT ATTENDANCE =====

Total Classes: 100
Classes Attended: 60

Current Attendance: 60.0 %

Eligibility Threshold: 75.0 %

Status: NOT ELIGIBLE

Minimum Consecutive Classes Required: 60

===== FUTURE ATTENDANCE SCENARIOS =====

Scenario: 100% Attendance

Future Classes: 60
Future Classes Attended: 60
Final Attendance: 75.0 %
Status: ELIGIBLE

Scenario: 90% Attendance

Future Classes: 60
Future Classes Attended: 54
Final Attendance: 71.25 %
Status: NOT ELIGIBLE

Scenario: 80% Attendance

Future Classes: 60
Future Classes Attended: 48
Final Attendance: 67.5 %
Status: NOT ELIGIBLE

Attendance Calculation Completed!
```

Understanding the calculation:

Current attendance is 60 out of 100 classes.

To reach 75%, the student must attend 60 additional consecutive classes:

\\[ \frac{60+60}{100+60}\times100=75\\% \\]

The 90% and 80% scenarios use the same 60 future classes, with some classes missed.

## 7. Mermaid Flowchart Code

Copy this code into [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com) to generate your flowchart.

\#chatgpt-mermaid-\_r_r0\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_r0\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_r0\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_r0\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_r0\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_r0\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_r0\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_r0\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_r0\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_r0\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_r0\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_r0\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_r0\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_r0\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_r0\_ p{margin:0;}#chatgpt-mermaid-\_r_r0\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_r0\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_r0\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_r0\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_r0\_ .label text,#chatgpt-mermaid-\_r_r0\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_r0\_ .node rect,#chatgpt-mermaid-\_r_r0\_ .node circle,#chatgpt-mermaid-\_r_r0\_ .node ellipse,#chatgpt-mermaid-\_r_r0\_ .node polygon,#chatgpt-mermaid-\_r_r0\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_r0\_ .rough-node .label text,#chatgpt-mermaid-\_r_r0\_ .node .label text,#chatgpt-mermaid-\_r_r0\_ .image-shape .label,#chatgpt-mermaid-\_r_r0\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_r0\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_r0\_ .rough-node .label,#chatgpt-mermaid-\_r_r0\_ .node .label,#chatgpt-mermaid-\_r_r0\_ .image-shape .label,#chatgpt-mermaid-\_r_r0\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_r0\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_r0\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_r0\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_r0\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_r0\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_r0\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_r0\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_r0\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_r0\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_r0\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_r0\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_r0\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_r0\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_r0\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_r0\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_r0\_ .icon-shape,#chatgpt-mermaid-\_r_r0\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_r0\_ .icon-shape p,#chatgpt-mermaid-\_r_r0\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_r0\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_r0\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_r0\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_r0\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_r0\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_r0\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_r0\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_r0\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_r0\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_r0\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_r0\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_r0\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_r0\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_r0\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_r0\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_r0\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_r0\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_r0\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_r0\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_r0\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_r0\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_r0\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_r0\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_r0\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_r0\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_r0\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_r0\_ .node rect,#chatgpt-mermaid-\_r_r0\_ .node circle,#chatgpt-mermaid-\_r_r0\_ .node ellipse,#chatgpt-mermaid-\_r_r0\_ .node polygon,#chatgpt-mermaid-\_r_r0\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_r0\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_r0\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_r0\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_r0\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_r0\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter Total ClassesEnter Attended ClassesEnter Eligibility PercentageValid Inputs?Display Invalid InputStopCalculate Current AttendanceAttendance = Threshold?Display Eligible StatusInitialize Required Classes = 0Add One Future ClassCalculate New AttendanceAttendance = Threshold?Display Minimum ClassesRequiredCalculate 100% ScenarioCalculate 90% ScenarioCalculate 80% ScenarioDisplay Future AttendanceResultsDisplay Final ReportNoYesYesNoNoYes

## 8. Python Concepts Used

| Concept              | Purpose                       |
| -------------------- | ----------------------------- |
| Variables            | Store attendance details      |
| `input()`            | Accept student information    |
| `if-else`            | Check eligibility             |
| `while` loop         | Find minimum required classes |
| `for` loop           | Process future scenarios      |
| Dictionary           | Store attendance scenarios    |
| Arithmetic operators | Calculate percentages         |
| `round()`            | Round attendance values       |

## 9. GitHub Upload

Save your files with these names:

- Python file: `attendance_recovery.py`
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

Important: This project assumes that the eligibility threshold is 75%. Actual college attendance policies may differ. The future scenarios are estimates based on the specified attendance rates.
