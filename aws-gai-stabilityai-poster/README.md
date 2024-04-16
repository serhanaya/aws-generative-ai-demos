# AWS-GAI-StabilityAI-Poster: Movie Poster Design with Generative AI

## Project Overview

This project demonstrates the use of Generative AI for movie poster design.  It leverages AWS services alongside Stability AI's image generation capabilities to create the following workflow:

1. A user provides a text prompt describing the desired movie poster.
2. The prompt is processed through an API Gateway and a Lambda function.
3. AWS Bedrock interacts with the Stability AI foundation model to generate a unique image based on the prompt.
4. The generated poster is stored in an S3 bucket.
5. A pre-signed URL is provided to the user for accessing and sharing the poster.

