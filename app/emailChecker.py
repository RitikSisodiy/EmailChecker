import dns.resolver
import socket,smtplib


def check_smtp_server(email):
    try:
        domain = email.split("@")[1]
        answers = dns.resolver.resolve(domain, 'MX')
        for rdata in answers:
            smtp_server = str(rdata.exchange).rstrip(".")
            print(f'SMTP server for {email} is {smtp_server}')
            return smtp_server
    except:
        print(f"Failed to find SMTP server for {email}")
        return None
def checkmail(emails):
    res = {
        "message":"",
    }
    if len(emails)>50:
        res["message"]="50 emails at a time"
        return res ,400
    valid = []
    invalid = []
    someEmails = emails
    mx = check_smtp_server(emails[0])
    domain = emails[0].split("@")[1]
    try:
        server = smtplib.SMTP(mx, 25)
    except:
        res["message"]="unable to connect to the domain"
        return res,500
    server.ehlo(name=domain)
    server.mail("supertool@mxtoolboxsmtpdiag.com")
    for email in someEmails:
        status, _ = server.rcpt(email)
        if status >= 200 and status <= 250:
            valid.append(email)
        else:
            print(_)
            invalid.append(email)
        # print(,email)
    server.quit()
    res["message"] = "success"
    res["valid"] = valid
    res["invalid"] = invalid
    return res,200