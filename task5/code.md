# Python Project: Railway Fare and Reservation Calculator

Project Name: Railway Ticket Fare and Reservation Management System

Objective: To develop a Python program that calculates railway ticket fares for multiple passengers using distance slabs, travel classes, age-based concessions, reservation fees, and cancellation penalties.

## 1. Problem Statement

Develop a Python program to calculate railway ticket fares for multiple passengers based on their journey details.

The program should:

1. Accept the number of passengers.
2. Enter passenger name and age.
3. Accept journey distance in kilometres.
4. Select travel class (Sleeper, AC 3 Tier, or AC 2 Tier).
5. Calculate fares using distance-based slabs.
6. Apply age-based concessions:
   - Children below 5 years: Free.
   - Passengers aged 60 and above: 20% concession.
   - Other passengers: No concession.
7. Add reservation fees.
8. Calculate the total reservation amount.
9. Calculate cancellation penalties when a ticket is cancelled.
10. Display the final fare for each passenger.

Note: These are assumed rules for an educational project, not actual Indian Railways fare or concession policies.

## 2. Algorithm

1. Start the program.
2. Enter the number of passengers.
3. Enter the journey distance.
4. Select the travel class.
5. Enter passenger details (name and age).
6. Validate the passenger age and journey distance.
7. Calculate the basic fare based on distance slabs.
8. Apply the selected class fare rate.
9. Apply age-based concessions.
10. Add reservation fees.
11. Calculate the final ticket fare.
12. Ask whether the passenger wants to cancel the ticket.
13. If cancelled, calculate the cancellation penalty.
14. Calculate the refund amount.
15. Display passenger-wise ticket details.
16. Display the total reservation cost.
17. Stop the program.

## 3. Flowchart

