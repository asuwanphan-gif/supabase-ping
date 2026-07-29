import urllib.request, urllib.error
PROJECTS = [
  ("ssk-rs",
   "https://qidtrlakxasksvovkopo.supabase.co",
   "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
   ".eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFpZHRybGFreGFza3N2b3Zrb3BvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODExMjE0MjAsImV4cCI6MjA5NjY5NzQyMH0"
   ".KBfnDMn0hR-DYSxqJjJ9SxDP2RYyHoLfQstKI3KPq9o"),
  ("waste",
   "https://bsmwdmdnhvntkkguzryp.supabase.co",
   "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
   ".eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJzbXdkbWRuaHZudGtrZ3V6cnlwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzk2MTY3NDIsImV4cCI6MjA5NTE5Mjc0Mn0"
   "._CsT38lEyeLFWs9UOKqSVh651l2CMHPU27l7WxkDBvs"),
  ("immigration-assets",
   "https://aosraqsdgceelwhfwjpm.supabase.co",
   "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
   ".eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFvc3JhcXNkZ2NlZWx3aGZ3anBtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODAwMzQ5MzgsImV4cCI6MjA5NTYxMDkzOH0"
   ".9y1t21ecDjfF1gZamGvH1DmNS9rKnx2lfKK8Uwx3OeE"),
  ("assets",
   "https://cbqukwedykaeqjdidoqa.supabase.co",
   "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
   ".eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNicXVrd2VkeWthZXFqZGlkb3FhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzkxNjE4NjUsImV4cCI6MjA5NDczNzg2NX0"
   ".Qg-_ISPIcGvnb9kPs_z4jof__X9NdXUIw08zDtNrQZM"),
  ("phanssk-bot",
   "https://wptjxlsarzkguitpbqic.supabase.co",
   "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
   ".eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndwdGp4bHNhcnprZ3VpdHBicWljIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcyODc1MjIsImV4cCI6MjA5Mjg2MzUyMn0"
   ".pa_hTULLJSMSBtXOuUiQfqbrqCUy_gnj_0i0k92K2IY"),
  ("stopdrinkssk-ui",
   "https://fvyhpgvmdpzkihvratbg.supabase.co",
   "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
   ".eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ2eWhwZ3ZtZHB6a2lodnJhdGJnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzk2MTY1MzEsImV4cCI6MjA5NTE5MjUzMX0"
   ".P7djsZcyLxjeCLAGAgKfBQLO4kJ6BlsrqXtn1FUJ5xw"),
  ("aphanssk-pixel",
   "https://wdosfpfpslghckedytju.supabase.co",
   "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
   ".eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Indkb3NmcGZwc2xnaGNrZWR5dGp1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODQ3MTA4NjEsImV4cCI6MjEwMDI4Njg2MX0"
   ".YdFVMgxIlnrWLexSb6z_KRtpImm481IYIuSA-u0VpWc"),
]
for name, url, key in PROJECTS:
    try:
        req = urllib.request.Request(
            url + "/rest/v1/rpc/ping",
            method="POST",
            data=b"{}",
            headers={
                "apikey": key,
                "Authorization": "Bearer " + key,
                "Content-Type": "application/json",
            },
        )
        with urllib.request.urlopen(req, timeout=15) as r:
            print("[OK]   " + name + " -> HTTP " + str(r.status))
    except urllib.error.HTTPError as e:
        if 200 <= e.code < 300:
            print("[OK]   " + name + " -> HTTP " + str(e.code))
        elif e.code == 404:
            print("[FAIL] " + name + " -> HTTP 404 (ping() function missing)")
        else:
            print("[FAIL] " + name + " -> HTTP " + str(e.code) + " (paused/blocked)")
    except Exception as e:
        print("[FAIL] " + name + " -> ERROR: " + str(e))
