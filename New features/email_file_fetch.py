import imaplib
import email
from email.header import decode_header
import os

def download_attachments():
    """
    It will download the attachment from the mail with the help of specific subject.
    :return: filename
    """
    mail_user = "manthan0404soni@gmail.com"
    mail_pass = "ydbvvkqkcmmbajlm"
    subject_to_find = "Bacancy Technology LLP Work Sessions Report"

    imap = imaplib.IMAP4_SSL("imap.gmail.com") # Connect to the Gmail IMAP server
    imap.login(mail_user, mail_pass) # Login to the account
    imap.select("inbox") # To select the mailbox

    status, messages = imap.search(None, f'(SUBJECT "{subject_to_find}")') # Search for the specific email (based on subject in this example)

    email_ids = messages[0].split() # Convert the result to a list of email IDs

    if email_ids:
        latest_email_id = email_ids[-1] # Fetch the latest email (the last email ID in the list)

        # Fetch the email by ID
        res, msg = imap.fetch(latest_email_id, "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                # Parse the email content
                msg = email.message_from_bytes(response[1])
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):
                    subject = subject.decode()
                print(f"Processing the latest email with Subject: {subject}")

                # If the email has multiple parts
                if msg.is_multipart():
                    for part in msg.walk():
                        # If part is an attachment
                        if part.get_content_disposition() == "attachment":
                            filename = part.get_filename().split('_')
                            extension = filename[-1].split('.')
                            extension = extension[-1]
                            filename = f"{filename[4]}.{extension}"
                            if filename:
                                # Download attachment to the Downloads folder
                                filepath = os.path.join("Downloads", filename)
                                with open(filepath, "wb") as f:
                                    f.write(part.get_payload(decode=True))
                                return filename
                else:
                    print("No attachments found.")
    else:
        print("No email found with the given subject.")

    # Close the connection and logout
    imap.close()
    imap.logout()