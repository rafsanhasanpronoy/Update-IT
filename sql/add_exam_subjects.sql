-- Per-subject maximum marks for each examination.
-- Run this script in the Supabase SQL Editor BEFORE deploying the application
-- changes that use the ExamSubject model.
--
-- Existing exams are backfilled with every subject belonging to their class,
-- using the exam's current full_marks value. This preserves the old behaviour.

CREATE TABLE IF NOT EXISTS exam_subjects (
    id BIGSERIAL PRIMARY KEY,
    exam_id BIGINT NOT NULL REFERENCES exams(id) ON DELETE CASCADE,
    subject_id BIGINT NOT NULL REFERENCES subjects(id) ON DELETE RESTRICT,
    full_marks NUMERIC(6,2) NOT NULL DEFAULT 100
        CHECK (full_marks > 0 AND full_marks <= 999),
    CONSTRAINT exam_subjects_exam_subject_unique UNIQUE (exam_id, subject_id)
);

CREATE INDEX IF NOT EXISTS exam_subjects_exam_id_idx
    ON exam_subjects (exam_id);

INSERT INTO exam_subjects (exam_id, subject_id, full_marks)
SELECT e.id, s.id, COALESCE(e.full_marks, 100)
FROM exams e
JOIN subjects s ON s.class_id = e.class_id
ON CONFLICT (exam_id, subject_id) DO NOTHING;

-- Verify the migration. Each existing exam should now list its class subjects.
SELECT
    e.id AS exam_id,
    e.exam_name,
    COUNT(es.id) AS configured_subjects
FROM exams e
LEFT JOIN exam_subjects es ON es.exam_id = e.id
GROUP BY e.id, e.exam_name
ORDER BY e.id;
