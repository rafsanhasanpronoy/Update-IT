-- Run this once in the Supabase SQL Editor before deploying code that
-- writes previous academic results. Existing student records remain valid.
ALTER TABLE public.students
    ADD COLUMN IF NOT EXISTS previous_exam_name varchar(150),
    ADD COLUMN IF NOT EXISTS previous_exam_year integer,
    ADD COLUMN IF NOT EXISTS previous_institution_name varchar(200),
    ADD COLUMN IF NOT EXISTS previous_gpa numeric(5, 2),
    ADD COLUMN IF NOT EXISTS previous_result_details text;

ALTER TABLE public.students
    ADD CONSTRAINT students_previous_exam_year_range
        CHECK (previous_exam_year IS NULL OR previous_exam_year BETWEEN 1900 AND 2100),
    ADD CONSTRAINT students_previous_gpa_range
        CHECK (previous_gpa IS NULL OR previous_gpa BETWEEN 0 AND 5);
