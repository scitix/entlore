---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T13:24:35+08:00"
authors:
  - "Simon Osborn"
department: "Platform Ops Dept"
---
## This Week's Work

The weekly status uses blue for done items, yellow for todo work, red for blockers, green for active progress, and purple for areas needing key attention. @Simon Osborn built xanios one-click SQL rule sync, covering unified synchronization across modules and multiple data types, while also continuing System-e6382db83d database metadata sync and finishing Redis database metadata synchronization. He also added Mongo database-creation and account-creation ticket capabilities, with functional testing still in progress before launch.

For Pelkeld, @Simon Osborn advanced environment deployment and containerization for virtual-machine MySQL instances that SRE had maintained, completing the Kubeconfig application, enabling PelkeldCasridge management permissions, and preparing 3 data-node resources. @Simon Osborn and @Kara Ingram Irwin finished SSD VG preparation, deployed the KubeBlocks environment, completed the containerized PelkeldCasridge MySQL deployment, and connected the network path. The team will continue moving Pelkeld physical-machine data into containerized MySQL and carry out the database cutover.

The team kept System-18eecad128 maintained after writing up deployment experience and operating procedures, so Pelshaw can serve as a later reference for standardized deployment, operations maintenance, and delivery. @Simon Osborn and @Kara Ingram Irwin continued supporting database access requests from R&D and business colleagues, synchronized Pelkeld MySQL physical-machine instance information with @Ethan Norris, and confirmed both network connectivity and base resources for Pelkeld MySQL. They also helped @Victor Quigley with database account creation and access, and the team aligned connection details plus maintenance content for cororum integration with maraum database credentials, improving business-side database usage and access efficiency. Overall, this week centered on xanios platform capability work, database containerized deployment, and support for R&D and business needs.

## Next Week's Plan

Next week, the team plans to move Pelkeld physical-machine mysql data into PelkeldCasridgemysql. After that, Pelshaw will be delivered to R&D colleagues.

## Coordination and Help Needed