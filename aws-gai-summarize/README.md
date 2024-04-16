# AWS-GAI-Summarize: Text Summarization for Manufacturing Issue Resolution

## Project Overview

This project streamlines issue resolution processes for manufacturers of large equipment.  It harnesses Generative AI to summarize lengthy incident reports and related data, allowing equipment experts (SMEs) to make faster, more informed decisions.

**Problem:** Incident reports in the manufacturing industry can be extensive, making it time-consuming for SMEs to diagnose and resolve equipment issues.

**Solution:**  A text summarization solution powered by foundation models reduces the time SMEs spend reviewing reports, improving response times and overall productivity.

## Use Case: Large Turbine Manufacturer

1. A technician at a remote turbine site creates a detailed incident report with images.
2. The report is submitted to a custom application.
3. An equipment SME reviews the report to determine the root cause and provide a solution. 
4. The Generative AI summarization solution condenses the incident report, aiding the SME's diagnosis.

## Architecture

The following diagram illustrates the architecture of the project:

<img src="docs/aws-gai-summarize-arch.jpg" alt="Architecture Diagram" width="500">

## Components

The following components are involved in the project:

* **User:** Initiates analysis by sending the incident report and relevant data as a prompt via a REST API call.
* **AWS API Gateway:** Receives incoming API requests, routing them to the Lambda function.
* **AWS Lambda Function:**  Core logic for the application:
    * Receives the prompt.
    * Interacts with AWS Bedrock to facilitate summarization.
    * Returns the summarized report to the API Gateway.
* **AWS Bedrock:** Interfaces with the Cohere foundation model for text summarization.
* **Cohere Foundation Model:** The generative AI model responsible for generating concise equipment issue summaries.
