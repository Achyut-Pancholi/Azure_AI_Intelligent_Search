# 🔍 Intelligent Search Application with Azure AI Search

> **Industry Project Submission** | *Company:* **Tata Consultancy Services (TCS)**

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Azure](https://img.shields.io/badge/Azure-AI%20Search-0078D4?logo=microsoft-azure)](https://azure.microsoft.com/)
[![License](https://img.shields.io/badge/License-TCS%202025-green)]()

---

## 📖 Project Overview

An **AI-powered Intelligent Search Portal** that solves the challenge of retrieving and classifying unstructured documents in large organizations.

Unlike traditional keyword search, this application harnesses an **Azure AI Enrichment Pipeline** to:
- 📄 Ingest documents from multiple formats (PDF, DOCX)
- 🔤 Extract text via OCR for image-based content
- 🤖 Automatically classify documents by urgency using a **Custom ML Skill** (Python)
- ⚡ Distinguish between "High-Priority" contracts and "Standard" reports

---

## 🏗️ Architecture

The solution follows a **Cloud-Native Microservices** architecture:

| Component | Function |
|-----------|----------|
| **Ingestion** | User uploads PDF/DOCX to Azure Blob Storage |
| **Trigger** | Azure Search Indexer detects new files |
| **OCR** | Extracts text from images and PDFs |
| **Custom Skill** | Sends text to Azure Functions (Python) for analysis |
| **Intelligence** | Python function analyzes text for keywords and assigns classification |
| **Indexing** | Data stored in Azure AI Search Index |
| **Retrieval** | HTML/JS Frontend queries index via REST API |

---

## 📂 Repository Structure

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

---

## 🚀 Getting Started

### Prerequisites

| Requirement | Details |
|------------|---------|
| **Azure Subscription** | Active Azure account with available quota |
| **VS Code** | With [Azure Tools Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-node-azure-pack) |
| **Python** | Version 3.10 or higher installed locally |
| **Git** | For version control |

### Installation Steps

#### **Step 1: Backend Deployment (Azure Functions)**

```bash
# Navigate to the custom skill directory
cd custom_skill/

# Install dependencies
pip install -r requirements.txt

# Deploy to Azure Function App
# Use Azure CLI: az functionapp deployment source config-zip ...
# Or use VS Code Azure Functions extension
```

**Important:** Copy your Function URL and Host Key after deployment.

---

#### **Step 2: Search Configuration (Azure Portal)**

1. Create an **Azure AI Search Service** in Azure Portal
2. Use the **"Import Data"** wizard to connect your Blob Storage
3. Add the **Custom Skill** to your Skillset JSON:

```json
{
  "@odata.type": "#Microsoft.Skills.Custom.WebApiSkill",
  "uri": "<YOUR_FUNCTION_URL>",
  "inputs": [{ "name": "text", "source": "/document/merged_content" }],
  "outputs": [{ "name": "category", "targetName": "category" }]
}
```

4. Map the output `/document/category` to a new index field `document_classification`

---

#### **Step 3: Frontend Configuration**

1. Open `app/index.html`
2. Update the **Configuration Section** at the bottom of the script:

```javascript
const SEARCH_SERVICE_NAME = "your-service-name";
const INDEX_NAME = "your-index-name";
const QUERY_KEY = "your-query-key";  // Use Query Key, NOT Admin Key!
```

---

## 🧠 ML Model Logic

The **ClassifySkill** implements intelligent rule-based classification:

### **Classification Algorithm**

### **Classification Algorithm**

| Condition | Output Classification |
|-----------|----------------------|
| Text contains **"urgent"** OR **"deadline"** | 🔴 **High-Priority** |
| Text contains **"archive"** | 📦 **Archived** |
| Otherwise (default) | 📋 **Standard** |

**Example Output:**
```json
{
  "category": "High-Priority"
}
```

---

## 🧪 Testing & Validation

| Test Case | Input | Expected Result | Status |
|-----------|-------|-----------------|--------|
| **TC-01** | PDF with text "Standard Job Description" | Classification: `Standard` | ✅ Pass |
| **TC-02** | PDF with text "Urgent deadline required" | Classification: `High-Priority` | ✅ Pass |
| **TC-03** | Search Query "Engineering" | Returns relevant documents | ✅ Pass |

> 📌 Full test scenarios available in [docs/Test_Documentation.md](docs/Test_Documentation.md)

---

## 🔧 Troubleshooting

### **❌ CORS Error (Failed to Fetch)**
```
Solution:
1. Go to Azure Portal → Search Service → Indexes
2. Find your index → CORS settings
3. Set CORS to "Allow all origins"
```

### **❌ Error 400 (Field not found)**
```
Solution:
1. Verify document_classification field exists in Index Fields
2. Ensure it's marked as "Retrievable"
3. Sync the skillset to regenerate the index
```

### **❌ Indexer returns null for classification**
```
Solution:
1. Verify Skillset JSON configuration
2. Check Python output name matches: category → /document/category
3. Ensure Function URL and Host Key are correct
4. Review Azure Function logs for errors
```

---

## 📊 Key Features

- ✅ **Automatic OCR Processing** - Extracts text from images and scanned documents
- ✅ **Intelligent Classification** - Rule-based ML model for document urgency assessment
- ✅ **Scalable Architecture** - Built on Azure Functions (serverless, auto-scaling)
- ✅ **Full-Text Search** - Azure AI Search with semantic capabilities
- ✅ **REST API Integration** - Easy integration with external systems
- ✅ **Web Portal** - User-friendly search interface

---

## 💡 How It Works

```
User Upload (PDF/DOCX)
        ↓
Blob Storage Detection
        ↓
Indexer Trigger
        ↓
OCR Processing
        ↓
Custom Python Skill (Classification)
        ↓
Indexed in Azure Search
        ↓
Frontend Query & Display Results
```

---

---

## 📝 Configuration Details

### **Environment Variables** (in `host.json`)
```json
{
  "version": "2.0",
  "logging": {
    "applicationInsights": {
      "samplingSettings": {
        "isEnabled": true,
        "maxTelemetryItemsPerSecond": 20
      }
    }
  },
  "functionTimeout": "00:05:00"
}
```

### **Dependencies** (in `requirements.txt`)
```
azure-functions
requests
numpy
scikit-learn
```

---

## 🤝 Contributing

This is a **TCS Industry Project** submission. For contributions or questions:
1. Review the [Test Documentation](docs/Test_Documentation.md)
2. Follow Azure best practices for function development
3. Test locally before deploying

---

## 📜 License & Copyright

Created as part of the TCS Industry Project
```

---

## 📞 Support & Resources

| Resource | Link |
|----------|------|
| **Azure AI Search Docs** | [Microsoft Learn](https://learn.microsoft.com/en-us/azure/search/) |
| **Azure Functions** | [Getting Started](https://learn.microsoft.com/en-us/azure/azure-functions/) |
| **Python SDK** | [azure-search-documents](https://pypi.org/project/azure-search-documents/) |

---

**Last Updated:** January 17, 2026  
**Project Status:** ✅ Active
