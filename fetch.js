const { createClient } = require('@supabase/supabase-js');
const SUPABASE_URL = 'https://ljdltxnxdklslomcolfx.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxqZGx0eG54ZGtsc2xvbWNvbGZ4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzczNzMzMTksImV4cCI6MjA5Mjk0OTMxOX0.Lg95TAnhmxTfEPIhqkNaB65Q8mAf9LpEMmQw8kEPVJo';
const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

async function main() {
  const { data, error } = await supabase.from('platforms').select('*');
  if (error) console.error('Error fetching:', error);
  else console.log(JSON.stringify(data, null, 2));
}
main();
