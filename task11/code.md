# Campus Registration Identifier Analyzer – Python Project

## 1. Problem Statement

Develop a Python program to analyse student registration ID numbers, validate their structure, extract important components, and classify students according to their branch and admission year.

The system should:

1. Accept student registration IDs from the user.
2. Validate the ID format and length.
3. Extract the admission year.
4. Extract the branch code.
5. Extract the student sequence number.
6. Identify the corresponding branch name.
7. Classify students based on admission year and branch.
8. Display valid and invalid registration IDs.
9. Generate a final summary report.

Assumed ID format for this project:

`YYBRNNN`

Example: `25CS101`

- `25` – Admission year (2025)
- `CS` – Branch code (Computer Science)
- `101` – Student sequence number

These are fictional example codes, not an official college registration-ID standard.

## 2. Algorithm

1. Start the program.
2. Define valid branch codes and their names.
3. Ask the user to enter the number of student records.
4. Read each student's registration ID.
5. Convert the ID into uppercase.
6. Check whether the ID contains exactly 7 characters.
7. Check whether the first two characters are digits.
8. Check whether the next two characters are valid branch codes.
9. Check whether the last three characters are digits.
10. If valid, extract the admission year, branch code, and sequence number.
11. Convert the admission year into a four-digit year.
12. Classify the student according to branch and admission year.
13. If invalid, display an error message.
14. Display all valid student records.
15. Display the number of valid and invalid IDs.
16. Stop the program.

## 3. Flowchart




## 4. Python Source Code

```

flowchart TD
    A([Start]) --> B[Define Branch Codes]
    B --> C[Enter Number of Records]
    C --> D[Read Student ID]
    D --> E{Length is 7?}

    E -- No --> F[Mark Invalid ID]
    E -- Yes --> G[Extract Year Branch and Sequence]

    G --> H{Year Contains Digits?}
    H -- No --> F
    H -- Yes --> I{Valid Branch Code?}

    I -- No --> F
    I -- Yes --> J{Sequence is Valid?}

    J -- No --> F
    J -- Yes --> K[Convert Admission Year]

    K --> L[Store Valid Record]
    L --> M{More Records?}

    F --> M
    M -- Yes --> D
    M -- No --> N[Display Valid Records]

    N --> O[Display Invalid Records]
    O --> P[Generate Branch and Year Summary]
    P --> Q[Display Final Summary]
    Q --> R([End])

```

## 5. Sample Input

```
===== CAMPUS REGISTRATION ID ANALYZER =====
Enter number of student records: 5

Student Record 1
Enter registration ID: 25CS101

Student Record 2
Enter registration ID: 25EC102

Student Record 3
Enter registration ID: 24ME103

Student Record 4
Enter registration ID: 25XX104

Student Record 5
Enter registration ID: ABCS105
```

## 6. Sample Output

```
===== VALID STUDENT RECORDS =====

Registration ID: 25CS101
Admission Year: 2025
Branch: Computer Science
Sequence Number: 101
------------------------------

Registration ID: 25EC102
Admission Year: 2025
Branch: Electronics
Sequence Number: 102
------------------------------

Registration ID: 24ME103
Admission Year: 2024
Branch: Mechanical
Sequence Number: 103
------------------------------

===== INVALID STUDENT RECORDS =====

25XX104 - Invalid branch code
ABCS105 - Invalid admission year

===== BRANCH-WISE SUMMARY =====

Computer Science : 1
Electronics : 1
Mechanical : 1
Civil : 0
Electrical : 0

===== YEAR-WISE SUMMARY =====

2024 : 1
2025 : 2

===== FINAL SUMMARY =====

Total Records: 5
Valid Records: 3
Invalid Records: 2
```

## 7. Mermaid Flowchart Code

Paste this code into [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com) to view the flowchart.

\#chatgpt-mermaid-\_r_15t\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_15t\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_15t\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_15t\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_15t\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_15t\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_15t\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_15t\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_15t\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_15t\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_15t\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_15t\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_15t\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_15t\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_15t\_ p{margin:0;}#chatgpt-mermaid-\_r_15t\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_15t\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_15t\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_15t\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_15t\_ .label text,#chatgpt-mermaid-\_r_15t\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_15t\_ .node rect,#chatgpt-mermaid-\_r_15t\_ .node circle,#chatgpt-mermaid-\_r_15t\_ .node ellipse,#chatgpt-mermaid-\_r_15t\_ .node polygon,#chatgpt-mermaid-\_r_15t\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_15t\_ .rough-node .label text,#chatgpt-mermaid-\_r_15t\_ .node .label text,#chatgpt-mermaid-\_r_15t\_ .image-shape .label,#chatgpt-mermaid-\_r_15t\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_15t\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_15t\_ .rough-node .label,#chatgpt-mermaid-\_r_15t\_ .node .label,#chatgpt-mermaid-\_r_15t\_ .image-shape .label,#chatgpt-mermaid-\_r_15t\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_15t\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_15t\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_15t\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_15t\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_15t\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_15t\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_15t\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_15t\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_15t\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_15t\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_15t\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_15t\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_15t\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_15t\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_15t\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_15t\_ .icon-shape,#chatgpt-mermaid-\_r_15t\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_15t\_ .icon-shape p,#chatgpt-mermaid-\_r_15t\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_15t\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_15t\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_15t\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_15t\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_15t\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_15t\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_15t\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_15t\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_15t\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_15t\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_15t\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_15t\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_15t\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_15t\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_15t\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_15t\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_15t\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_15t\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_15t\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_15t\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_15t\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_15t\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_15t\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_15t\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_15t\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_15t\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_15t\_ .node rect,#chatgpt-mermaid-\_r_15t\_ .node circle,#chatgpt-mermaid-\_r_15t\_ .node ellipse,#chatgpt-mermaid-\_r_15t\_ .node polygon,#chatgpt-mermaid-\_r_15t\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_15t\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_15t\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_15t\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_15t\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_15t\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartDefine Branch CodesEnter Number of RecordsRead Student IDLength is 7?Mark Invalid IDExtract Year Branch andSequenceYear Contains Digits?Valid Branch Code?Sequence is Valid?Convert Admission YearStore Valid RecordMore Records?Display Valid RecordsDisplay Invalid RecordsGenerate Branch and YearSummaryDisplay Final SummaryEndNoYesNoYesNoYesNoYesYesNo

## 8. Python Concepts Used

| Concept        | Purpose               |
| -------------- | --------------------- |
| Dictionary     | Store branch codes    |
| List           | Store student records |
| String slicing | Extract ID components |
| `isdigit()`    | Validate digits       |
| `if-else`      | Check ID conditions   |
| `for` loop     | Process records       |
| `sum()`        | Count students        |
| `try-except`   | Handle input errors   |
| `sorted()`     | Sort admission years  |

## 9. GitHub Upload Files

Create a folder named:

`Campus_Registration_Analyzer`

Inside it, save:

- `registration_analyzer.py`
- `flowchart.md`
- `README.md`

Project outcome: You will learn string slicing, validation, dictionaries, lists, loops, and student record classification using Python.
