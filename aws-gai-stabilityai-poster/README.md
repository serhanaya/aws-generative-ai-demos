# AWS-GAI-StabilityAI-Poster: Movie Poster Design with Generative AI

## Project Overview

This project demonstrates the use of Generative AI for movie poster design.  It leverages AWS services alongside Stability AI's image generation capabilities to create the following workflow:

1. A user provides a text prompt describing the desired movie poster.
2. The prompt is processed through an API Gateway and a Lambda function.
3. AWS Bedrock interacts with the Stability AI foundation model to generate a unique image based on the prompt.
4. The generated poster is stored in an S3 bucket.
5. A pre-signed URL is provided to the user for accessing and sharing the poster.

## Architecture

The following diagram illustrates the architecture of the project:

<img src="./docs/movie_poster_design_architecture.jpg" alt="Architecture Diagram" width="600">

## Components

The following components are involved in the project:

* **End User:** Initiates the process by sending a movie poster description (prompt) via a REST API call.
* **AWS API Gateway:** Serves as the entry point for API requests, routing them to the Lambda function. 
* **AWS Lambda Function:**  Handles the core logic:
    * Receives the prompt and any inference parameters.
    * Interacts with AWS Bedrock to trigger image generation.
    * Retrieves the image from S3.
    * Generates a pre-signed URL for secure access.
    * Returns the pre-signed URL to the API Gateway.
* **AWS Bedrock:** Interacts with the Stability AI foundation model for image generation.
* **Stability AI Foundation Model:** The generative AI model responsible for creating the movie poster based on the provided prompt.
* **Amazon S3 Bucket:** Stores the generated movie poster image. 
* **Pre-signed URL:** A temporary, shareable URL that grants access to the movie poster in S3.

## Project Setup

To set up the project, follow these steps:

1. **Create an S3 Bucket:**
   * Go to the AWS S3 console.
   * Create a bucket and give it a unique name (e.g., "movie-poster-design-01")

2. **Create an AWS Lambda Function:**
   * Go to the AWS Lambda console.
   * Create a function with an appropriate name (e.g., "movie-poster-design").
   * Choose Python 3.12 as the runtime.

**Lambda Configuration & Permissions:**

1. **Check Boto3 Version:**
   * Inside the Lambda function's code, import Boto3 and print its version.
   * If the version is below `1.28.63`, follow the AWS documentation to create a Lambda layer and add it to your function.  

2. **Adjust Timeout:**
   * Go to the Lambda function's **Configuration** -> **General configuration**.
   * Increase the timeout to at least one minute (e.g., `63 seconds`).

3. **IAM Permissions:**
   * Go to the Lambda function's **Permissions** tab.
   * Attach an IAM policy granting at least the following:
     * Full access to the S3 bucket you created.
     * The ability to invoke Amazon Bedrock.
   * **Important:** For production, refine these permissions to be more granular.

4. **Lambda Function Code**

Check Lambda function from source folder: [src/lambda_function.py](src/lambda_function.py)

Absolutely! Here's the converted version with proper Markdown formatting:

5. **API Gateway**

   **Create an API Gateway REST API**
   * Navigate to the API Gateway service in the AWS console.
   * Click `Create API`.
   * Select `REST API` and click `Build`.
   * Give your API a descriptive name (e.g., `Movie Poster API`).

   **Create a Resource**
   * Click on `Actions` and select `Create Resource`.
   * Name the resource descriptively (e.g.,  `movie-poster-api-design`).

   **Create a GET Method**
   * Select the newly created resource.
   * Click on `Actions` and select `Create Method`.
   * Choose `GET` from the dropdown.
   * Set the following:
      *  Integration type: Lambda Function
      *  Lambda Function: (Select your existing Lambda function) 

   **Configure Method Request**
   * Navigate to the GET method's `Method Request`.
   * In `URL Query String Parameters`, click `Add query string`.
   * Set the following:
      * Parameter name: `prompt`
      * Required: True 

   **Enable Request Validation**
   * In the `Method Request` settings:
      * Check `Validate query string parameters and headers`.

   **Configure Integration Request**
   * Navigate to the GET method's `Integration Request`.
   * Go to `Mapping Templates`.
   *  Set Content-Type to `application/json`.
   * Add the following template body:

   ```json
   {
     "prompt": "$input.params('prompt')" 
   }
   ```

   **Deploy the API**
   * Click  on `Actions` and select `Deploy API`.
   * Create a new stage (e.g., `dev`) and click `Deploy`.

**Important Notes:**

* **IAM Permissions:** Ensure your Lambda function has these IAM permissions:
   * Amazon Bedrock Full Access
   * Amazon S3 Full Access (You'll want to refine this for production)
* **Re-Deployment:** Any changes to the API Gateway configuration require re-deployment for them to take effect. 

