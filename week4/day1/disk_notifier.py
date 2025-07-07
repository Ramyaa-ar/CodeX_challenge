import shutil
import smtplib
from email.message import EmailMessage

# ----------------------------------------
# Check disk usage
# ----------------------------------------
total, used, free = shutil.disk_usage("/mnt/c/")
percent_used = used / total * 100

# ----------------------------------------
# Email setup
# ------------------------com----------------
sender_email = "21bcs463@gecskp.ac.in"      # <-- Your Gmail address
receiver_email = "21bcs463@gecskp.ac.in"  # <-- Can be same as sender
app_password = "ihpmkdukuydxgwkg"              # <-- Your App Password (NO SPACES!)

# Create email content
msg = EmailMessage()
msg.set_content(f"""
Hello,

This is your daily disk usage report:

- Total: {total / (1024**3):.2f} GB
- Used: {used / (1024**3):.2f} GB
- Free: {free / (1024**3):.2f} GB
- Usage: {percent_used:.2f}%

Best regards,
Disk Notifier Bot
""")

msg['Subject'] = f"Daily Disk Usage Report — Used: {percent_used:.2f}%"
msg['From'] = sender_email
msg['To'] = receiver_email

# Send email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_email, app_password)
    smtp.send_message(msg)

print("✅ Email sent successfully!")
