# 🚀 AI Supply-Chain Automation Agent  
### Inventory Forecasting • Auto Reorder • LLM-Generated PO Emails • Real-Time Email Alerts • Founder Summary

This project is an **AI-powered Supply Chain Automation Agent** designed for fast-moving D2C companies like **Boldfit**.  
It automates forecasting, purchasing decisions, supplier communication, and leadership reporting — all through intelligent Python + LLM agents.

---

## 🧠 Features

### ✅ 1. **Reads Inventory Data (from Excel)**
Processes:
- SKU  
- Quantity in stock  
- Lead time  
- Last 30-day sales  
- Supplier info  
- Unit cost  

### ✅ 2. **Forecasts Stockouts**
Calculates:
- Average daily sales  
- Days until stockout  
- Whether stockout happens before lead time  

### ✅ 3. **Auto-Generates Reorder Quantity**
Formula:
```
reorder_qty = avg_daily_sales × (lead_time + 7 days buffer)
```

### ✅ 4. **Generates Purchase Order (PO) Emails Using an LLM**
- Concise  
- Professional  
- Supplier-ready  

### ✅ 5. **Sends Real-Time Email Notifications**
Uses Gmail SMTP to send alerts when a PO is triggered.

### ✅ 6. **Generates a Founder-Level Business Summary Using LLM**
Summarizes:
- Critical SKUs  
- Supplier load  
- Estimated total cost  
- Operational recommendations  

Saved as: **`founder_summary.txt`**

---

## 📂 Project Structure

```
BoldFit-Agent/
│
├── agent.py               # Main automation agent
├── mail_helper.py         # Sends real email notifications
├── inventory.xlsx         # Input dataset
├── forecast_results.csv   # Generated forecast output
├── founder_summary.txt    # LLM-generated business summary
├── .env                   # API & email secrets (not committed)
└── README.md              # This file
```

---

## ⚙️ Tech Stack

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

## 🔑 Environment Variables (`.env`)

Create a `.env` file:

```
api_key=YOUR_OPENROUTER_API_KEY
APP_PASSWORD=YOUR_GMAIL_APP_PASSWORD
SENDER_EMAIL=your@gmail.com
RECEIVER_EMAIL=recipient@gmail.com
```

---

## ▶️ How to Run

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

---

## 📧 Real Email Notification Example

**Subject:**
```
PO Triggered for SKU P98320
```

**Body:**
```
PO triggered for P98320: 140 units. Estimated cost: ₹22300
```

---

## 🧾 Sample Founder Summary (LLM-Generated)

```
3 SKUs are projected to stockout within the next 10 days,
with P98420 and P70372 being the most urgent.
Global Parts accounts for the largest reorder load this cycle.
Estimated total PO spend is ₹58,300.
Recommendation: Increase buffer for SKUs with high daily velocity and
follow up with suppliers with >15-day lead times.
```

---

## 🎥 Demo Video Script

> “This is my AI Supply-Chain Agent.  
> It reads our inventory Excel file, forecasts stockouts, auto-generates reorder quantities, creates a purchase order email through an LLM, and sends a real-time email alert when a purchase order is triggered.  
> Finally, it generates a Founder-level business summary. This system can plug directly into Boldfit’s operations workflow.”

---

## 💼 Why This Project Matters

This agent delivers:
- Faster decision-making  
- Fewer stockouts  
- Automated purchasing  
- Reduced manual work  
- Clear visibility for leadership  

It acts as a **plug-and-play operations assistant** for any fast-scaling company.

---

## 🌟 Author  
**Rachit Gupta**  
AI/ML Engineer • Automation Systems • NLP/LLM Specialist
