import { createClient } from '@supabase/supabase-js';

const supabaseUrl = 'https://nujyopdmqolfvvzggyud.supabase.co';
const supabaseAnonKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im51anlvcGRtcW9sZnZ2emdneXVkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTc0NzYyMTEsImV4cCI6MjA3MzA1MjIxMX0.3XB8LIfV52uXJ-SOMUyPOvFBRBZhkz0IBccaSdyh_6c'; // This key is safe to use in a browser

export const supabase = createClient(supabaseUrl, supabaseAnonKey);