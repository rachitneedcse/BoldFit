# 🚀 AI Supply-Chain Automation Agent  
### Inventory Forecasting • Auto Reorder • LLM-Generated PO Emails • Real-Time Email Alerts • Founder Summary

This project is an **AI-powered Supply Chain Automation Agent** designed for fast-moving D2C companies like **Boldfit**.  
It automates forecasting, purchasing decisions, supplier communication, and leadership reporting — all through intelligent Python + LLM agents.

---

## Features

### 1. **Reads Inventory Data (from Excel)**
Processes:
- SKU  
- Quantity in stock  
- Lead time  
- Last 30-day sales  
- Supplier info  
- Unit cost  

### 2. **Forecasts Stockouts**
Calculates:
- Average daily sales  
- Days until stockout  
- Whether stockout happens before lead time  

### 3. **Auto-Generates Reorder Quantity**
Formula:
```
reorder_qty = avg_daily_sales × (lead_time + 7 days buffer)
```

### 4. **Generates Purchase Order (PO) Emails Using an LLM**
- Concise  
- Professional  
- Supplier-ready  

### 5. **Sends Real-Time Email Notifications**
Uses Gmail SMTP to send alerts when a PO is triggered.

### 6. **Generates a Founder-Level Business Summary Using LLM**
Summarizes:
- Critical SKUs  
- Supplier load  
- Estimated total cost  
- Operational recommendations  

Saved as: **`founder_summary.txt`**

---

## Project Structure

```
BoldFit-Agent/
│
├── agent.py               # Main automation agent
├── mail_helper.py         # Sends real email notifications
├── inventory.xlsx         # Input dataset
├── forecast_results.csv   # Generated forecast output
├── founder_summary.txt    # LLM-generated business summary
└── README.md              # This file
```

---

## Tech Stack

### **Python**
- pandas  
- openpyxl  
- smtplib  
- python-dotenv  

### **LLMs**
- OpenRouter API  
- Model: `openai/gpt-oss-20b:free`  

### **Notifications**
- Gmail SMTP (real-time alerts)

---

## Environment Variables (`.env`)

Create a `.env` file:

```
api_key=YOUR_OPENROUTER_API_KEY
APP_PASSWORD=YOUR_GMAIL_APP_PASSWORD
SENDER_EMAIL=your@gmail.com
RECEIVER_EMAIL=recipient@gmail.com
```

---

## ▶How to Run

1. Install dependencies:
   ```bash
   pip install pandas python-dotenv openai openpyxl
   ```

2. Add your `.env` file.

3. Run the agent:
   ```bash
   python agent.py
   ```

4. Outputs:
   - Real email notifications  
   - PO email text  
   - Forecast results CSV  
   - Founder summary text  




