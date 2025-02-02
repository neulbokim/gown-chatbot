import supabase from './supabaseClient.js'

async function fetchStudents() {
  const { data, error } = await supabase
    .from('students')
    .select('*')

  if (error) {
    console.error("❌ 데이터 조회 실패:", error)
  } else {
    console.log("✅ 학생 데이터:", data)
  }
}

fetchStudents()
