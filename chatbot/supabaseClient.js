import { createClient } from '@supabase/supabase-js'
import dotenv from 'dotenv'

// .env 파일 로드
dotenv.config()

// Supabase 연결 정보 (환경 변수에서 가져오기)
const supabaseUrl = process.env.SUPABASE_URL
const supabaseKey = process.env.SUPABASE_KEY

// Supabase 클라이언트 생성
const supabase = createClient(supabaseUrl, supabaseKey)

export default supabase
