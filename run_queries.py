import sqlite3

con = sqlite3.connect("data/sample.db")
cur = con.cursor()

print("=== Query 1: All students ===")
for row in cur.execute("""
    SELECT id, name, cohort, country, prereq_score
    FROM students
    ORDER BY prereq_score DESC
"""):
    print(row)

print("\n=== Query 2: High scorers ===")
for row in cur.execute("""
    SELECT name, country, prereq_score
    FROM students
    WHERE prereq_score >= 80
    ORDER BY prereq_score DESC
"""):
    print(row)

print("\n=== Query 3: Average by cohort ===")
for row in cur.execute("""
    SELECT cohort, COUNT(*) AS student_count, ROUND(AVG(prereq_score), 1) AS avg_score
    FROM students
    GROUP BY cohort
    ORDER BY avg_score DESC
"""):
    print(row)

print("\n=== Query 4: Students + projects (non-missing) ===")
for row in cur.execute("""
    SELECT s.name, s.cohort, p.title, p.week, p.status, p.grade
    FROM students s
    JOIN projects p ON s.id = p.student_id
    WHERE p.status != 'missing'
    ORDER BY s.name, p.week
"""):
    print(row)

con.close()