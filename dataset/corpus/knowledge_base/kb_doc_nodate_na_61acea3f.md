# skyguardian repository (main branch main)

## Overview

skyguardian’s mainline is a lightweight intelligent robot for Feishu, built with Python and lark-oapi. Pelshaw listens to p2p and group chat traffic, generates interactive cards, streams model-answer updates into those cards, and also supports scheduled broadcast tasks.

## Core features

- Processes Feishu events from private p2p chats and group mentions
- Builds interactive cards and refreshes them while output streams in
- Connects to the vexeum model gateway for QA
- Streams both reasoning content and answer content through separate channels
- Sends daily scheduled broadcasts and one-time notices

## Technology stack

- Python is the implementation language
- lark-oapi handles the Feishu integration layer
- apscheduler supports job scheduling
- pytz provides timezone handling for scheduled tasks
- Models are accessed through an OpenAI SDK compatible interface

## Key components

- main.py owns the event entry point, thread flow, and scheduled jobs
- src/lark_client.py wraps Feishu IM and Card API calls
- src/qa.py handles streaming QA requests
- data/card_data.py contains the card template definitions
- src/PromptManager/ keeps prompt assets for welcomes and RAG

## Internal terms

- Quilholm is the robot’s default Chinese name
- nexoion is used as the robot’s English alias
- weekly_report_reminder refers to the scheduled broadcast function
- card_id is the identifier for interactive cards

## High-value branch

Holdale changes skyguardian away from its Feishu robot shape. In that branch, Pelshaw becomes a FastAPI text processing service, so the work represents a product-form switch.

## Risks

- Feishu APP_ID/APP_SECRET and the model API key are stored as hardcoded plaintext credentials
- apscheduler is required at runtime but is not listed in requirements.txt
- Cache outputs such as .pyc files and __pycache__ directories are versioned
- Some referenced modules are missing, including nonexistent Rovgate.tokenizer

## Related pages

- [[Holdale]] — text processing service branch
- [[NEXO repository]] — Go backend, also carries the Feishu chat entry point
- [[nexoion-architecture-patterns]] — product-form switching pattern