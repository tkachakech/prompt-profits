import urllib.request
import urllib.error
import json

supabase_url = 'https://ljdltxnxdklslomcolfx.supabase.co'
anon_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxqZGx0eG54ZGtsc2xvbWNvbGZ4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzczNzMzMTksImV4cCI6MjA5Mjk0OTMxOX0.Lg95TAnhmxTfEPIhqkNaB65Q8mAf9LpEMmQw8kEPVJo'

headers = {
    'apikey': anon_key,
    'Authorization': f'Bearer {anon_key}',
    'Content-Type': 'application/json',
    'Prefer': 'return=representation'
}

def fetch_data():
    req = urllib.request.Request(f"{supabase_url}/rest/v1/platforms?select=*", headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        print(f"Error: {e.code} {e.read().decode()}")
        return None

if __name__ == "__main__":
    data = fetch_data()
    print(json.dumps(data, indent=2))
