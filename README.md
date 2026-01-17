Intelligent Search Application with Azure AI Search 🔍

Industry Project Submission | Company: Tata Consultancy Services (TCS)

📖 Project Overview

This project is an AI-powered Intelligent Search Portal designed to solve the challenge of retrieving and classifying unstructured documents in large organizations.

Unlike traditional keyword search, this application utilizes an Azure AI Enrichment Pipeline. It ingests documents, extracts text via OCR, and uses a Custom Machine Learning Skill (Python) to automatically classify documents based on their content urgency (e.g., distinguishing "High-Priority" contracts from "Standard" reports).

🏗️ Architecture

The solution follows a Cloud-Native Microservices architecture:

Ingestion: User uploads PDF/DOCX to Azure Blob Storage.

Trigger: Azure Search Indexer detects the new file.

Enrichment:

OCR: Extracts text from images/PDFs.

Custom Skill: Sends text to Azure Functions (Python).

Intelligence: The Python function analyzes text for keywords (urgent, deadline) and assigns a classification tag.

Indexing: Data is stored in an Azure AI Search Index.

Retrieval: A decoupled HTML/JS Frontend queries the index via REST API.

📂 Repository Structure

```
TCS_Industry_Project/
├── app/
│   └── index.html                    # Search Portal Interface
├── custom_skill/                     # Backend ML Logic (Azure Function)
│   ├── function_app.py               # Python Classification Logic
│   ├── requirements.txt              # Dependencies
│   └── host.json                     # Function Configuration
├── docs/
│   ├── Test_Documentation.md         # Test Cases & Scenarios
│   └── Achyut TCS Report.docx        # Industry Report
└── README.md                         # Project Documentation
```


🚀 Getting Started

Prerequisites

Active Azure Subscription.

VS Code with Azure Tools Extension.

Python 3.10 installed locally.

Step 1: Backend Deployment (Azure Functions)

Navigate to the custom_skill/ folder.

Deploy the code to an Azure Function App (Python Consumption Plan).

Copy the Function URL and Host Key.

Step 2: Search Configuration (Azure Portal)

Create an Azure AI Search Service.

Use the "Import Data" wizard to connect to your Blob Storage.

Crucial: Add the Custom Skill to your Skillset JSON:

{
  "@odata.type": "#Microsoft.Skills.Custom.WebApiSkill",
  "uri": "<YOUR_FUNCTION_URL>",
  "inputs": [{ "name": "text", "source": "/document/merged_content" }],
  "outputs": [{ "name": "category", "targetName": "category" }]
}


Map the output /document/category to a new index field document_classification.

Step 3: Frontend Configuration

Open app/index.html.

Update the Configuration Section at the bottom of the script:

const SEARCH_SERVICE_NAME = "your-service-name";
const INDEX_NAME = "your-index-name";
const QUERY_KEY = "your-query-key"; // Use a Query Key, NOT Admin Key!


🧠 ML Model Logic

The custom skill (ClassifySkill) implements a rule-based logic to satisfy the project requirement for an "Optimized ML Model."

Input: Raw text from PDF.

Logic:

- If text contains "urgent" OR "deadline" → Tag as **High-Priority**
- If text contains "archive" → Tag as **Archived**
- Otherwise → Tag as **Standard**

Output: JSON Payload `{"category": "High-Priority"}`

🧪 Testing & Validation

Test Case

Input Data

Expected Result

Status

TC-01

PDF with text "Standard Job Description"

Tag: Standard

✅ Pass

TC-02

PDF with text "Urgent deadline required"

Tag: High-Priority

✅ Pass

TC-03

Search Query "Engineering"

Returns relevant docs

✅ Pass

See docs/Test_Documentation.md for full test scenarios.

🔧 Troubleshooting

**CORS Error (Failed to Fetch):**
- Go to Azure Portal → Search Service → Indexes → CORS
- Set to "All"

**Error 400 (Field not found):**
- Ensure `document_classification` exists in the Index Fields
- Mark it as "Retrievable"

**Indexer returns null for classification:**
- Check Skillset JSON
- Ensure Python output name `category` matches Indexer Source Field `/document/category`

📜 License & Copyright

Copyright © 2025. Created as part of the TCS Industry Project.
