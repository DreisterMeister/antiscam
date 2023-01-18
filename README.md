# antiscam
A simple python script who sends scammers fake data to hopefully confuse them.

Maybe you have to change the payload data. Check the phishing website sourcecode how they wannt the payload.
E.g:  
     $.ajax({
            method: "POST",
            url: "home.php" + location.search,
      --->  data: { user: user1, pass: pass1 } <---
Then change the variables "email" and "password" so its matches the needed data. in this case it would be:  
user1 = names.get_full_name().replace(" ", ".") + "@" + random.choice(emails)
pass1 = ''.join(random.choice(wlist))
payload = {"user":user1,"pass":pass1}
and also
print(f"Sending No.{counter}: {user1} and {pass1}")

The wordlist must be in the same directory as the script or specified as a relative path and in UTF-8 format to work without problems.

Only use this tool to send a few data per day.

Dont change or delete the time.sleep value.

Dont DoS the scammer server.

Only use for ethical purposes!
