import smtplib
from email.mime.text import MIMEText

def send_email_alert(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = "your_email@example.com"
    msg['To'] = "recipient@example.com"
    
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login("your_email@example.com", "password")
        server.send_message(msg)

def monitor_market(df):
    for index, row in df.iterrows():
        if row['Signal'] == 1:
            send_email_alert("Buy Signal", f"Buy at {row['close']} on {row['timestamp']}")
        elif row['Signal'] == -1:
            send_email_alert("Sell Signal", f"Sell at {row['close']} on {row['timestamp']}")

# Example usage
monitor_market(sma_df)
