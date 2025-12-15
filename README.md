# 📂 sam-s3-lambda-file-processor

**Example Project:** S3 File Processor using **AWS Lambda** and **SAM (Serverless Application Model)**.

This project demonstrates:

* **Serverless development with Python 3.12** 🐍
* **Local testing** with **SAM CLI** and **Docker** 🐳
* **Automatic deployment to AWS** with S3, Lambda, and IAM permissions ☁️

---

## 🏗️ Project Structure

* sam-s3-lambda-file-processor/
    * src/
        * file_processor/
            * app.py (Lambda function logic)
            * requirements.txt (Python dependencies)
    * events/
        * s3_event.json (Simulated event for local testing)
    * template.yaml (AWS resource definition)


---

## ⚙️ Requirements

To run and deploy this project, you need the following installed:

* **Python 3.12**
* **AWS CLI** configured
* **Docker Desktop** (required for SAM local testing)
* **AWS SAM CLI**

---

## 💻 Local Execution

1.  **Build the project:**

    ```powershell
    sam build
    ```

2.  **Invoke the Lambda function with a simulated event:**

    ```powershell
    sam local invoke FileProcessorFunction --event events/s3_event.json
    ```

    **Local Execution Details:**

    * The Lambda function detects if it is running locally (`AWS_SAM_LOCAL`).
    * **Skips writing** to the actual S3 bucket.
    * Returns the processed JSON in the console.

    **Example Output:**

    ```json
    {
      "statusCode": 200,
      "body": {
        "bucket": "test-input-bucket",
        "file_name": "example.txt",
        "size_bytes": 1234,
        "extension": "txt"
      }
    }
    ```

---

## 🚀 AWS Deployment

1.  **Build the project (if you haven't already):**

    ```powershell
    sam build
    ```

2.  **Guided deploy:**

    ```powershell
    sam deploy --guided
    ```

    **Suggested Values:**

    * `Stack name`: `sam-s3-file-processor`
    * `Region`: `eu-west-1` (or your preferred region)
    * `Save arguments to samconfig.toml`: `Y`

    **Resources Created Automatically:**

    * **S3 Buckets:** `InputBucket` and `OutputBucket`
    * **Lambda Function:** `FileProcessorFunction`
    * **S3 Trigger** automatically configured for the `InputBucket`.

### Test the Real AWS Flow

1.  **Upload a file** to the input bucket (`InputBucket`).
2.  The **Lambda function will be triggered** automatically.
3.  The **processed JSON** will be saved in the output bucket (`OutputBucket`).

**Check the Lambda function logs:**

```powershell
sam logs -n FileProcessorFunction --stack-name sam-s3-file-processor