[

[slideteam.net](https://www.slideteam.net/ticket-flow-powerpoint-ppt-template-bundles.html?utm_source=chatgpt.com)

## 4. Python Source Code

```

flowchart TD

    A([Start]) --> B[/Enter Journey Distance/]
    B --> C{Valid Distance?}

    C -->|No| D[Display Invalid Distance]
    D --> Z([Stop])

    C -->|Yes| E[/Select Travel Class/]
    E --> F{Valid Class?}

    F -->|No| G[Display Invalid Class]
    G --> Z

    F -->|Yes| H[/Enter Number of Passengers/]
    H --> I[/Enter Passenger Name and Age/]

    I --> J{Valid Age?}

    J -->|No| K[Display Invalid Age]
    K --> Z

    J -->|Yes| L[Calculate Distance Slab Fare]

    L --> M[Apply Travel Class Rate]

    M --> N{Age Below 5?}

    N -->|Yes| O[100% Concession]
    N -->|No| P{Age 60 or Above?}

    P -->|Yes| Q[Apply 20% Concession]
    P -->|No| R[No Concession]

    O --> S[Calculate Final Fare]
    Q --> S
    R --> S

    S --> T[Add Reservation Fee]

    T --> U{Cancel Ticket?}

    U -->|Yes| V[Calculate 10% Cancellation Penalty]
    V --> W[Calculate Refund]

    U -->|No| X[Confirm Ticket]

    W --> Y[Update Booking Summary]
    X --> Y

    Y --> AA{More Passengers?}

    AA -->|Yes| I
    AA -->|No| AB[Display Total Booking and Refund]

    AB --> Z([Stop])
0
```

## 5. Sample Input

```
===== RAILWAY RESERVATION SYSTEM =====

Enter journey distance (KM): 200

Available Classes:
1. Sleeper
2. AC 3 Tier
3. AC 2 Tier

Enter travel class: sleeper
Enter number of passengers: 3

Passenger 1
Enter passenger name: Ravi
Enter passenger age: 30
Cancel ticket? (yes/no): no

Passenger 2
Enter passenger name: Kumar
Enter passenger age: 65
Cancel ticket? (yes/no): no

Passenger 3
Enter passenger name: Sai
Enter passenger age: 25
Cancel ticket? (yes/no): yes
```

## 6. Sample Output

```
===== RAILWAY RESERVATION SYSTEM =====

----- TICKET DETAILS -----

Passenger Name: Ravi
Age: 30
Travel Class: SLEEPER
Distance: 200 KM
Basic Fare: Rs. 250.0
Concession: 0 %
Concession Amount: Rs. 0.0
Reservation Fee: Rs. 40
Final Fare: Rs. 290.0
Ticket Confirmed!

----- TICKET DETAILS -----

Passenger Name: Kumar
Age: 65
Travel Class: SLEEPER
Distance: 200 KM
Basic Fare: Rs. 250.0
Concession: 20 %
Concession Amount: Rs. 50.0
Reservation Fee: Rs. 40
Final Fare: Rs. 240.0
Ticket Confirmed!

----- TICKET DETAILS -----

Passenger Name: Sai
Age: 25
Travel Class: SLEEPER
Distance: 200 KM
Basic Fare: Rs. 250.0
Concession: 0 %
Concession Amount: Rs. 0.0
Reservation Fee: Rs. 40
Final Fare: Rs. 290.0
Cancellation Penalty: Rs. 29.0
Refund Amount: Rs. 261.0

===== RESERVATION SUMMARY =====

Total Passengers: 3
Total Active Booking Amount: Rs. 530.0
Total Refund Amount: Rs. 261.0

Reservation Process Completed!
```

## 7. Mermaid Flowchart Code

Copy this code into [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com) to generate your flowchart.

\#chatgpt-mermaid-\_r_lc\_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(237, 237, 237);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-\_r_lc\_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_lc\_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-\_r_lc\_ .error-icon{fill:rgb(48, 48, 48);}#chatgpt-mermaid-\_r_lc\_ .error-text{fill:rgb(237, 237, 237);stroke:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_lc\_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-\_r_lc\_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-\_r_lc\_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-\_r_lc\_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-\_r_lc\_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-\_r_lc\_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-\_r_lc\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_lc\_ .marker.cross{stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_lc\_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-\_r_lc\_ p{margin:0;}#chatgpt-mermaid-\_r_lc\_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_lc\_ .cluster-label text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_lc\_ .cluster-label span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_lc\_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-\_r_lc\_ .label text,#chatgpt-mermaid-\_r_lc\_ span{fill:rgb(237, 237, 237);color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_lc\_ .node rect,#chatgpt-mermaid-\_r_lc\_ .node circle,#chatgpt-mermaid-\_r_lc\_ .node ellipse,#chatgpt-mermaid-\_r_lc\_ .node polygon,#chatgpt-mermaid-\_r_lc\_ .node path{fill:rgb(9, 23, 44);stroke:rgb(31, 78, 148);stroke-width:1px;}#chatgpt-mermaid-\_r_lc\_ .rough-node .label text,#chatgpt-mermaid-\_r_lc\_ .node .label text,#chatgpt-mermaid-\_r_lc\_ .image-shape .label,#chatgpt-mermaid-\_r_lc\_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-\_r_lc\_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-\_r_lc\_ .rough-node .label,#chatgpt-mermaid-\_r_lc\_ .node .label,#chatgpt-mermaid-\_r_lc\_ .image-shape .label,#chatgpt-mermaid-\_r_lc\_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-\_r_lc\_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-\_r_lc\_ .root .anchor path{fill:rgb(175, 175, 175)!important;stroke-width:0;stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_lc\_ .arrowheadPath{fill:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_lc\_ .edgePath .path{stroke:rgb(175, 175, 175);stroke-width:1px;}#chatgpt-mermaid-\_r_lc\_ .flowchart-link{stroke:rgb(175, 175, 175);fill:none;}#chatgpt-mermaid-\_r_lc\_ .edgeLabel{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_lc\_ .edgeLabel p{background-color:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_lc\_ .edgeLabel rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_lc\_ .labelBkg{background-color:rgba(0, 0, 0, 0.5);}#chatgpt-mermaid-\_r_lc\_ .cluster rect{fill:rgb(48, 48, 48);stroke:rgba(255, 255, 255, 0.15);stroke-width:1px;}#chatgpt-mermaid-\_r_lc\_ .cluster text{fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_lc\_ .cluster span{color:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_lc\_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(48, 48, 48);border:1px solid rgba(255, 255, 255, 0.15);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-\_r_lc\_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(237, 237, 237);}#chatgpt-mermaid-\_r_lc\_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-\_r_lc\_ .icon-shape,#chatgpt-mermaid-\_r_lc\_ .image-shape{background-color:rgb(0, 0, 0);text-align:center;}#chatgpt-mermaid-\_r_lc\_ .icon-shape p,#chatgpt-mermaid-\_r_lc\_ .image-shape p{background-color:rgb(0, 0, 0);padding:2px;}#chatgpt-mermaid-\_r_lc\_ .icon-shape .label rect,#chatgpt-mermaid-\_r_lc\_ .image-shape .label rect{opacity:0.5;background-color:rgb(0, 0, 0);fill:rgb(0, 0, 0);}#chatgpt-mermaid-\_r_lc\_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-\_r_lc\_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-\_r_lc\_ .node .neo-node{stroke:rgb(31, 78, 148);}#chatgpt-mermaid-\_r_lc\_ [data-look="neo"].node rect,#chatgpt-mermaid-\_r_lc\_ [data-look="neo"].cluster rect,#chatgpt-mermaid-\_r_lc\_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-\_r_lc\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_lc\_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-\_r_lc\_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-\_r_lc\_-gradient);stroke-width:1px;}#chatgpt-mermaid-\_r_lc\_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_lc\_ [data-look="neo"].node .neo-line path{stroke:rgb(31, 78, 148);filter:none;}#chatgpt-mermaid-\_r_lc\_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-\_r_lc\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_lc\_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-\_r_lc\_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-\_r_lc\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_lc\_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-\_r_lc\_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-\_r_lc\_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_lc\_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(153, 206, 255);}#chatgpt-mermaid-\_r_lc\_ .node tspan[font-weight="normal"],#chatgpt-mermaid-\_r_lc\_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-\_r_lc\_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-width:1px;}#chatgpt-mermaid-\_r_lc\_ .node rect,#chatgpt-mermaid-\_r_lc\_ .node circle,#chatgpt-mermaid-\_r_lc\_ .node ellipse,#chatgpt-mermaid-\_r_lc\_ .node polygon,#chatgpt-mermaid-\_r_lc\_ .node path{fill:rgb(0, 40, 77);stroke:rgba(255, 255, 255, 0.1);stroke-width:1px;}#chatgpt-mermaid-\_r_lc\_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-\_r_lc\_ .mermaid-decision .label-container{fill:rgb(0, 14, 26);stroke:rgb(26, 62, 95);stroke-dasharray:2,2;}#chatgpt-mermaid-\_r_lc\_ .edgePaths .flowchart-link{stroke:rgb(175, 175, 175);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-\_r_lc\_ .marker{fill:rgb(175, 175, 175);stroke:rgb(175, 175, 175);}#chatgpt-mermaid-\_r_lc\_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter Journey DistanceValid Distance?Display Invalid DistanceStopSelect Travel ClassValid Class?Display Invalid ClassEnter Number of PassengersEnter Passenger Name and AgeValid Age?Display Invalid AgeCalculate Distance Slab FareApply Travel Class RateAge Below 5?100% ConcessionAge 60 or Above?Apply 20% ConcessionNo ConcessionCalculate Final FareAdd Reservation FeeCancel Ticket?Calculate 10% CancellationPenaltyCalculate RefundConfirm TicketUpdate Booking SummaryMore Passengers?Display Total Booking andRefundNoYesNoYesNoYesYesNoYesNoYesNoYesNo

## 8. Python Concepts Used

| Concept              | Purpose                             |
| -------------------- | ----------------------------------- |
| Variables            | Store passenger details             |
| Dictionary           | Store class rates                   |
| `if-elif-else`       | Apply concessions                   |
| `for` loop           | Process multiple passengers         |
| Arithmetic operators | Calculate fares                     |
| Input validation     | Check age and distance              |
| `round()`            | Round fare amounts                  |
| Accumulators         | Calculate total booking and refunds |

## 9. GitHub Upload

Save your files with these names:

- Python file: `railway_fare_calculator.py`
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

Important: This project uses assumed educational fare rates, class multipliers, concessions and cancellation penalties. They are not official railway booking rules.
