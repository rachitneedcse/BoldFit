import pandas as pd
from openai import OpenAI
from mail_helper import send_email_notification
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("api_key")
)

def generate_po_email(sku, qty, supplier, email):
    prompt = f"""
    Write a short, professional Purchase Order email:

    SKU: {sku}
    Quantity: {qty}
    Supplier: {supplier}
    Supplier Email: {email}

    Keep it concise (5-6 lines), formal, and ready to send.
    """
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content

def summary_agent(data):
    prompt = f"""
    Create a concise business summary for a Founder’s Office.
    Here is the forecast data:

    {data.to_string()}

    Summarize:
    - Which SKUs are most critical (stockout soon)
    - Which suppliers show the highest reorder load
    - Total reorder cost (if UnitCost is present)

    Keep it short (5-6 lines).
    """
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content

def run_agent(path):
    df = pd.read_excel(path)
    df = df.head(5)

    results = []

    for _, row in df.iterrows():
        sku = row["ProductID"]
        stock = row["QuantityInStock"]
        lead = row["LeadTime"]
        sales_30 = row["sales_last_30"]
        supplier = row["Supplier"]
        email = row["SupplierContact"]
        cost = row["UnitCost"]

        avg_daily_sales = sales_30 / 30
        days_left = stock / avg_daily_sales

        reorder_qty = 0
        po_email = ""
        notification_text = ""

        if days_left < lead:
            reorder_qty = int(avg_daily_sales * (lead + 7))
            po_email = generate_po_email(sku, reorder_qty, supplier, email)

            
            est_cost = reorder_qty * cost

            
            notification_text = f"PO triggered for {sku}: {reorder_qty} units. Estimated cost: ₹{round(est_cost,2)}"
            email_subject = f"PO Triggered for {sku}"
            email_message = notification_text
            send_email_notification(email_subject, email_message)


        results.append({
            "SKU": sku,
            "StockLeft": stock,
            "AvgDailySales": round(avg_daily_sales, 2),
            "DaysUntilStockout": round(days_left, 1),
            "Recommended Reorder Qty": reorder_qty,
            "PO Email": po_email,
            "Supplier": supplier
        })

    output = pd.DataFrame(results)
    print("\n Forecast Results ")
    print(output)

    output.to_csv("forecast_results.csv", index=False)

    
    founder_summary = summary_agent(output)
    print("\n Founder Summary ")
    print(founder_summary)

    with open("founder_summary.txt", "w",encoding="utf-8") as f:
        f.write(founder_summary)

    print("\nFiles saved: forecast_results.csv, founder_summary.txt")

run_agent("inventory.xlsx")
