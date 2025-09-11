import { createClient } from '@supabase/supabase-js';

const supabaseUrl = 'https://nujyopdmqolfvvzggyud.supabase.co';
const supabaseAnonKey = 'sb_publishable_R1lbMf8In7Nn5zu0jKsxkw_NXgFJli6'; // This key is safe to use in a browser

export const supabase = createClient(supabaseUrl, supabaseAnonKey);