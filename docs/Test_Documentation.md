# Testing Documentation
**Project:** Building Intelligent Application with Azure AI Search

---

## I. Test Design Document

| Test Case # | Test Step # | Application /Screen | Test Case | Pre-Requisites | Input provided to the data analysis | Iteration # | Cross-Validation Method | Actual result | Defect[Y/N] |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC01 | 1 | Azure Portal / Search Service | Verify Blob Storage Connection | Storage Account created and container `documents` exists. | Connection String, Container Name | 1 | Check "Test Connection" status in Data Source setup. | Connection Successful. | N |
| TC02 | 1 | Azure Function / Code+Test | Verify ML Logic (Standard Case) | Function App deployed and running. | Text Payload: `{"values": [{"recordId": "1", "data": {"text": "This is a standard job description."}}]}` | 1 | Verify JSON Response body. | JSON Output: `{"category": "Standard"}` | N |
| TC03 | 1 | Azure Function / Code+Test | Verify ML Logic (Urgent Case) | Function App deployed and running. | Text Payload: `{"values": [{"recordId": "1", "data": {"text": "This task is urgent and has a deadline."}}]}` | 1 | Verify JSON Response body. | JSON Output: `{"category": "High-Priority"}` | N |
| TC04 | 2 | Search Explorer | Verify Indexer Output Mapping | Indexer Run Status = Success. | Query: `search=*&$select=document_classification` | 1 | Compare `document_classification` field in JSON vs Expected. | Field matches classification. | N |
| TC05 | 3 | Web App (Frontend) | Verify End-to-End Search | Frontend running locally; CORS enabled. | Search Query: "engineering" | 1 | Compare UI results with Source PDF content. | Relevant PDF displayed with correct tag. | N |

---

## II. Test Case Template

| Test Case # | Test Case Description | Application /Screen for searching | Test Step | Test Step Description | Expected Result | Pre-Requisites | Test Data |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC03 | Validate "High-Priority" Classification Logic | Azure Function / Postman | 1 | Send POST request to Function URL with "urgent" text. | Response body should contain "High-Priority". | Function App running. | Text: "Urgent deadline" |
| TC05 | Validate Frontend Search functionality | Web App (HTML) | 1 | Enter "Standard" in search bar and click Search. | List of documents tagged as "Standard" should appear. | CORS enabled on Index. | Keyword: "Standard" |
| TC06 | Validate Document Upload | Web App (HTML) | 1 | Select `test.pdf` and click Upload. | Success message "Upload Successful". | Valid SAS Token. | File: `test.pdf` |

---

## III. Test Scenario Template

| Req Id | Test Scenario Id | Application /Screen | High Level Test Conditions | Expected Results | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- |
| REQ01 | TS01 | Search Portal Home | Search for keywords existing in the document. | The search result should list documents containing the keyword. | High |
| REQ02 | TS02 | Upload Section | Upload a PDF document to the portal. | File uploaded successfully to Azure Blob Storage; Indexer triggered. | High |
| REQ03 | TS03 | Search Result Grid | Verify AI Classification (ML Model). | Documents should display a "High-Priority" or "Standard" tag based on content. | High |
| REQ04 | TS04 | Search Portal | Search using Natural Language (e.g., "urgent documents"). | Results should filter/rank documents classified as "High-Priority". | Medium |